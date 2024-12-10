from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.db_models import Admin
from models.database import get_db   
from utils.auth_utils import * 
from utils.db_operations import *  
from app_service.controllers.fetch_admin_dahsboard import DashboardGenerator
 
router = APIRouter(prefix="/v1", tags=["Admin dashboard"])

@router.get("/get-admin-dashboard")
def get_student_dashboard(db: Session = Depends(get_db), user_id: str = "") : 
    existing_admin = db.query(Admin).filter(Admin.id == user_id).first()
    if not existing_admin : 
        raise HTTPException(status_code=400, detail="Student id is not matching")
    
    else :
        obj = DashboardGenerator(admin_id=user_id) 
        return obj.get_dashboard()