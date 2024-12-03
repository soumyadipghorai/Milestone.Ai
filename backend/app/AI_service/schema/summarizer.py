from pydantic import BaseModel, Field
from typing import List, Optional

class SummarizerResponseSchema(BaseModel):
    summary: str = Field(..., description="The generated summary of the project report")
    key_insights: Optional[List[str]] = Field(..., description="List of key insights extracted from the project report")
    additional_notes: Optional[str] = Field(..., description="Any extra notes or metadata related to the summary")
    tags: Optional[List[str]] = Field(..., description="List of tags associated with the project report.")
    conclusions: List[str] = Field(..., description="List of conclusions drawn from the project")   
    recommendations: Optional[List[str]] = Field(..., description="Recommendations for the project, if any")  