from AI_service.llm_ops.llm_base import LLMBase
from utils.pdf_utils import TextExtractorFromPDF
from AI_service.schema.milestone import ProjectMilestones
from store.prompt_store import MILESTONE_BREAKDOWN
from models.database import get_db
from models.db_models import Project, Milestone, Checklist
from utils.elaborator import generate_elaborated_output
from datetime import datetime, timedelta
from utils.db_operations import add_entry
import uuid

class MilestoneGenerator(LLMBase) : 
    def __init__(self, pdf_file, unique_id: str, debug: bool = True, store_in_db: bool = True) -> None : 
        super().__init__(prompt = MILESTONE_BREAKDOWN, schema = ProjectMilestones, temperature = 0.3)
        self.pdf_file = pdf_file
        self.unique_id = unique_id
        self.debug = debug 
        self.store_in_db = store_in_db 
        self.db = get_db()

    def generate_milestone(self) : 
        extractor_obj = TextExtractorFromPDF(pdf_file = self.pdf_file, unique_id = self.unique_id)
        pdf_text, pdf_file_path = extractor_obj.extract() 
        if not pdf_text : 
            return {"message" : "failure"}
        
        llm_output = self.generate_output(project_description = pdf_text)
        llm_output["project_id"] = self.unique_id 

        if self.store_in_db : 
            project_deadline_days, milestone_start, current_date = 0, datetime.now().date(), datetime.now().date()
            for milestone in llm_output["milestones"] : 
                milestone_deadline_days, unique_milestone_id = 0, str(uuid.uuid4())  
                for checklist in milestone["checklist"] : 
                    milestone_deadline_days += int(checklist["time_in_days"])
                    project_deadline_days += int(checklist["time_in_days"])

                    new_checklist = Checklist(
                        name = checklist["task_title"], description = checklist["task_description"], 
                        code_required = checklist["coding_required"], deadline = checklist["time_in_days"], 
                        milestone_id = unique_milestone_id
                    )

                    checklist_entry = add_entry(
                        entry= new_checklist, success_key="name", 
                        success_value=new_checklist.name
                    )
                    
                milestone_target_date = milestone_start + timedelta(days=milestone_deadline_days)
                milestone_start = milestone_target_date
                new_milestone = Milestone(
                    id = unique_milestone_id, name = milestone["milestone_title"], 
                    description = milestone["milestone_description"], 
                    deadline = milestone_target_date, project_id = str(self.unique_id)
                )
                milestone_entry = add_entry(
                    entry= new_milestone, success_key="name", 
                    success_value=new_milestone.name
                )

            project_target_date = current_date + timedelta(days=project_deadline_days)
            new_project = Project( 
                id = str(self.unique_id), name = llm_output["project_title"], 
                description = llm_output["project_description"],
                file_path = pdf_file_path, deadline = project_target_date, 
                creation_date = datetime.now()
            )
            project_entry = add_entry(
                entry = new_project, success_key="id", 
                success_value= new_project.id
            )

        return {"message" : "success", "output" : llm_output}


