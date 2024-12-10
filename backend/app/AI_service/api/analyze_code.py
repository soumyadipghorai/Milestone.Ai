from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.db_models import Student
from models.database import get_db   
from AI_service.controllers.github_analyzer import CodeAnalyzer 
from AI_service.schema.github_summarize import CodeAnalyzerInput

# add similarity score 
router = APIRouter(prefix="/v1", tags=["Analyze codes from github"])
@router.post("/analyze-code/")
async def analyze_code(user_details: CodeAnalyzerInput, db: Session = Depends(get_db)): 
    existing_student = db.query(Student).filter(Student.id == user_details.user_id).first()
    if not existing_student : 
        raise HTTPException(status_code=400, detail="Student id is not matching")
    
    analyzer_obj = CodeAnalyzer(
        username= existing_student.github_username, repo_name= user_details.repo_name, 
        branch_name = user_details.branch_name, checklist_id= user_details.checklist_id, 
        student_id= user_details.user_id
    )
    
    output = analyzer_obj.analyze()
    return output 

@router.get("/get-all-repo/")
async def get_all_repo(user_id: str, db: Session = Depends(get_db)):  
    existing_student = db.query(Student).filter(Student.id == user_id).first()
    if not existing_student : 
        raise HTTPException(status_code=400, detail="Student id is not matching")
    
    analyzer_obj = CodeAnalyzer(username= existing_student.github_username)
    output = analyzer_obj.fetch_repos()
    return output 

@router.get("/get-all-branches/")
async def get_all_branches(user_id: str, repo_name: str, db: Session = Depends(get_db), ):  
    existing_student = db.query(Student).filter(Student.id == user_id).first()
    if not existing_student : 
        raise HTTPException(status_code=400, detail="Student id is not matching")
    
    analyzer_obj = CodeAnalyzer(username= existing_student.github_username, repo_name= repo_name)
    output = analyzer_obj.fetch_branch()
    return output 