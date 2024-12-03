from fastapi import File, UploadFile, HTTPException, APIRouter, Form
import uuid
from AI_service.controllers.pdf_analyzer import PdfAnalyzer

# add similarity score 
router = APIRouter(prefix="/v1", tags=["Analyze pdf documents"])
@router.post("/analyze-student-report/")
async def analyze_student_report(user_id: int = Form(...), file: UploadFile = File(...)): 
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Invalid file type. Only PDF files are allowed.")
    
    unique_id = str(uuid.uuid4()) 
    analyzer_obj = PdfAnalyzer(unique_id= unique_id, pdf_file= file)
    output = analyzer_obj.analyze()
    
    output["filename"], output["unique_id"] = file.filename, unique_id
    return output 