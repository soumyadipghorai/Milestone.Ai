import requests
from collections import Counter
from utils.github_utils import GitHubBase
import random
from _temp.config import LANGUAGE_TO_EXTENSION
from tqdm import tqdm
from models.db_models import LanguageGuidelines, CodeQuality, GitHubAccount
from models.database import get_db
import json
# from utils.generate_report import FeedbackGenerator
from utils.generate_instruction_md import convert_best_practices_to_markdown, convert_list_to_markdown
from AI_service.llm_ops.llm_base import LLMBase
from AI_service.schema.github_summarize import CodeSummarizationResult, OverallSummary, TestReport
from store.prompt_store import GUIDELINE_CHECK, SUMMARIZE_CODE, TEST_CASE_FAILED, TEST_CASE_PASSED
import time 
from datetime import datetime
from utils.db_operations import add_entry

db = get_db()

class FetchGitContent(GitHubBase) :
    def __init__(self, username: str, repo_name: str = None) -> None : 
        self.username = username
        self.repo_name = repo_name 
        self.url_endpoint = f"https://api.github.com/repos/{self.username}/{self.repo_name}"
        self.raw_file_endpoint = f"https://raw.githubusercontent.com/{self.username}/{self.repo_name}"
        self.commits = None

    def __fetch_commit(self) :  
        response = requests.get(self.url_endpoint+'/commits')
        commits = response.json()

        if response.status_code == 200 : 
            self.commits = commits
            return True 
        return False  
    
    def fetch_branch(self) -> list : 
        response = requests.get(self.url_endpoint+'/branches', headers = self.get_header())
        all_branches = response.json() 
        return [branch['name'] for branch in all_branches]
    
    def fetch_repos(self) -> list : 
        response = requests.get(f"https://api.github.com/users/{self.username}/repos")
        all_repos  = response.json()
        return [repo["name"] for repo in all_repos]
    
    def _fetch_repo_file_paths(self, branch: str = "master") -> dict : 
        try :
            url = self.url_endpoint + f"/git/trees/{branch}?recursive=1"
        except :  
            url = self.url_endpoint + f"/git/trees/main?recursive=1"
        response = requests.get(url, headers = self.get_header())
        if response.status_code == 200 : 
            tree = response.json().get("tree", [])
            language_mapper = {}
            for file in tree : 
                if file["type"] == "blob" : 
                    language = '.' + file["path"].split('.')[-1]
                    if language not in language_mapper : language_mapper[language] = []
                    language_mapper[language].append(file["path"])

            return language_mapper
        else : 
            response.raise_for_status()
            return {}
    
    def __get_all_commit_message(self) :  
        return [commit["commit"]["message"] for commit in self.commits]
    
    def __get_total_commit(self) :
        return len(self.commits)
    
    def __count_committer(self) : 
        commit_authors = [commit["commit"]["author"]["name"] for commit in self.commits]
        author_commit_count = Counter(commit_authors)
        return author_commit_count
        
    def analyze(self) : 
        if self.__fetch_commit() : 
            return {
                "message" : "success",
                "commit_message" : self.__get_all_commit_message(),
                "total_commit" : self.__get_total_commit(),
                "committer_count" : self.__count_committer(),
            }
        
        return {"message" : "failure"}
    


class InstructorReport(LLMBase) : 
    def __init__(self) : 
        LLMBase.__init__(self, prompt=SUMMARIZE_CODE, schema=OverallSummary)

    def generate_overall_feedback(self, text_content) : 
        llm_output = self.generate_output(text_content = convert_list_to_markdown(text_content)) 
        return llm_output
    
class TestPassed(LLMBase) : 
    def __init__(self) : 
        LLMBase.__init__(self, prompt=TEST_CASE_PASSED, schema=TestReport)
    
    def generate_pass_report(self, best_practice, comments) : 
        llm_output = self.generate_output(best_practice = best_practice, comments = convert_list_to_markdown(comments)) 
        return llm_output
    
class TestFailed(LLMBase) : 
    def __init__(self) : 
        LLMBase.__init__(self, prompt=TEST_CASE_FAILED, schema=TestReport)
    
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
                    "feedback" : feedback
                }

        return output
    

class CodeAnalyzer(LLMBase, FetchGitContent) : 
    def __init__(
            self, username: str, student_id: str = "", checklist_id: int = 0, repo_name:str = None, branch_name: str = None, code_coverage: float = 0.3, 
            language_coverage: float = 0.5, token_limit: int = 5000, save_to_db: bool = True
        ) -> None :  
        FetchGitContent.__init__(self, username=username, repo_name=repo_name)  
        LLMBase.__init__(self, prompt=GUIDELINE_CHECK, schema=CodeSummarizationResult, save_history = True)  
        self.code_coverage = code_coverage
        self.language_coverage = language_coverage
        self.token_limit = token_limit
        self.branch_name = branch_name
        self.save_to_db = save_to_db
        self.checklist_id = checklist_id
        self.student_id = student_id
    
    def __find_used_languages(self) -> dict:
        response = requests.get(self.url_endpoint+'/languages') 
        used_languages = response.json()  
        return used_languages
    
    def __download_files(self, path: str, branch: str = "master") -> str: 
        url =self.raw_file_endpoint + f"/{branch}/{path}"  
        response = requests.get(url, headers = self.get_header())
        response.raise_for_status()
        return response.text
    
    def __fetch_instructions(self, language_name: str) -> dict :  
        existing_language = db.query(LanguageGuidelines).filter(LanguageGuidelines.name == language_name).first()
        if existing_language :
            instructions = existing_language
            return json.loads(instructions.guideline)["best_practices"]
        
        # ? generate entry 
        return "couldn't find"
    
    def __preprocess_code_analysis(self, history, unique_tag: str = "code_analysis") : 
        intermediate_output, final_output = {"overall_feedback" : []}, dict()
        for message in history.messages :  
            structured_msg = json.loads(message.content)
            if "tag" in structured_msg and structured_msg["tag"] == unique_tag : 
                intermediate_output["overall_feedback"].append(structured_msg["overall_feedback"])
                for guideline in structured_msg["guidelines_evaluation"] : 
                    if guideline["guideline"] not in intermediate_output : 
                        intermediate_output[guideline["guideline"]] = {
                            "comment" : [], "passed" : 0, "failed" : 0
                        }
    
                    intermediate_output[guideline["guideline"]]["comment"].append(guideline["comments"])
                    if guideline["is_followed"] : intermediate_output[guideline["guideline"]]["passed"] += 1 
                    else : intermediate_output[guideline["guideline"]]["failed"] += 1 

        for key in intermediate_output : 
            if key == "overall_feedback" : 
                final_output["overall_feedback"] = intermediate_output["overall_feedback"]
            else : 
                final_output[key] = {
                    "result" : "passed" if intermediate_output[key]["passed"] >= intermediate_output[key]["failed"] else "failed", 
                    "comment" : intermediate_output[key]["comment"]
                }   

        return final_output

    def analyze(self):
        code_report = super().analyze() 
        all_paths_in_repo = self._fetch_repo_file_paths(branch=self.branch_name)
        all_languages = self.__find_used_languages() # ! assuming it is already sorted
        total_languages_to_cover = int(len(all_languages)*self.language_coverage)

        code_report["all_paths"] = all_paths_in_repo
        code_report["languages"] = all_languages
        code_report["total_language"] = len(all_languages)
        code_report["total_languages_to_cover"] = total_languages_to_cover

        # ! avoid name mismatching --> sorted_max_freq_path might have images as well 
        max_freq_path = {key:len(value)  for key, value in all_paths_in_repo.items()}
        sorted_max_freq_path = sorted(max_freq_path.items(), key = lambda x: x[1], reverse= True)

        for i, item in enumerate(all_languages.items()) : 
            if i > total_languages_to_cover : 
                break 

            language = item[0] 
            try : # ? if proper naming is not present take most freq files from the repo 
                language_files = all_paths_in_repo[LANGUAGE_TO_EXTENSION[language]]
            except : 
                language_files = all_paths_in_repo[sorted_max_freq_path[i][0]]

            best_practices = self.__fetch_instructions(language)
            best_practices_md = convert_best_practices_to_markdown(best_practices)
            random_code_sample = random.sample(
                population = language_files, k = int(len(language_files)*self.code_coverage)
            )
            
            for j in tqdm(range(len(random_code_sample))) :
                path = random_code_sample[j] 
                raw_file = self.__download_files(path = path, branch=self.branch_name)
                start_point, end_point = 0, max(len(raw_file) - self.token_limit - 1, 0)
                sample_start = random.randint(start_point, end_point)
                sample_code = raw_file[sample_start : sample_start + self.token_limit] # ? avoid empty code 
                llm_output = self.generate_output(
                    language = language, code = sample_code, 
                    best_practices_list = best_practices_md, tag = "code_analysis"
                )
                time.sleep(3) # to avoid burning rate limit  

            code_report["history"] = self.__preprocess_code_analysis(history=self.memory, unique_tag="code_analysis")   
            code_report["instructor_feedback"] = InstructorReport().generate_overall_feedback(text_content=code_report["history"]["overall_feedback"])
            code_report["instructor_commit_summary"] = InstructorReport().generate_overall_feedback(text_content= code_report["commit_message"])
            code_report["student_feedback"] = StudentReport().generate_student_feedback(report= code_report["history"])

            if self.save_to_db :  
                new_code_quality = CodeQuality( 
                    instructor_feedback = json.dumps(code_report["instructor_feedback"]), overall_summary = json.dumps(code_report["student_feedback"]),
                    commit_summary = json.dumps(code_report["instructor_commit_summary"]), checklist_id = self.checklist_id, 
                    upload_time = datetime.now(), repo_name = self.repo_name, branch_name = self.branch_name, 
                    written_by = self.student_id
                )

                new_github_entry = GitHubAccount(
                    username = self.username, total_commit = code_report["committer_count"][self.username], 
                    total_language = json.dumps(code_report["languages"]), repo_name = self.repo_name, 
                    entry_time = datetime.now(), student_id = self.student_id
                )
    
                add_entry(entry = new_github_entry, success_key="id", success_value= new_github_entry.id)
                add_entry(entry = new_code_quality, success_key="id", success_value= new_code_quality.id)
  
            return code_report