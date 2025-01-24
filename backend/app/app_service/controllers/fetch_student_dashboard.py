from models.db_models import Student, Project, PDF, CodeQuality, Checklist, GitHubAccount
from models.database import get_db
from app_service.controllers.fetch_instructor_dashboard import FetchProjectReport
import json
from sqlalchemy import func
from datetime import datetime
from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from utils.web_socket_util import Manager
from config.logs import logger
from sqlalchemy.orm import Session
from models.database import get_db   
from utils.db_operations import * 
import random
from fastapi.responses import JSONResponse

class DBOps : 
    def __init__(self) : 
        self.db = get_db()

class DashboardGenerator(DBOps) : 
    def __init__(self, student_id: str = "") -> None : 
        self.student_id = student_id 
        self.project_id = None
        super().__init__()  

    def __fetch_available_projects(self) : 
        all_projects = self.db.query(Project).all()
        return all_projects
    
    def __get_language_details(self) : 
        if(self.db.query(GitHubAccount).filter(GitHubAccount.student_id == self.student_id).first()):
            github_details = json.loads(self.db.query(GitHubAccount).filter(GitHubAccount.student_id == self.student_id).first().total_language) 
            if github_details:
                return {
                    "labels" : list(github_details.keys()), "datasets" : [
                        {
                            "label": "Language Used",
                            "data": list(github_details.values()) ,
                            "backgroundColor":  [f'rgba(0, 123, 255, {1.0 - 1/len(github_details.keys())*i})' for i in range(len(github_details.keys()))],
                            "borderColor": "#ffffff",
                            "borderWidth": 2,
                        }
                    ]
                }
        else:
             return {}
        
    def __get_metric(self) : 
        
        all_codes = self.db.query(GitHubAccount).filter(GitHubAccount.student_id == self.student_id).all()
        return {
            "pdf_count" : len(self.db.query(PDF).filter(PDF.uploaded_by == self.student_id).all()),
            "code_count" : max([code.total_commit for code in all_codes])
        }  
    
    def __create_leaderboard(self) :
        all_student, output = self.db.query(Student).all(), []
        for student in all_student : 
            if student.project_id == self.project_id : 
                all_codes = self.db.query(GitHubAccount).filter(GitHubAccount.student_id == student.id).all()
                max_commit = max([code.total_commit for code in all_codes])

                output.append({
                    "name" : student.name, "max_commit" : max_commit,
                    "id" : student.id
                })

        return output
    
    def __generate_progress_chart(self):
        all_pdf_record = self.db.query(
            func.strftime('%Y-%m', PDF.upload_time).label('month'),   
            func.count().label('count')
        ).filter(PDF.uploaded_by == self.student_id).group_by(func.strftime('%Y-%m', PDF.upload_time)).order_by('month').all()

        all_code_record = self.db.query(
            func.strftime('%Y-%m', GitHubAccount.entry_time).label('month'),
            func.sum(GitHubAccount.total_commit).label('total_value')
        ).filter(GitHubAccount.student_id==self.student_id).group_by(func.strftime('%Y-%m', GitHubAccount.entry_time)).order_by('month').all()

        all_date = set() 
        for record in all_pdf_record : 
            all_date.add(datetime.strptime(record.month, "%Y-%m").date()) 

        for record in all_code_record : 
            all_date.add(datetime.strptime(record.month, "%Y-%m").date()) 

        sorted_date = sorted(list(all_date))
        label = [date.strftime("%Y-%m") for date in sorted_date]

        pointer = 0
        pdf_count = []
        for record in all_pdf_record : 
            if record.month == label[pointer] : 
                pdf_count.append(record.count)
                pointer += 1 

        pointer = 0
        commit_count = []
        for record in all_code_record : 
            if record.month == label[pointer] : 
                commit_count.append(record.total_value)
                pointer += 1 

        return {
            "labels" : label, "datasets" : [
                {
                    "label": 'Commits',
                    "data": commit_count,
                    "backgroundColor": 'rgba(0, 123, 255, 0.5)',
                    "borderColor": '#007BFF',
                    "borderWidth": 1,
                },
                {
                    "label": 'Reports Uploaded',
                    "data": pdf_count,
                    "backgroundColor": 'rgba(52, 58, 64, 0.5)',
                    "borderColor": '#343A40',
                    "borderWidth": 1,
                }
            ]
        }
    def __get_notifs(self):
            unsent_notifs = (
                self.db.query(Notification)
                .filter(Notification.role == 'student')
                .order_by(Notification.id.desc())
                .all()
            )
            notifications = []
            for notif in unsent_notifs:
                notifications.append({"id": notif.id, "message": notif.content, "status": notif.status})
                notif.status = "sent"
            db.commit()
            return notifications
    def __check_registration(self) : 
        user_details = self.db.query(Student).filter(Student.id == self.student_id).first()
        self.project_id = user_details.project_id 
        if user_details.project_id : 
            return {
                "registered" : True, "project_id" : user_details.project_id, 
                "language_details" : self.__get_language_details(), 
                "metric" : self.__get_metric(), "leader_board" : self.__create_leaderboard(),
                "progress_chart" : self.__generate_progress_chart(),
                "notifications":self.__get_notifs()
            }
        else : 
            return {
                "registered" : False, "new_project" : self.__fetch_available_projects()
            }


    def get_dashboard(self) : 
        return {"status" : self.__check_registration()}
    
class StudentProjectDetails(FetchProjectReport) : 
    def __init__(self, project_id: str, student_id: str) :  
        super().__init__(project_id=project_id)
        self.user_id = student_id
        self.github_base = "https://github.com"

    def fecth_feedback(self) : 
        all_feedback, output = self.db.query(CodeQuality).filter(CodeQuality.written_by == self.user_id).all(), []
        github_username = self.db.query(Student).filter(Student.id == self.user_id).first().github_username
        for feedback in all_feedback :
            checklist_details = self.db.query(Checklist).filter(Checklist.id == feedback.checklist_id).first()
            sample_codes = list(json.loads(feedback.sampled_files).items())
            random.shuffle(sample_codes)
            
            random_sampl_code_output, i, pointer = {}, 0, 0
            while i < 3 : 
                if len(sample_codes[pointer][1]['code']) > 0 :
                    random_sampl_code_output[sample_codes[pointer][0]] = sample_codes[pointer][1]
                    i += 1
                    pointer += 1
                else : 
                    pointer += 1             

            output.append({
                "name" : checklist_details.name, "checklist_id" : checklist_details.id, 
                "instructor_feedback" : json.loads(feedback.instructor_feedback), "id" : feedback.id,
                "overall_summary" : json.loads(feedback.overall_summary), "commit_summary" : json.loads(feedback.commit_summary), 
                "project_url" : f'{self.github_base}/{github_username}/{feedback.repo_name}/tree/{feedback.branch_name}', 
                "sampled_files" : random_sampl_code_output
            }) 

        return output

    def get_uploaded_docs(self) : 
        all_pdfs, output = self.db.query(PDF).filter(PDF.uploaded_by == self.user_id).all(), []
        for pdf in all_pdfs : 
            output.append({
                "id" : pdf.id, "file_path" : pdf.file_path, "ai_response" : pdf.ai_response, 
                "instructor_feedback" : pdf.instructor_feedback, "checklist_id" : pdf.checklist_id, 
                "name" : pdf.file_path.split("__")[-1]
            })

        return output
    def notifs(self):
            unsent_notifs = (
                self.db.query(Notification)
                .filter(Notification.role == 'student')
                .order_by(Notification.id.desc())
                .all()
            )
            notifications = []
            for notif in unsent_notifs:
                notifications.append({"id": notif.id, "message": notif.content, "status": notif.status})
                notif.status = "sent"
            db.commit()
            return notifications

    def get_project_dashboard(self) : 
        return {
            "project_details" : self.fetch(), "uploaded_docs" : self.get_uploaded_docs(), 
            "code_feedback" : self.fecth_feedback(),
            "notifications":self.notifs()
        } 