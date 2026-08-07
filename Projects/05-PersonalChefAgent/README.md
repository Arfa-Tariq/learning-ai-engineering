# 👨‍🍳 Personal Chef Agent

A notebook-based agent that suggests recipes from what you already have.
Show it a photo of your fridge/pantry (or just type your ingredients) and
chat with a chef agent that searches the web for recipes and remembers the
conversation.

## What's inside

- **`Personal_Chef_Agent.ipynb`** — the whole app. Run the cells top to
  bottom once; the last cell renders a small GUI you use for everything
  after that (no re-running cells needed).
- **`Chef_Agent.py`** — a python file implementation of the same agent.
- **`Chef_Agent(test_build).ipynb`** — initial scrap implementation of the chef agent.
## How it works

1. **Vision agent** reads a photo of your fridge/pantry and lists the food
   items it sees.
2. **Cleanup agent** normalizes that into a tidy comma-separated ingredient
   list (vision models sometimes leak extra reasoning text, so this step
   strips that out).
3. **Chef agent** takes the ingredient list, searches the web (via Tavily)
   for matching recipes, and chats back and forth with you — it remembers
   earlier turns in the same session, so you can ask follow-ups like "give
   me the full recipe for #2."

All three agents run on Groq-hosted models via LangChain's `create_agent`,
with a LangGraph `InMemorySaver` checkpointer keeping the chef conversation's
memory.

## Setup

### 1. Get API keys

- **Groq** — [console.groq.com](https://console.groq.com) (free tier
  available)
- **Tavily** (web search) — [tavily.com](https://tavily.com) (free tier
  available)

### 2. Install dependencies

The first notebook cell handles this for you:

```
pip install -q langchain langchain-groq langgraph tavily-python ipywidgets
```

### 3. Provide your keys

Run the notebook's "API keys" cell. It will:

- Use your Colab secrets automatically if you're running in Google Colab
  (secrets named `groq_key` and `tavily_key`)
- Otherwise check for `GROQ_API_KEY` / `TAVILY_API_KEY` environment
  variables
- Otherwise prompt you once with a hidden password input

### 4. Run it

Run every cell in order. The final cell displays the GUI:

- Upload a photo and click **Scan photo for ingredients**, or type your
  ingredients directly into the text box
- Click **Start chat**
- Keep chatting in the message box at the bottom (Enter or the Send button
  both work)

## Notes / known limitations

- Works in both Google Colab and a local Jupyter install.
- The vision model occasionally needs the cleanup pass to strip stray
  reasoning text from its output — this is already handled automatically.
- Conversation memory is in-memory only and resets if you restart the
  kernel or reload the page.
- Image upload accepts standard formats (PNG, JPG, etc.) via the browser
  file picker.

## Requirements

```
langchain
langchain-groq
langgraph
tavily-python
ipywidgets
```
