from fastapi import File, UploadFile, HTTPException, APIRouter, Form
from AI_service.controllers.generate_milestones import MilestoneGenerator 
import uuid
from utils.web_socket_util import push_notification
router = APIRouter(prefix="/v1", tags=["generate milestones"])
@router.post("/generate-milestone/")
async def generate_milestone(file: UploadFile = File(...)): 
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Invalid file type. Only PDF files are allowed.")
    
    unique_id = str(uuid.uuid4()) 
    milestone_obj = MilestoneGenerator(unique_id = unique_id, pdf_file = file)
    res = milestone_obj.generate_milestone()
    await push_notification(to_role="student", message="new milestone ready, please take action")
    return {"result" : res}