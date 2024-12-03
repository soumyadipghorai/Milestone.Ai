from pydantic import BaseModel, Field
from typing import List, Optional

class CodeExample(BaseModel):
    description: str = Field(..., description="A brief explanation of the example.")
    code: Optional[str] = Field(None, description="Optional code demonstrating the best practice.")

class BestPractice(BaseModel):
    title: str = Field(..., description="A short title of the best practice.")
    explanation: str = Field(..., description="Explanation of why this best practice is important.")
    examples: List[CodeExample] = Field(..., description="List of examples, each with a description and optional code.")

class LanguageBestPracticesResponse(BaseModel):
    language: str = Field(...,  description="The programming language for which best practices are provided.")
    best_practices: List[BestPractice] = Field(..., description="A list of best practices for the given programming language.")
