# FastAPI Exercise – University Student Directory API

A REST API built with FastAPI that manages student information. Built as a learning exercise to practice path parameters, query parameters, type hints, and Pydantic models.

## Requirements

- Python 3.8 or higher
- FastAPI
- Uvicorn

## Installation and Setup

### Step 1 – Navigate to the exercise folder
cd exercises/01-fastapi-intro


### Step 2 – Install dependencies
pip install fastapi uvicorn


### Step 3 – Run the server
uvicorn main:app --reload


### Step 4 – Open in your browser

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
- Homepage: http://localhost:8000

## API Endpoints

| Method | Endpoint | Description | Parameters |
|--------|----------|-------------|------------|
| GET | / | Service information | None |
| GET | /student/{student_id} | Get a student by ID | Path: student_id (integer) |
| GET | /search?name={name} | Search students by name | Query: name (string, min 2 chars) |

## Request and Response Examples

### Get a student by ID

Request:
GET http://localhost:8000/student/101


Response (200 OK):
{
"student_id": 101,
"name": "John Doe",
"major": "Computer Science",
"year": 2024
}


### Student not found

Request:
GET http://localhost:8000/student/999


Response (404 Not Found):
{
"detail": "Student with ID 999 not found"
}


### Search students by name

Request:
GET http://localhost:8000/search?name=john


Response (200 OK):
{
"search_query": "john",
"results": [
{
"student_id": 101,
"name": "John Doe",
"major": "Computer Science",
"year": 2024
}
],
"count": 1
}


### No search results

Request:
GET http://localhost:8000/search?name=xyz


Response (404 Not Found):
{
"detail": "No students found matching 'xyz'"
}


## Error Handling

| Status Code | Scenario | Example |
|-------------|----------|---------|
| 200 | Success | /student/101 |
| 404 | Student not found | /student/999 |
| 404 | No search results | /search?name=xyz |
| 422 | Validation error | /search?name=a |

## Project Structure
01-fastapi-intro/
├── main.py
├── requirements.txt
└── README.md


## Sample Student Data (Hardcoded)

| Student ID | Name | Major | Year |
|------------|------|-------|------|
| 101 | John Doe | Computer Science | 2024 |
| 102 | Jane Smith | Biology | 2023 |
| 103 | Bob Johnson | Mathematics | 2024 |
| 104 | Alice Williams | Computer Science | 2025 |

## Concepts Practiced

- FastAPI application setup
- Path parameters (/student/{student_id})
- Query parameters (/search?name=)
- Pydantic models for response validation
- Type hints (student_id: int, name: str)
- HTTPException for error handling
- Parameter validation (min_length, max_length, ge, le)
- Automatic API documentation (Swagger/ReDoc)

## Future Improvements

- Replace hardcoded data with a real database (SQLite/PostgreSQL)
- Add POST endpoint to create new students
- Add PUT endpoint to update student information
- Add DELETE endpoint to remove students
- Add authentication/authorization
- Add unit tests with TestClient

## Related Projects

This is Exercise 01 in my FastAPI learning journey:

- Project 01: Pokémon CLI (API consumption)
- Exercise 01: University Student Directory API (API creation)
- Project 02: Full FastAPI Pokémon API (coming soon)

## License

MIT – Free for learning and portfolio use.
