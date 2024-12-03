from models.db_models import Instructor, Project, Milestone
from models.database import get_db
from sqlalchemy.orm import joinedload


class DBOps : 
    def __init__(self) : 
        self.db = get_db()

class DashboardGenerator(DBOps) : 
    def __init__(self, instructor_id: str = "") -> None : 
        self.instructor_id = instructor_id  
        super().__init__()

    def __fetch_available_projects(self) : 
        all_projects = self.db.query(Project).all()
        return all_projects

    def __check_registration(self) : 
        user_details = self.db.query(Instructor).filter(Instructor.id == self.instructor_id).first()
        if user_details.project_id : 
            return {"registered" : True, "project_id" : user_details.project_id}
        else : 
            return {"registered" : False, "new_project" : self.__fetch_available_projects()}


    def get_dashboard(self) : 
        return {"status" : self.__check_registration()}
    
class FetchProjectReport(DBOps) : 
    def __init__(self, project_id: str) : 
        self.project_id = project_id
        super().__init__()

    def fetch(self) : 
        project_details = (
            self.db.query(Project)
            .filter(Project.id == self.project_id)
            .options(
                joinedload(Project.milestones).joinedload(Milestone.checklists)
            )
            .first()
        )

        return project_details