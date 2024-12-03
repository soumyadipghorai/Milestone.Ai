from AI_service.llm_ops.llm_base import LLMBase
from AI_service.schema.github_summarize import OverallSummary, TestReport, CodeSummarizationResult
from store.prompt_store import SUMMARIZE_CODE, TEST_CASE_FAILED, TEST_CASE_PASSED
from utils.generate_instruction_md import convert_list_to_markdown

class InstructorReport(LLMBase) : 
    def __init__(self) : 
        super().__init__(prompt=SUMMARIZE_CODE, schema=OverallSummary)

    def generate_overall_feedback(self, text_content: list) : 
        llm_output = self.generate_output(text_content = convert_list_to_markdown(text_content)) 
        return llm_output
    
class TestPassed(LLMBase) : 
    def __init__(self) : 
        super().__init__(prompt=TEST_CASE_PASSED, schema=TestReport)
    
    def generate_pass_report(self, best_practice, comments) : 
        print(self.prompt)
        llm_output = self.generate_output(best_practice = best_practice, comments = convert_list_to_markdown(comments)) 
        return llm_output
    
class TestFailed(LLMBase) : 
    def __init__(self) : 
        super().__init__(prompt=TEST_CASE_FAILED, schema=TestReport)
    
    def generate_fail_report(self, best_practice, comments) :  
        llm_output = self.generate_output(best_practice = best_practice, comments = convert_list_to_markdown(comments)) 
        return llm_output
    
class StudentReport(TestFailed, TestPassed) : 
    def generate_student_feedback(self, report) : 
        output = {} 
        for key in report : 
            if key != "overall_feedback" : 
                if report[key]["result"] == "failed" : 
                    feedback = self.generate_fail_report(best_practice=key, comments=report[key]["comment"])
                elif report[key]["result"] == "passed" :  
                    feedback = self.generate_pass_report(best_practice=key, comments=report[key]["comment"]) 

                output[key] = {
                    "result" : report[key]["result"], 
                    "feedback" : feedback["description"]
                }

        return output
    
class FeedbackGenerator(InstructorReport, StudentReport) : 
    def generate_report(self, role, **kwargs) : 
        if role == "instructor" : 
            return self.generate_overall_feedback(text_content = kwargs.get("text_content", []))
        else : 
            return self.generate_student_feedback(report = kwargs.get("report", {}))
        
