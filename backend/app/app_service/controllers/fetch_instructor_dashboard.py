from models.db_models import *
from models.database import get_db
from sqlalchemy.orm import joinedload
from datetime import datetime
from utils.db_operations import * 
class DBOps : 
    def __init__(self) : 
        self.db = get_db()

class DashboardGenerator(DBOps) : 
    def __init__(self, instructor_id: str = "") -> None : 
        self.instructor_id = instructor_id  
        self.user_details = None
        super().__init__()
    
    def __fetch_available_projects(self) : 
        all_projects = self.db.query(Project).all()
        return all_projects
    
    def __get_leaderboard(self) : 
        all_student, output = self.db.query(Student).all(), []
        for student in all_student : 
            if student.project_id == self.user_details.project_id : 
                all_codes = self.db.query(GitHubAccount).filter(GitHubAccount.student_id == student.id).all()
                max_commit = max([code.total_commit for code in all_codes])

                output.append({
                    "name" : student.name, "max_commit" : max_commit,
                    "id" : student.id
                })

        return output 
    def __get_notifs(self):
            unsent_notifs = (
                self.db.query(Notification)
                .filter(Notification.role == 'instructor')
                .order_by(Notification.id.desc())
                .all()
            )
            notifications = []
            for notif in unsent_notifs:
                notifications.append({"id": notif.id, "message": notif.content, "status": notif.status})
                notif.status = "sent"
                db.commit()
            return notifications
    
    def __fetch_all_feedback(self) : 
        all_feedbacks = self.db.query(StudentSupport).filter(StudentSupport.project_id == self.user_details.project_id).all()
        return all_feedbacks

    def __get_enrolled_students(self) : 
        output = []
        all_students = self.db.query(Project).filter(Project.id == self.user_details.project_id).first().students
        for student in all_students : 
            output.append({
                "id" : student.id, "name" : student.name, "project_id" : student.project_id
            }) 

        return output

    def __find_min_max_checklist_id(self) : 
        all_milestone = self.db.query(Milestone).filter(Milestone.project_id == self.user_details.project_id).all()
        all_checklist_id = []
        for milestone in all_milestone : 
            all_checklist = self.db.query(Checklist).filter(Checklist.milestone_id == milestone.id).all()
            all_checklist_id += [checklist.id for checklist in all_checklist]

        return min(all_checklist_id), max(all_checklist_id)

    def __get_student_progress(self) : 
        output = []
        min_checklist_id, max_checklist_id = self.__find_min_max_checklist_id()
        all_students = self.db.query(Student).filter(Student.project_id == self.user_details.project_id).all()
        for student in all_students :
            max_pdf_checklist, max_code_checklist = -1, -1
            pdf_details = self.db.query(PDF).filter(PDF.uploaded_by == student.id).all()
            code_details = self.db.query(CodeQuality).filter(CodeQuality.written_by == student.id).all()

            for pdf in pdf_details : 
                max_pdf_checklist = max(max_pdf_checklist, int(pdf.checklist_id))

            for code in code_details : 
                max_code_checklist = max(max_code_checklist, int(code.checklist_id))

            abs_checklist = max(max_pdf_checklist, max_code_checklist)-min_checklist_id+1
            abs_max_checklist = max_checklist_id - min_checklist_id+1
            output.append({
                "id" : student.id, "name" : student.name, 
                'current_checklist' : abs_checklist, 
                "percentage" : round((abs_checklist/abs_max_checklist)*100)
            })

            
        return output
    

    def __check_registration(self) : 
        self.user_details = self.db.query(Instructor).filter(Instructor.id == self.instructor_id).first()
        if self.user_details.project_id :  
            return {
                "registered" : True, "project_id" : self.user_details.project_id, 
                "enrolled_student_list" : self.__get_enrolled_students(), 
                "all_feedback" : self.__fetch_all_feedback(),
                "leader_board" : self.__get_leaderboard(), 
                "student_progress" : self.__get_student_progress(),
                "notifications":self.__get_notifs()
                
            }
        else : 
            return {"registered" : False, "new_project" : self.__fetch_available_projects()}


    def get_dashboard(self) : 
        return {"status" : self.__check_registration()}
    
class FetchProjectReport(DBOps) : 
    def __init__(self, project_id: str) : 
        self.project_id = project_id
        super().__init__()

    def __add_current_milestone(self, project_details) : 
        output = {
            "deadline" : project_details.deadline, "name" : project_details.name, 
            "id" : project_details.id, "description" : project_details.description, 
            "file_path" : project_details.file_path, "creation_date" : project_details.creation_date,
            "milestones" : []
        } 
        curr = -1
        for index, milestone in enumerate(project_details.milestones) : 
            if milestone.deadline >= datetime.now().date() : 
                curr = index 
                break 
        
        for index, milestone in enumerate(project_details.milestones) : 
            milestone_details = {
                "id" : milestone.id, "name" : milestone.name, 
                "description" : milestone.description, "deadline" : milestone.deadline,
                "checklists" : []                  
            }  
            if index == curr : milestone_details["index"] = "current"
            elif index < curr: milestone_details["index"] = "past"
            else : milestone_details["index"] = "future"  
            for checklist in milestone.checklists :
                milestone_details["checklists"].append(
                    {
                        "id" : checklist.id, "name" : checklist.name, "description" : checklist.description, 
                        "deadline" : checklist.deadline, "code_required" : checklist.code_required
                    }
                )
            output["milestones"].append(milestone_details)

        return output

    def fetch(self) : 
        project_details = (
            self.db.query(Project)
            .filter(Project.id == self.project_id)
            .options(
                joinedload(Project.milestones).joinedload(Milestone.checklists)
            )
            .first()
        )

        modified_project_details = self.__add_current_milestone(project_details)
        return modified_project_details