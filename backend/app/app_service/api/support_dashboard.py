from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.db_models import SupportTeam
from models.database import get_db   
from utils.auth_utils import * 
from utils.db_operations import *  
from datetime import datetime
from app_service.controllers.fetch_support_dashboard import DashboardGenerator
from app_service.schema.dahboard import Feedback
 
router = APIRouter(prefix="/v1", tags=["support dashboard"])

@router.get("/get-support-dashboard")
def get_student_dashboard(db: Session = Depends(get_db), user_id: str = "") : 
    existing_support = db.query(SupportTeam).filter(SupportTeam.id == user_id).first()
    if not existing_support : 
        raise HTTPException(status_code=400, detail="Support team id is not matching")
    
    else :
        obj = DashboardGenerator(support_id=user_id) 
        return obj.get_dashboard()