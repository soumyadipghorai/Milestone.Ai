from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.db_models import Student, StudentSupport
from models.database import get_db   
from utils.auth_utils import * 
from utils.db_operations import *  
from datetime import datetime
from app_service.controllers.fetch_student_dashboard import DashboardGenerator, StudentProjectDetails
from app_service.schema.dahboard import Feedback
from utils.web_socket_util import push_notification
import asyncio
from config.logs import logger
router = APIRouter(prefix="/v1", tags=["student dashboard"])

@router.get("/get-student-dashboard")
def get_student_dashboard(db: Session = Depends(get_db), user_id: str = "") : 
    existing_student = db.query(Student).filter(Student.id == user_id).first()
    if not existing_student : 
        raise HTTPException(status_code=400, detail="Student id is not matching")
    
    else :
        obj = DashboardGenerator(student_id=user_id) 
        try:
            notified_milestone_ids=[notif.milestone_id for notif in db.query(Notification).all()]
            deadline_today_milestones=db.query(Milestone).filter(Milestone.deadline==datetime.now().date(), Milestone.id not in notified_milestone_ids).all()
            for milestone in deadline_today_milestones:
                push_notification(to_role="student", message=f"Today is the last date to submit the following milestone: '{milestone.name}'", db=db)
        except Exception as e:
            logger.error(f"student_dashboard.py:deadline notification:{str(e)}")
        finally:    
           return obj.get_dashboard()
        
    
@router.get("/get-student-project-details")
def get_student_dashboard(user_id: str, db: Session = Depends(get_db)) : 
    existing_student = db.query(Student).filter(Student.id == user_id).first()
    if not existing_student : 
        raise HTTPException(status_code=400, detail="Student id is not matching")
    
    else :
        obj = StudentProjectDetails(project_id=existing_student.project_id, student_id=user_id) 
        return obj.get_project_dashboard()
    
@router.post("/submit-feedback")
def submit_feedback(feedback: Feedback, db: Session = Depends(get_db)) : 
    existing_student = db.query(Student).filter(Student.id == feedback.user_id).first()
    if not existing_student : 
        raise HTTPException(status_code=400, detail="Student id is not matching")
    
    new_feedback = StudentSupport( 
        feedback = feedback.feedback.strip(), tag = "Feedback", 
        feedback_date = datetime.now().date(),
        like_count = 0, comment_count = 0, feedback_by = feedback.user_id, 
        project_id = existing_student.project_id
    )
    
    return add_entry(entry = new_feedback, success_key="feedback", success_value= new_feedback.feedback)
 
 