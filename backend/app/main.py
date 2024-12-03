from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from config.logs import logger
from models.database import engine, Base 
from models.db_models import *
from models.database import get_db
from utils.db_operations import insert_into_language_guidelines

Base.metadata.create_all(bind=engine)

db = get_db()
entries = db.query(LanguageGuidelines).all()
if not entries :
    insert_into_language_guidelines()

app = FastAPI(
    title="AI-Assisted Project Tracking System",
    description="A web-based application designed to assist instructors in tracking student projects using AI.",
    version="1.0.0",
    license_info={
        "name": "Apache 2.0",
        "url": "http://www.apache.org/licenses/LICENSE-2.0.html",
    }
)

app.add_middleware(
    CORSMiddleware, allow_origins = ["*"], allow_credentials = True, 
    allow_methods = ["*"], allow_headers = ["*"],
)

@app.get("/")
def read_root():
    logger.info("logger activated")
    return {"message": "Success"}



from AI_service.api.milestone import router as create_milestone_router
from AI_service.api.analyze_pdf import router as pdf_analyzer_router 
from AI_service.api.analyze_code import router as code_analyzer_router 
from AI_service.api.best_practices import router as coding_best_practices_router  
from app_service.api.auth_api import router as authentication_router  
from app_service.api.student_dashboard import router as student_dahboard_router   
from app_service.api.instructor_dashboard import router as instructor_dashboard_router

app.include_router(create_milestone_router)
app.include_router(pdf_analyzer_router)
app.include_router(code_analyzer_router)
app.include_router(coding_best_practices_router)
app.include_router(authentication_router)
app.include_router(student_dahboard_router)
app.include_router(instructor_dashboard_router)

if __name__ == "__main__" : 
    uvicorn.run("main:app", host = "0.0.0.0", reload=True)