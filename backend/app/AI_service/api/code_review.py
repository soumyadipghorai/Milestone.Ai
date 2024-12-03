from fastapi import APIRouter
import uuid
from AI_service.controllers.generate_best_practice import GuidelineGenerator

# add similarity score 
router = APIRouter(prefix="/v1", tags=["Generate best practices for a given language"])
@router.post("/best-practice/")
async def best_practices(language: str = "Python"): 
    analyzer_obj = GuidelineGenerator(language= language)
    output = analyzer_obj.generate()
    return output 