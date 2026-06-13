# Learning Progress Tracker

## Project 01: Pokémon CLI

### Milestones

- [x] Milestone 0: Repository setup and documentation
- [x] Milestone 1: Basic API request, raw JSON output
- [x] Milestone 2: Parse specific fields (name, type, height, weight)
- [x] Milestone 3: Error handling (404, network, timeout)
- [ ] Milestone 4: Random Pokémon bonus
- [ ] Stretch: FastAPI wrapper
- [ ] Stretch: Unit tests with mocking

### What I Learned from Project 01

**Technical:**
- HTTP GET requests with timeout parameter
- JSON parsing and nested data extraction
- Exception hierarchy (ConnectionError, Timeout, JSONDecodeError)
- Virtual environment workflow
- Input sanitization (strip, lower)

**Mistakes I Made:**
- Variable name conflict (file vs filename)
- Calling response.json() multiple times
- Generic exception handling catching KeyboardInterrupt
- Forgetting timeout parameter

**Fixed:**
- Renamed variables properly
- Stored JSON in data variable once
- Added specific exception handlers in correct order
- Added timeout=10

### Time Spent
- Setup and environment: 45 minutes
- Writing code: 30 minutes
- Debugging and fixing: 40 minutes
- Documentation: 20 minutes

---

## Project 02: FastAPI Pokémon API (Planned)

### Milestones

- [ ] Setup FastAPI project structure
- [ ] Create GET /pokemon/{name} endpoint
- [ ] Add error handling (404, 500)
- [ ] Add request validation
- [ ] Write API documentation with Swagger
- [ ] Add rate limiting

---

## Future Projects

### RAG System
- [ ] Research vector databases
- [ ] Implement document ingestion
- [ ] Create retrieval pipeline

### Agentic AI
- [ ] Learn LangChain basics
- [ ] Build simple agent with tools

---

## Skills Matrix

| Skill | Novice | Intermediate | Advanced |
|-------|--------|--------------|----------|
| HTTP Requests | ✅ | - | - |
| JSON Parsing | ✅ | - | - |
| Error Handling | - | ✅ | - |
| Virtual Environments | ✅ | - | - |
| Git/GitHub | ✅ | - | - |
| FastAPI | - | - | - |
| RAG | - | - | - |
| LangChain | - | - | - |

Last Updated: June 2026