# Pokémon CLI – API Integration Learning Project

A command-line tool that fetches Pokémon data from the [PokeAPI](https://pokeapi.co). Built to practice HTTP requests, JSON parsing, error handling, and Python development workflows.

---

## Features

- Search any Pokémon by name (case-insensitive, handles spaces)
- Display: Name, Height (meters), Weight (kilograms)
- Robust error handling for:
  - Invalid Pokémon names (404 Not Found)
  - No internet connection
  - API timeout (10 seconds)
  - Invalid JSON responses
  - Keyboard interrupt (Ctrl+C)
- Optional JSON response saving (commented out by default)
- Input sanitization (strip and lowercase)

---

## Requirements

- Python 3.8 or higher
- requests library

---

## Installation & Setup

### 1. Clone the repository

git clone https://github.com/Arfa-Tariq/learning-ai-engineering.git
cd learning-ai-engineering/projects/01-pokemon-cli

### 2. Create and activate virtual environment

Windows (PowerShell):
python -m venv .venv
.\.venv\Scripts\Activate.ps1

Mac/Linux:
python3 -m venv .venv
source .venv/bin/activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Run the program

python pokemon.py

---

## Usage Examples

Valid Pokémon:
Enter the name of a Pokemon: pikachu
Pokemon data saved to pikachu.json.
Pokemon Name: Pikachu
Height(m): 0.4
Weight(kg): 6.0

With capital letters and spaces:
Enter the name of a Pokemon:   CHARIZARD   
Pokemon data saved to charizard.json.
Pokemon Name: Charizard
Height(m): 1.7
Weight(kg): 90.5

Invalid Pokémon:
Enter the name of a Pokemon: pikachuuuu
Error: Pokemon 'pikachuuuu' not found.

No Internet Connection:
Error: No internet connection. Please check your network.

---

## Error Handling Architecture

The code uses Python's exception hierarchy with specific handlers in order:

- ConnectionError – No network connectivity
- Timeout – API takes longer than 10 seconds
- JSONDecodeError – API returns malformed response
- RequestException – Parent class for other request failures
- Exception – Catch-all for unexpected errors

---

## Project Structure

01-pokemon-cli/
├── pokemon.py           # Main application
├── requirements.txt     # Dependencies
└── README.md           # This file

---

## Testing the Code

Run these test scenarios manually:

Test: pikachu
Expected: Shows height 0.4m, weight 6.0kg

Test: "  bulbasaur  "
Expected: Strips spaces, shows data

Test: missingno
Expected: "Pokemon not found" error

Test: Disable WiFi
Expected: "No internet connection" error

Test: Press Ctrl+C
Expected: Exits silently (no error traceback)

---

## What I Learned

Technical Skills:
- Making HTTP GET requests with Python's requests library
- Parsing nested JSON responses from REST APIs
- Exception handling with proper hierarchy (specific to generic)
- Virtual environment setup and dependency management
- Input sanitization for security (strip and lowercase)
- Timeout implementation to prevent hanging requests
- Git workflow for learning projects

Engineering Practices:
- Commenting out non-essential features to reduce clutter
- Meaningful error messages for end users
- Defensive programming (assuming API or network could fail)
- Separation of concerns (main() function for modularity)

---

## Security Considerations

- No hardcoded secrets – PokeAPI requires no authentication
- Input sanitization – strip() prevents path traversal via spaces
- Timeout implemented – Prevents hanging requests (10 second limit)
- No file write vulnerabilities – JSON saving commented by default
- .gitignore configured – Excludes .venv/, *.json, __pycache__/

---

## Future Improvements (Stretch Goals)

- Random Pokémon – Add "random" keyword to fetch any Pokémon by ID (1-1010)
- FastAPI wrapper – Expose functionality as REST API endpoint
- Command-line arguments – save-json flag instead of editing code
- Unit tests – Mock API responses with unittest.mock
- Caching – Store results to reduce repeated API calls
- Type hints complete – Add return types to functions

---

## Portfolio Context

This is Project 01 in my AI Systems Engineering learning journey. Upcoming projects will cover:

- Project 02: FastAPI wrapper for this Pokémon CLI
- Project 03: RAG (Retrieval-Augmented Generation)
- Project 04: Agentic AI with LangChain
- Project 05: MCP (Model Context Protocol) server

---

## License

MIT – Free for learning and portfolio use.

---

## Acknowledgments

- PokeAPI for the free, no-auth Pokémon data
- My AI engineering mentor for code review and system design guidance

Made with Python and determination