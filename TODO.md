# Todo List

## Immediate (Next Session)

- [ ] Add random Pokémon feature to pokemon.py
  - Detect if user types "random"
  - Generate random ID between 1 and 1010
  - Fetch by ID instead of name

- [ ] Clean up commented JSON saving code
  - Either remove it completely OR
  - Convert to command-line argument

- [ ] Add docstring to main() function explaining what it does

## Short Term (This Week)

- [ ] Create unit tests for pokemon.py
  - Mock API responses
  - Test error paths
  - Test parsing logic

- [ ] Set up GitHub Actions for automated testing

- [ ] Start FastAPI project structure
  - Create projects/02-fastapi-pokemon/
  - Initialize with main.py
  - Install fastapi and uvicorn

## Long Term (Next Month)

- [ ] Complete FastAPI wrapper
- [ ] Add authentication to FastAPI (API keys)
- [ ] Research RAG frameworks
- [ ] Set up ChromaDB locally

## Learning Resources to Read

- [ ] requests library documentation (timeout section)
- [ ] Python exception hierarchy
- [ ] FastAPI tutorial (official docs)
- [ ] PokeAPI documentation (limit/offset for random)

## Questions for Mentor

- How do I test functions that make API calls without hitting the real API?
- What's the best way to handle rate limiting in production?
- Should I use asyncio for multiple API calls?

## Abandoned Ideas

- Saving JSON by default → Too much clutter
- Using .env for API URL → Not needed (public API)
- Complex input validation → Overkill for this project