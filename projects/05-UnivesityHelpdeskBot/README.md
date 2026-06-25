# NED University CIS Helpdesk Bot

A conversational helpdesk chatbot for the Computer & Information Systems Engineering (CIS) Department at NED University, Karachi. Students can ask questions about admissions, programs, faculty, labs, key dates, and graduation requirements — and get accurate, friendly answers drawn from a structured knowledge base.

> **Note:** The `knowledge_base.json` included in this project contains sample dummy data for demonstration purposes. Replace it with your department's real information before deploying.

---

## Features

- 7-step safety and quality pipeline on every message
- LLM-powered intent classification and response generation
- Structured knowledge base (no hallucination — answers are grounded in `knowledge_base.json`)
- Input and output moderation (blocks harmful, illegal, and adult content)
- Automatic response quality evaluation before the student sees anything
- Multi-turn conversation memory
- Gradio web UI with optional debug mode

---

## Project Structure

```
Univesity_Helpdesk_Bot.ipynb   # Main Colab notebook
knowledge_base.json            # All department data
README.md
```

---

## Requirements

- A Google account (to run on Colab)
- A [Groq](https://console.groq.com) API key (free tier works)

---

## Setup on Google Colab

**1. Add your Groq API key to Colab Secrets:**

- Open the notebook in Colab
- Click the 🔑 **Secrets** tab in the left sidebar
- Add a new secret: Name = `groq_key`, Value = your Groq API key
- Toggle **Notebook access** on

**2. Upload `knowledge_base.json` to the Colab session:**

- Click the 📁 **Files** tab in the left sidebar
- Click **Upload to session storage**
- Select `knowledge_base.json`

> Note: uploaded files are temporary — you'll need to re-upload each time the session restarts. To avoid this, store the file in Google Drive and mount it instead (see tip below).

**3. Run all cells** — the Gradio UI will launch with a public link at the bottom of the last cell.

---

## Optional: Load knowledge_base.json from Google Drive

Instead of uploading manually each session, save `knowledge_base.json` to your Drive and add this cell before the `open()` call:

```python
from google.colab import drive
drive.mount('/content/drive')
# Then update the path:
with open('/content/drive/MyDrive/knowledge_base.json', 'r') as f:
    kb = json.load(f)
```

---

## Pipeline — How Every Message Is Processed

Every student message goes through 7 steps before a response is returned:

```
Student message
      │
      ▼
Step 1: Moderate input ─────────── harmful/illegal/adult → blocked immediately
      │
      ▼
Step 2: Classify intent ─────────── LLM maps question to category + specific_query
      │
      ▼
Step 3: Retrieve from KB ────────── fetch matching data from knowledge_base.json
      │
      ▼
Step 4: Generate response ───────── LLM writes a friendly answer using KB as reference
      │
      ▼
Step 5: Moderate output ─────────── check the generated response is also safe
      │
      ▼
Step 6: Evaluate quality ────────── second LLM call: does this actually answer the question?
      │
      ▼
Step 7: Approve or escalate ─────── Y → return response │ N → direct student to department
```

---

## Knowledge Base Coverage

The bot can answer questions about the following topics:

| Category | What it covers |
|---|---|
| `university` | University name |
| `department` | Department name and field |
| `location` | City and country |
| `contact` | Phone, email, website, student portal |
| `admissions` | BS, MS, and PhD requirements, deadlines, fees, scholarships |
| `programs` | Core courses, credit hours for BS / MS / PhD |
| `faculty` | Dr. Ahmed Ali, Dr. Sara Khan, Dr. Hassan Raza, Dr. Umar Malik |
| `labs` | AI Lab, Networks Lab, Software Lab |
| `key_dates` | Career fair, hackathon, tech talks |
| `bs_graduation_requirements` | Credits, minimum CGPA, internship, capstone project |

To extend the bot, add new entries to `knowledge_base.json` and update the category list in the `classify_intent` prompt inside `university_helpdesk_bot.py`.

---

## Functions Reference

| Function | Purpose |
|---|---|
| `get_completion_from_messages()` | Sends a message list to the Groq LLM and returns the reply |
| `moderation_check()` | Classifies input as safe / harmful / illegal / adult |
| `classify_intent()` | Maps a student question to KB categories and specific keys |
| `parse_classification()` | Safely parses the LLM's JSON output into a Python list |
| `get_kb_entry()` | Looks up a specific entry in the knowledge base |
| `format_data()` | Recursively formats KB data into readable text |
| `generate_response_from_kb()` | Assembles KB data for all classified intents |
| `process_user_message()` | Runs the full 7-step pipeline |
| `chat_interface()` | Gradio handler — rebuilds conversation history each turn |

---

## Debug Mode

Enable **Show Debug Info in Console** in the Gradio UI, or pass `debug=True` when calling `process_user_message()` directly. You'll see each step printed as it runs:

```
Step 1: Input passed moderation check.
Step 2: Extracted intent: [{'category': 'admissions', 'specific_query': 'bs'}]
Step 3: Looked up information from knowledge base.
Step 4: Generated response to user question.
Step 5: Response passed moderation check.
Step 6: Model evaluated the response → 'Y'
Step 7: Model approved the response.
```

---

## Model

Uses `llama-3.1-8b-instant` via the Groq API. To switch models, change the `model` parameter in `get_completion_from_messages()`. Any model available on Groq will work.

---

## Contact

For questions about the CIS department not covered by the bot:
📧 cis@neduet.edu.pk | 📞 +92-21-12345678 | 🌐 https://cis.neduet.edu.pk
