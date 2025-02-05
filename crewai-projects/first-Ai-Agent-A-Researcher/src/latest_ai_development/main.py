#!/usr/bin/env python
# src/latest_ai_development/main.py
import sys
from fastapi import FastAPI
from .crew import LatestAiDevelopmentCrew  # Updated import statement

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Latest AI Development Crew"}

@app.post("/run/")
def run(inputs: dict):
    """
    Run the crew with the provided inputs.
    """
    LatestAiDevelopmentCrew().crew().kickoff(inputs=inputs)
    return {"status": "Crew has been kicked off", "inputs": inputs}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
