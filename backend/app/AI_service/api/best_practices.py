from fastapi import APIRouter
import uuid
from AI_service.controllers.generate_best_practice import GuidelineGenerator

# add similarity score 
router = APIRouter(prefix="/v1", tags=["Generate best practices for a given language"])
@router.get("/best-practice/")
async def best_practices(): 
    analyzer_obj = GuidelineGenerator()
    output = analyzer_obj.generate()
    return output 