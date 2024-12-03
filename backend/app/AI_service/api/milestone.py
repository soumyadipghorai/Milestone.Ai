from fastapi import File, UploadFile, HTTPException, APIRouter, Form
from AI_service.controllers.generate_milestones import MilestoneGenerator 
import uuid
 
router = APIRouter(prefix="/v1", tags=["generate milestones"])
@router.post("/generate-milestone/")
async def generate_milestone(file: UploadFile = File(...)): 
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Invalid file type. Only PDF files are allowed.")
    
    unique_id = str(uuid.uuid4()) 
    milestone_obj = MilestoneGenerator(unique_id = unique_id, pdf_file = file)
    res = milestone_obj.generate_milestone()
    return {"result" : res}