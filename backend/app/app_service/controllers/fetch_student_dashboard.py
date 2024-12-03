from models.db_models import Student, Project
from models.database import get_db

class DashboardGenerator : 
    def __init__(self, student_id: str = "") -> None : 
        self.student_id = student_id 
        self.db = get_db()

    def __fetch_available_projects(self) : 
        all_projects = self.db.query(Project).all()
        return all_projects

    def __check_registration(self) : 
        user_details = self.db.query(Student).filter(Student.id == self.student_id).first()
        if user_details.project_id : 
            return {"registered" : True, "project_id" : user_details.project_id}
        else : 
            return {"registered" : False, "new_project" : self.__fetch_available_projects()}


    def get_dashboard(self) : 
        return {"status" : self.__check_registration()}