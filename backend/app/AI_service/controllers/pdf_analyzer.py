import os
import logging
from utils.pdf_utils import TextExtractorFromPDF
from store.prompt_store import SUMMARIZE_PDF
from AI_service.schema.summarizer import SummarizerResponseSchema
from AI_service.llm_ops.llm_base import LLMBase
from models.db_models import PDF
from models.database import get_db
from datetime import datetime
from utils.db_operations import add_entry
import json

class PdfAnalyzer(LLMBase) : 
    def __init__(
            self, pdf_file, unique_id: str, student_id: str, checklist_id: int, 
            debug: bool = False, store_in_db: bool = True
        ) -> None : 
        super().__init__(prompt = SUMMARIZE_PDF, schema = SummarizerResponseSchema)
        self.pdf_file = pdf_file 
        self.unique_id = unique_id 
        self.debug = debug
        self.store_in_db = store_in_db
        self.student_id = student_id
        self.checklist_id = checklist_id
        self.db = get_db()

    def analyze(self) : 
        extractor_obj = TextExtractorFromPDF(pdf_file = self.pdf_file, unique_id = self.unique_id)
        pdf_text, pdf_file_path = extractor_obj.extract()  
        ai_output = self.generate_output(project_report = pdf_text)

        if self.store_in_db : 
            new_pdf = PDF(
                file_path = pdf_file_path, ai_response = ai_output,
                upload_time = datetime.now(), checklist_id = self.checklist_id,  
                uploaded_by = self.student_id
            )
            project_entry = add_entry(
                entry = new_pdf, success_key="id", 
                success_value= new_pdf.id
            ) 
        if not pdf_text : 
            return {"message" : "failure"}
        return {"message" : "success", "output" : ai_output}



