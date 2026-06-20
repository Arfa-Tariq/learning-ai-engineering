from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="University Student Directory API",
    description="API for managing student information",
    version="1.0.0"
)

# Simulated database
STUDENTS = {
    101: {"name": "John Doe", "major": "Computer Science", "year": 2024},
    102: {"name": "Jane Smith", "major": "Biology", "year": 2023},
    103: {"name": "Bob Johnson", "major": "Mathematics", "year": 2024},
    104: {"name": "Alice Williams", "major": "Computer Science", "year": 2025},
}

# Pydantic Models for response validation
class StudentResponse(BaseModel):
    student_id: int
    name: str
    major: str
    year: int

class SearchResponse(BaseModel):
    search_query: str
    results: List[StudentResponse]
    count: int

@app.get("/")
async def root():
    """Service information and available endpoints"""
    return {
        "service": "Undergraduate Management Portal",
        "version": "1.0.0",
        "status": "operational",
        "endpoints": [
            {"path": "/", "method": "GET", "description": "Service information"},
            {"path": "/student/{student_id}", "method": "GET", "description": "Get student by ID"},
            {"path": "/search?name={name}", "method": "GET", "description": "Search students by name"},
        ],
        "documentation": "/docs",
        "contact": "admin@university.edu"
    }

@app.get("/student/{student_id}", response_model=StudentResponse)
async def student_details(
    student_id: int = Path(..., 
                          description="The student ID", 
                          ge=100, 
                          le=999,
                          example=101)
):
    """Get information about a specific student by their ID"""
    if student_id not in STUDENTS:
        raise HTTPException(
            status_code=404, 
            detail=f"Student with ID {student_id} not found"
        )
    
    return {"student_id": student_id, **STUDENTS[student_id]}

@app.get("/search", response_model=SearchResponse)
async def search(
    name: str = Query(..., 
                     min_length=2, 
                     max_length=50, 
                     description="The name to search for",
                     example="john")
):
    """Search for students by name (case-insensitive partial match)"""
    # Filter students whose name contains the search term (case-insensitive)
    results = [
        {"student_id": sid, **data}
        for sid, data in STUDENTS.items()
        if name.lower() in data["name"].lower()
    ]
    
    if not results:
        raise HTTPException(
            status_code=404, 
            detail=f"No students found matching '{name}'"
        )
    
    return {
        "search_query": name, 
        "results": results, 
        "count": len(results)
    }