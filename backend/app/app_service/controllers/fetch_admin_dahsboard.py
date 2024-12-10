from models.db_models import Admin, StudentSupport, Project, Instructor, Student, Milestone
from models.database import get_db
from sqlalchemy.orm import joinedload
from datetime import datetime
from sqlalchemy import func

class DBOps : 
    def __init__(self) : 
        self.db = get_db()

class DashboardGenerator(DBOps) : 
    def __init__(self, admin_id: str = "") -> None : 
        self.admin_id = admin_id  
        self.user_details = None
        super().__init__()
 
    def __fetch_all_feedback(self) : 
        all_feedbacks = self.db.query(StudentSupport).all()
        return all_feedbacks

    def __fetch_project_details(self) : 
        all_project, project_list = self.db.query(Project).all(), []
        for project in all_project : 
            milestone_details = self.db.query(Milestone).filter(Milestone.project_id == project.id).all() 
            try :
                instructor_details = self.db.query(Instructor).filter(Instructor.project_id == project.id).first() 
                student_details = self.db.query(Student).filter(Student.project_id == project.id).all()
                project_list.append({
                    "instructor_name" : instructor_details.name, "total_student" : len(student_details),
                    "total_milestones" : len(milestone_details), "finish_date" : abs((project.deadline - datetime.now().date()).days), 
                    "status" : "In Progress" if project.deadline >= datetime.now().date() else "Done"
                }) 
            except : 
                project_list.append({
                    "instructor_name" : None, "total_student" : None,
                    "total_milestones" : len(milestone_details), "finish_date" : abs((project.deadline - datetime.now().date()).days),  
                    "status" : "Unassigned"
                })       
        
        all_instructors = self.db.query(Instructor).all() 
        all_students = self.db.query(Student).all() 
        return {
            "total_instructors" : len(all_instructors), "total_students" : len(all_students),
            "project_list" : project_list
        }
    
    def __fetch_progress_report(self) : 
        all_student = self.db.query(
            func.strftime('%Y-%m', Student.enrollment_date).label('month'),   
            func.count().label('count')
        ).group_by(func.strftime('%Y-%m', Student.enrollment_date)).order_by('month').all()

        all_project = self.db.query(
            func.strftime('%Y-%m', Project.creation_date).label('month'),   
            func.count().label('count')
        ).group_by(func.strftime('%Y-%m', Project.creation_date)).order_by('month').all()

        all_date = set() 
        for record in all_student : 
            all_date.add(datetime.strptime(record.month, "%Y-%m").date()) 

        for record in all_project : 
            all_date.add(datetime.strptime(record.month, "%Y-%m").date()) 

        sorted_date = sorted(list(all_date))
        label = [date.strftime("%Y-%m") for date in sorted_date]

        pointer = 0
        project_count = []
        for record in all_project : 
            if record.month == label[pointer] : 
                project_count.append(record.count)
                pointer += 1 

        pointer = 0
        student_count = []
        for record in all_student : 
            if record.month == label[pointer] : 
                student_count.append(record.count)
                pointer += 1 

        return {
            "labels" : label, "datasets" : [
                {
                    "label": 'Projects',
                    "data": project_count,
                    "backgroundColor": 'rgba(0, 123, 255, 0.5)',
                    "borderColor": '#007BFF',
                    "borderWidth": 1,
                },
                {
                    "label": 'Students',
                    "data": student_count,
                    "backgroundColor": 'rgba(52, 58, 64, 0.5)',
                    "borderColor": '#343A40',
                    "borderWidth": 1,
                }
            ]
        } 

    def get_dashboard(self) : 
        self.user_details = self.db.query(Admin).filter(Admin.id == self.admin_id).first() 
        return { 
            "all_feedback" : self.__fetch_all_feedback(), 
            "project_details" : self.__fetch_project_details(), 
            "progress_report" : self.__fetch_progress_report()
        }