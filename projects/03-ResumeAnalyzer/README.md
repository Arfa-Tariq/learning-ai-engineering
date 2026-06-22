# Resume Analyzer & Critiquer

An AI-powered resume analysis tool that extracts structured information from PDF resumes and provides detailed critiques against job descriptions.

## Features

- **PDF Processing**: Converts resumes to Markdown using Docling
- **Information Extraction**: Extracts name, contact, skills, experience, education, certifications, and summary
- **Job Description Analysis**: Compares resume against job descriptions
- **Detailed Critique**:
  - Match percentage (0-100%)
  - Strengths (3-5 items)
  - Gaps (missing skills/experience)
  - Recommendations (actionable steps)
  - Final verdict (Hire/Strong Consider/Consider/Pass)
- **Interactive UI**: Built with Gradio for easy use

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Docling | PDF to Markdown conversion |
| Groq | LLM inference (Llama 3.3 70B) |
| Gradio | Interactive web UI |
| Python | Core programming language |

## How to Run

1. Open the notebook in Google Colab
2. Run all cells
3. Upload a resume PDF
4. Paste a job description
5. Click "Analyze Resume"

## Sample Results

| Job Role | Match % | Verdict |
|----------|---------|---------|
| Software Engineer | 88% | Strong Consider |
| Data Scientist | 48% | Consider |
| DevOps Engineer | 73% | Strong Consider |

## Project Structure
projects/03-resume-analyzer/
├── resume_analyzer.ipynb # Main notebook
└── README.md # This file


## Learning Objectives

- Build an end-to-end document processing pipeline
- Use Docling for robust PDF extraction
- Design structured prompts for information extraction
- Build a Gradio UI for interactive demos

## Author

Built as part of an AI Engineering learning journey.

## License

MIT – Free for learning and portfolio use.
