from AI_service.llm_ops.llm_base import LLMBase
from AI_service.schema.coding_guidelines import LanguageBestPracticesResponse
from store.prompt_store import GENERATE_BEST_PRACTICES
from _temp.config import LANGUAGE_TO_EXTENSION
from models.database import get_db
from models.db_models import LanguageGuidelines
from tqdm import tqdm

class GuidelineGenerator(LLMBase) : 
    def __init__(self, debug: bool = True) -> None : 
        super().__init__(prompt = GENERATE_BEST_PRACTICES, schema = LanguageBestPracticesResponse) 
        self.debug = debug 
        self.db = get_db()
    
    def generate(self) : 
        for language in tqdm(LANGUAGE_TO_EXTENSION.keys()) :
            try :
                llm_output = self.generate_output(language = language) 
                JSON_DATA = LanguageGuidelines(name = language, guideline = llm_output)
                self.db.add(JSON_DATA)
                self.db.commit()
                self.db.refresh(JSON_DATA)

            except :
                return {"message" : "success", "language" : language}
            
        return {"message" : "success", "language" : "all"}