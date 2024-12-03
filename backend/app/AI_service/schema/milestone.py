from pydantic import BaseModel, Field
from typing import List

class ChecklistItem(BaseModel):
    task_title: str = Field(..., description="A title of the task in the checklist.")
    task_description: str = Field(..., description="A description of the task in the checklist. Each description must be of atleast 500 words")
    time_in_days: int = Field(..., description="Time required to complete the task in days.")
    coding_required: bool = Field(..., description="If this is a coding task or not")

class Milestone(BaseModel):
    milestone_title: str = Field(..., description="The title or name of the milestone.")
    milestone_description: str = Field(..., description="The descriptive explanation of the milestone. Each description must be of atleast 200 words")
    checklist: List[ChecklistItem] = Field(..., description="A list of tasks with time estimates under this milestone.")

class ProjectMilestones(BaseModel): 
    project_title: str = Field(..., description="A brief title of the project.")
    project_description: str = Field(..., description="A short description of the project. The description must be of atleast 200 words")
    milestones: List[Milestone] = Field(..., description="A list of milestones with checklists and time estimates.")

class ProjectInputSchema(BaseModel):
    title: str = Field(..., description="The title of the project") 
