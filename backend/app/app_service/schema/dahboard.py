from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class ProjectEnroll(BaseModel):
    user_id: str = Field(..., description="ID of the user")
    role: str = Field(..., description="role of the user")
    project_id: str  = Field(..., description="ID of the project the user wants to enroll in")

class ChecklistUpdate(BaseModel):
    id: int
    name: str
    description: str
    code_required: bool
    deadline: int
    # milestone_id: str

class MilestoneUpdate(BaseModel):
    id: str
    name: str
    description: str
    # project_id: str 
    deadline: str 
    checklists: List[ChecklistUpdate]
    index: str

class ProjectUpdate(BaseModel):
    id: str
    name: str
    description: str
    deadline: str
    file_path: str 
    milestones: List[MilestoneUpdate]
    creation_date: str

class Feedback(BaseModel) : 
    feedback: str = Field(..., description="student feedback")
    user_id: str = Field(..., description="ID of the user giving the feedback") 