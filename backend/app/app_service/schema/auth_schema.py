from pydantic import BaseModel, Field
from typing import Optional

class UserRegistration(BaseModel):
    name: str = Field(..., description="Full name of the user")
    email: str = Field(..., description="Email address of the user")
    password: str = Field(..., min_length=8, description="Password for the account") 
    role: str = Field(..., description="Role of the user")
    github_username: Optional[str] = Field(None, description="GitHub username of the user")

class UserLogin(BaseModel):
    email: str = Field(..., description="Email address of the user")
    password: str = Field(..., description="Password for the account")
    role: str = Field(..., description="Role of the user")