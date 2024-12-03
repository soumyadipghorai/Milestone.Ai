from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.db_models import Student
from models.database import get_db   
from utils.auth_utils import * 
from utils.db_operations import *  
from app_service.controllers.fetch_student_dashboard import DashboardGenerator
 
router = APIRouter(prefix="/v1", tags=["student dashboard"])

@router.get("/get-student-dashboard")
def get_student_dashboard(db: Session = Depends(get_db), user_id: str = "") : 
    existing_student = db.query(Student).filter(Student.id == user_id).first()
    if not existing_student : 
        raise HTTPException(status_code=400, detail="Student id is not matching")
    
    else :
        obj = DashboardGenerator(student_id=user_id) 
        return obj.get_dashboard()