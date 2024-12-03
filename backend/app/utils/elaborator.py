from store.prompt_store import EXPAND_TEXT
from AI_service.llm_ops.llm_base import LLMBase
from pydantic import BaseModel, Field 

class ExpandedOutput(BaseModel):
    expanded_output: str = Field(..., description="Elaborated text from the given input text") 
 
def generate_elaborated_output(standard_description: str, standard_title: str, token_limit: int = 500) -> str: 
    llm_obj = LLMBase(prompt = EXPAND_TEXT, schema = ExpandedOutput) 
    llm_output = llm_obj.generate_output(
        description = standard_description, title = standard_title, 
        token_limits = token_limit
    )

    return llm_output
