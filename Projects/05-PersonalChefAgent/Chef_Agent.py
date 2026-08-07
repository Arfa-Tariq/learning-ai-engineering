"""
Personal Chef Agent
====================
A single, continuous pipeline (no manual cell-by-cell running required):

1. Greets the user and asks whether they want to scan a fridge/pantry photo
   or just type their ingredients.
2. If a photo is given, a vision model extracts a raw ingredient list, and a
   cleanup agent normalizes it into a tidy comma-separated list.
3. Hands the ingredient list to a "chef" agent that can search the web for
   recipes, and drops the user into a live back-and-forth chat with that
   agent (memory is preserved across turns via a checkpointer) until they
   type "exit" or "quit".

Setup
-----
1. pip install -r requirements.txt   (see bottom of this file for the list)
2. Set two environment variables before running:
     export GROQ_API_KEY="your-groq-key"
     export TAVILY_API_KEY="your-tavily-key"
   (On Windows: set GROQ_API_KEY=... / set TAVILY_API_KEY=...)
3. Run:
     python personal_chef_agent.py
"""

import base64
import os
import sys

from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langchain.tools import tool
from langchain_groq import ChatGroq
from langgraph.checkpoint.memory import InMemorySaver
from tavily import TavilyClient


# ---------------------------------------------------------------------------
# 1. Configuration / setup (runs once)
# ---------------------------------------------------------------------------

def get_required_env(var_name: str) -> str:
    value = os.environ.get(var_name)
    if not value:
        print(f"\n Missing required environment variable: {var_name}")
        print("   Set it before running this script, e.g.:")
        print(f"     export {var_name}='your-key-here'\n")
        sys.exit(1)
    return value


GROQ_API_KEY = get_required_env("GROQ_API_KEY")
TAVILY_API_KEY = get_required_env("TAVILY_API_KEY")

tavily_client = TavilyClient(TAVILY_API_KEY)


@tool
def web_search(query: str) -> str:
    """Searches the web for the given input query."""
    response = tavily_client.search(query)
    if response.get("answer"):
        return response["answer"]
    elif "results" in response:
        return " ".join(
            r["content"] for r in response["results"] if "content" in r
        )[:3000]
    else:
        return "No relevant information found."


# Text model, used for ingredient cleanup + the chef conversation
llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=GROQ_API_KEY, temperature=0.1)

# Vision model, used only to read ingredients out of a photo
llm_image = ChatGroq(model="qwen/qwen3.6-27b", api_key=GROQ_API_KEY, temperature=0.1)


# ---------------------------------------------------------------------------
# 2. Agents
# ---------------------------------------------------------------------------

image_agent = create_agent(
    model=llm_image,
    system_prompt=(
        "Identify all food items and ingredients visible in the image. "
        "Your response MUST be a comma-separated list of these items, and "
        "ONLY these items. Do NOT include any conversational text, "
        "introductory phrases, explanations, or any form of thought "
        "process. Strictly adhere to outputting just the comma-separated "
        "list."
    ),
)

# Some vision models leak their reasoning ("<think>...</think>") even when
# told not to, so a small cleanup agent normalizes whatever comes back into
# a strictly comma-separated ingredient list.
ingredients_agent = create_agent(
    model=llm,
    system_prompt=(
        "Extract and output only a comma separated list of ingredients "
        "from the provided text. Do not include any other commentary, "
        "reasoning, or formatting."
    ),
)

CHEF_SYSTEM_PROMPT = """
You are a friendly, knowledgeable personal chef.

The user will tell you what ingredients they have on hand. Using the
web_search tool, look up recipes that make good use of those ingredients
(prioritizing ones that use as many of them as possible). Offer a short list
of recipe suggestions, and if the user asks for full instructions on one of
them, search for and provide clear step-by-step instructions.

Keep responses conversational and concise. Ask a clarifying question if the
user's request is ambiguous (e.g. dietary restrictions, cuisine preference,
time available).
"""

chef_agent = create_agent(
    model=llm,
    tools=[web_search],
    system_prompt=CHEF_SYSTEM_PROMPT,
    checkpointer=InMemorySaver(),
)


# ---------------------------------------------------------------------------
# 3. Helpers
# ---------------------------------------------------------------------------

def extract_ingredients_from_image(image_path: str) -> str:
    """Runs the vision agent + cleanup agent on a local image file and
    returns a tidy comma-separated ingredient string."""
    with open(image_path, "rb") as f:
        img_bytes = f.read()
    img_b64 = base64.b64encode(img_bytes).decode("utf-8")

    ext = os.path.splitext(image_path)[1].lower().lstrip(".") or "png"
    mime_type = f"image/{'jpeg' if ext == 'jpg' else ext}"

    multimodal_question = HumanMessage(
        content=[
            {
                "type": "text",
                "text": (
                    "Identify all food items and ingredients visible in the "
                    "image. Your response MUST be a comma-separated list of "
                    "these items, and ONLY these items. Do NOT include any "
                    "conversational text, introductory phrases, "
                    "explanations, or any form of thought process. Strictly "
                    "adhere to outputting just the comma-separated list. "
                    "For example: apple, banana, orange."
                ),
            },
            {"type": "image", "base64": img_b64, "mime_type": mime_type},
        ]
    )

    raw_response = image_agent.invoke({"messages": [multimodal_question]})
    raw_text = raw_response["messages"][-1].content

    cleaned = ingredients_agent.invoke(
        {"messages": [HumanMessage(content=raw_text)]}
    )
    return cleaned["messages"][-1].content.strip()


def chat_with_chef(initial_message: str, thread_id: str = "1") -> None:
    """Sends an initial message to the chef agent, prints the reply, then
    loops on user input until they type exit/quit. Conversation memory is
    preserved across turns via the agent's checkpointer."""
    config = {"configurable": {"thread_id": thread_id}}

    print("\n👨‍🍳 Chef: ", end="", flush=True)
    response = chef_agent.invoke(
        {"messages": [HumanMessage(content=initial_message)]}, config
    )
    print(response["messages"][-1].content)

    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n\nGoodbye! 👋")
            break

        if user_input.lower() in {"exit", "quit"}:
            print("\nGoodbye! 👋")
            break
        if not user_input:
            continue

        response = chef_agent.invoke(
            {"messages": [HumanMessage(content=user_input)]}, config
        )
        print(f"\n👨‍🍳 Chef: {response['messages'][-1].content}")


# ---------------------------------------------------------------------------
# 4. Main flow
# ---------------------------------------------------------------------------

def main() -> None:
    print("=" * 60)
    print(" 👨‍🍳  Personal Chef Agent")
    print("=" * 60)
    print(
        "\nI can suggest recipes based on what you have on hand.\n"
        "Type 'exit' or 'quit' at any time to end the chat.\n"
    )

    choice = input(
        "Do you want to scan a fridge/pantry photo, or type your "
        "ingredients? [photo/type]: "
    ).strip().lower()

    if choice.startswith("p"):
        image_path = input("Path to the image file: ").strip().strip('"')
        if not os.path.isfile(image_path):
            print(f"\nCouldn't find a file at '{image_path}'. Exiting.")
            sys.exit(1)

        print("\nLooking at your photo...")
        ingredients = extract_ingredients_from_image(image_path)
        print(f"\nHere's what I found: {ingredients}")

        confirm = input(
            "\nDoes that look right? Press Enter to continue, or type "
            "corrections: "
        ).strip()
        if confirm:
            ingredients = confirm
    else:
        ingredients = input("\nWhat ingredients do you have? ").strip()

    if not ingredients:
        print("\nNo ingredients given — exiting.")
        sys.exit(1)

    initial_message = (
        f"I have the following ingredients: {ingredients}. What can I make?"
    )
    chat_with_chef(initial_message)


if __name__ == "__main__":
    main()
