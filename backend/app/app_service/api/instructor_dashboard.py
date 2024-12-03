from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.db_models import Instructor, Student, Project
from datetime import datetime
from models.database import get_db   
from utils.auth_utils import * 
from utils.db_operations import * 
from app_service.schema.dahboard import ProjectEnroll, ProjectUpdate
from _temp.config import ROLE_MAPPING
from app_service.controllers.fetch_instructor_dashboard import DashboardGenerator, FetchProjectReport
 
router = APIRouter(prefix="/v1", tags=["instructor dashboard"])

@router.get("/get-instructor-dashboard")
def get_instructor_dashboard(db: Session = Depends(get_db), user_id: str = "") : 
    existing_Instructor = db.query(Instructor).filter(Instructor.id == user_id).first()
    if not existing_Instructor : 
        raise HTTPException(status_code=400, detail="Instructor id is not matching")
    else :
        obj = DashboardGenerator(instructor_id=user_id) 
        return obj.get_dashboard()
    
@router.put("/project-enroll")
def enroll_into_project(user_details: ProjectEnroll, db: Session = Depends(get_db)) : 
    Table = ROLE_MAPPING[user_details.role.lower()]
    existing_user = db.query(Table).filter(Table.id == user_details.user_id).first()
    if not existing_user : 
        raise HTTPException(status_code=400, detail="Instructor id is not matching")
    else :
        existing_user.project_id = user_details.project_id
        db.commit()
        return {"message" : "success", "user_id" : existing_user.id}
    
@router.get("/get-project-details")
def get_project_details(project_id: str) :
    obj = FetchProjectReport(project_id = project_id)
    return obj.fetch()

@router.get("/get-enrolled-students")
def get_enrolled_studentsd(user_id: str, db: Session = Depends(get_db)) : 
    user = db.query(Instructor).filter(Instructor.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Project not found")

    output = []
    all_students = db.query(Project).filter(Project.id == user.project_id).first().students
    for student in all_students : 
        output.append({
            "id" : student.id, "name" : student.name, "project_id" : student.project_id
        })

    return output

@router.put("/update-project")
def update_project(project_details: ProjectUpdate, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_details.id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    # Update project attributes
    project.name = project_details.name
    project.description = project_details.description
    
    project_deadline_days, milestone_start, current_date = 0, datetime.now().date(), datetime.now().date()
    for milestone in project_details.milestones:
        milestone_entry = next((m for m in project.milestones if m.id == milestone.id), None)
        if milestone_entry:
            milestone_entry.name = milestone.name
            milestone_entry.description = milestone.description
            
            # Update checklists
            milestone_deadline_days = 0
            for checklist in milestone.checklists:
                checklist_entry = next((c for c in milestone_entry.checklists if c.id == checklist.id), None)
                if checklist_entry:
                    checklist_entry.name = checklist.name
                    checklist_entry.description = checklist.description
                    checklist_entry.code_required = checklist.code_required
                    checklist_entry.deadline = int(checklist.deadline)
                    milestone_deadline_days += int(checklist.deadline)
                    project_deadline_days += int(checklist.deadline)
    
            milestone_target_date = milestone_start + timedelta(days=milestone_deadline_days)
            milestone_start = milestone_target_date
            milestone_entry.deadline = milestone_target_date

    project_target_date = current_date + timedelta(days=project_deadline_days)
    project.deadline = project_target_date 
    db.commit()
    return {"message": "Project updated successfully"}