import os
import logging
from utils.pdf_utils import TextExtractorFromPDF
from store.prompt_store import SUMMARIZE_PDF
from AI_service.schema.summarizer import SummarizerResponseSchema
from AI_service.llm_ops.llm_base import LLMBase

class PdfAnalyzer(LLMBase) : 
    def __init__(self, pdf_file, unique_id: str, debug: bool = False) -> None : 
        super().__init__(prompt = SUMMARIZE_PDF, schema = SummarizerResponseSchema)
        self.pdf_file = pdf_file 
        self.unique_id = unique_id 
        self.debug = debug

    def analyze(self) : 
        extractor_obj = TextExtractorFromPDF(pdf_file = self.pdf_file, unique_id = self.unique_id)
        pdf_text = extractor_obj.extract() 
        if not pdf_text : 
            return {"message" : "failure"}
        return {"message" : "success", "output" : self.generate_output(project_report = pdf_text)}



