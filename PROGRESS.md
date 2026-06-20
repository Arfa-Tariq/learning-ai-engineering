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

## ✅ Exercise 01: FastAPI – University Student Directory API

**Status:** ✅ Complete  
**Folder:** `exercises/01-fastapi-intro/`  
**Date Completed:** June 2026

### Milestones

- [x] Setup FastAPI project structure
- [x] Create GET / endpoint (service information)
- [x] Create GET /student/{student_id} endpoint (path parameter)
- [x] Create GET /search?name= endpoint (query parameter)
- [x] Add Pydantic response models
- [x] Add HTTPException error handling (404)
- [x] Add parameter validation (min_length, ge, le)
- [x] Test all endpoints via Swagger UI
- [x] Write professional README documentation

### What I Learned from Exercise 01

**Technical:**
- FastAPI application setup with `uvicorn`
- Path parameters vs Query parameters (critical distinction)
- Pydantic models for response validation
- HTTPException for proper API error handling
- Parameter validation with `Path()` and `Query()`
- Automatic API documentation (Swagger/ReDoc)

**Mistakes I Made:**
- Confused Path and Query parameters (used Path for query parameter)
- Hardcoded student ID instead of making it dynamic
- Returned mock data instead of filtering search results
- Forgot to handle "student not found" cases

**Fixed:**
- Used `Query(...)` for search endpoint (not `Path`)
- Made student ID a dynamic path parameter
- Implemented proper filtering in search
- Added 404 error handling for missing students

**Key Takeaway:**
- Path parameters = identify a specific resource (`/student/101`)
- Query parameters = filter or paginate results (`/search?name=john`)

### Time Spent
- Setup and environment: 10 minutes
- Writing code: 25 minutes
- Debugging and fixing: 15 minutes
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
| FastAPI | - | ✅ | - |
| RAG | - | - | - |
| LangChain | - | - | - |

Last Updated: June 2026