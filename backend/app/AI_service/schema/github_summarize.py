from pydantic import BaseModel, Field
from typing import List

class GuidelineEvaluation(BaseModel):
    guideline: str = Field(..., description="The specific guideline being evaluated.")
    is_followed: bool = Field(..., description="Indicates if the guideline is followed (True/False).")
    comments: str = Field(..., description="Feedback or comments regarding the code for the guideline.")

class CodeSummarizationResult(BaseModel):
    overall_feedback: str = Field(..., description="Overall feedback of code that is being evaluated.")
    guidelines_evaluation: List[GuidelineEvaluation] = Field(
        ..., description="List of evaluations for each guideline."
    ) 

class SummaryPoint(BaseModel) : 
    title: str = Field(..., description="Title describing a point in summary")
    description: str = Field(..., description="Description abou the suggestion")

class OverallSummary(BaseModel) : 
    key_points: List[SummaryPoint] = Field(..., description="List of summarized information.")

class TestReport(BaseModel) : 
    description: str = Field(..., description="Summarized description of the comments")

class CodeAnalyzerInput(BaseModel) : 
    user_id: str = Field(..., description="User id of the student")
    repo_name: str = Field(..., description="Reposatory name of the student")
    branch_name: str = Field(..., description="Branch name of the selected repo") 
    checklist_id: int = Field(..., description="Checklist ID corresponding to the code")  