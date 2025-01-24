from sqlalchemy import (
    Column, String, Integer, Boolean, Date, DateTime, ForeignKey, Text, Table, JSON
)
from sqlalchemy.orm import relationship
from models.database import Base

from sqlalchemy import Column, String, ForeignKey, Integer, Date, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()  

class LanguageGuidelines(Base):
    __tablename__ = "language_guidelines"

    id = Column(Integer, primary_key=True, index=True, autoincrement = True)
    name = Column(String)
    guideline = Column(JSON) 

class Admin(Base):
    __tablename__ = "admin"
    id = Column(String, primary_key=True, nullable = False)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False) 
    enrollment_date = Column(DateTime, nullable= False)

    # projects = relationship("Project", back_populates="admin")

class Project(Base):
    __tablename__ = "projects"
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    file_path = Column(String, nullable = False)
    deadline = Column(Date, nullable = False)
    creation_date = Column(DateTime, nullable= False)
    # admin_id = Column(String, ForeignKey("admin.id"), nullable=False)

    # admin = relationship("Admin", back_populates="projects")
    students = relationship("Student", back_populates="project")
    milestones = relationship("Milestone", back_populates="project")
    feedback = relationship("StudentSupport", back_populates="project_details")
    # chatbots = relationship("Chatbot", back_populates="project")

class Instructor(Base):
    __tablename__ = "instructors"
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    enrollment_date = Column(DateTime, nullable= False)
    project_id = Column(String, ForeignKey("projects.id"), nullable = True) 

class Student(Base):
    __tablename__ = "students"
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    github_username = Column(String, nullable=True)
    password = Column(String, nullable=False)
    project_id = Column(String, ForeignKey("projects.id"), nullable = True) 
    enrollment_date = Column(DateTime, nullable= False)
    # dashboard_id = Column(String, ForeignKey("projects.id"), nullable = True)  
    # chat = Column(String, ForeignKey("projects.id"))  

    project = relationship("Project", back_populates="students")
    uploaded_by = relationship("PDF", back_populates="student")
    written_code_quality = relationship("CodeQuality", back_populates="student")
    llm_feedback = relationship("LLMFeedback", back_populates="student")
    github_profile = relationship("GitHubAccount", back_populates="student")
    student_feedback = relationship("StudentSupport", back_populates='student')
    # dashboard = relationship("StudentDashboard", back_populates="student")
    # chat_history = relationship("ChatHistory", back_populates="student")

class Milestone(Base):
    __tablename__ = "milestones"
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    deadline = Column(Date, nullable = False)
    
    checklists = relationship("Checklist", back_populates="milestone")
    project_id = Column(String, ForeignKey("projects.id"))
    project = relationship("Project", back_populates="milestones")

class Checklist(Base):
    __tablename__ = "checklists"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    deadline = Column(Integer, nullable=False)
    code_required = Column(Boolean, nullable=False)
    
    milestone_id = Column(String, ForeignKey("milestones.id"))
    milestone = relationship("Milestone", back_populates="checklists")
    pdfs = relationship("PDF", back_populates="checklist")
    code_quality = relationship("CodeQuality", back_populates="checklist")
    llm_feedback = relationship("LLMFeedback", back_populates="checklist")

class PDF(Base):
    __tablename__ = "pdfs"
    id = Column(Integer, primary_key=True, autoincrement=True)
    file_path = Column(String, nullable=False)
    ai_response = Column(JSON, nullable= False)
    instructor_feedback = Column(String, nullable=True)
    upload_time = Column(DateTime, nullable=False)
    checklist_id = Column(String, ForeignKey("checklists.id"))
    uploaded_by = Column(String, ForeignKey("students.id"))
    
    checklist = relationship("Checklist", back_populates="pdfs")
    student = relationship("Student", back_populates="uploaded_by")


class GitHubAccount(Base):
    __tablename__ = "github_accounts"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    total_commit = Column(Integer, nullable = True)
    total_language = Column(JSON, nullable = True)
    repo_name = Column(String, nullable= True)
    entry_time = Column(DateTime, nullable= True)
    student_id = Column(String, ForeignKey('students.id'))
    student = relationship("Student", back_populates="github_profile")


# class StudentDashboard(Base):
#     __tablename__ = "student_dashboard"
#     id = Column(String, primary_key=True)
#     monthly_commits = Column(Integer, nullable=False)
#     docs_uploaded = Column(Integer, nullable=False)
#     milestone_progress = Column(String, nullable=True)
    
#     student_id = Column(String, ForeignKey("students.id"))
#     student = relationship("Student", back_populates="dashboard")

# class InstructorDashboard(Base):
#     __tablename__ = "instructor_dashboard"
#     id = Column(String, primary_key=True)
#     approved_pdf = Column(Integer, nullable=False)
#     approved_code = Column(Integer, nullable=False)
#     feedbacks = Column(Integer, nullable=False)
    
#     instructor_id = Column(String, ForeignKey("instructors.id"))
#     instructor = relationship("Instructor", back_populates="dashboard")


class SupportTeam(Base):
    __tablename__ = "support_team"
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False) 
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    enrollment_date = Column(DateTime, nullable= False)
    
"""
# class Bug(Base):
#     __tablename__ = "bugs"
#     id = Column(String, primary_key=True)
#     description = Column(String, nullable=False)
#     status = Column(String, nullable=False)
#     name = Column(String, nullable=False)
#     source = Column(String, nullable=False)

# class Chatbot(Base):
#     __tablename__ = "chatbots"
#     id = Column(String, primary_key=True)
#     project_id = Column(String, ForeignKey("projects.id"))
    
#     project = relationship("Project", back_populates="chatbots")
#     chat_history = relationship("ChatHistory", back_populates="chatbot")

# class ChatHistory(Base):
#     __tablename__ = "chat_history"
#     id = Column(String, primary_key=True)
#     student_id = Column(String, ForeignKey("students.id"))
#     timestamp = Column(DateTime, nullable=False)
#     student_message = Column(String, nullable=False)
#     ai_message = Column(String, nullable=False)
    
#     student = relationship("Student", back_populates="chat_history")
#     chatbot_id = Column(String, ForeignKey("chatbots.id"))
#     chatbot = relationship("Chatbot", back_populates="chat_history")
"""
class CodeQuality(Base):
    __tablename__ = "code_quality"
    id = Column(Integer, primary_key=True, autoincrement=True)
    instructor_inputs = Column(String, nullable=True)
    instructor_feedback = Column(String, nullable=True)
    overall_summary = Column(String, nullable= True)
    commit_summary = Column(String, nullable= True)
    repo_name = Column(String, nullable= True)
    branch_name = Column(String, nullable= True)
    sampled_files = Column(String, nullable= True)
    checklist_id = Column(String, ForeignKey("checklists.id"))
    upload_time = Column(DateTime, nullable= False) 
    
    checklist = relationship("Checklist", back_populates="code_quality")
    written_by = Column(String, ForeignKey("students.id"))
    student = relationship("Student", back_populates="written_code_quality")

class LLMFeedback(Base):
    __tablename__ = "llm_feedback"
    id = Column(String, primary_key=True)
    feedback = Column(String, nullable=False)
    instructor_feedback = Column(String, nullable=True)
    checklist_id = Column(String, ForeignKey("checklists.id"))
    
    checklist = relationship("Checklist", back_populates="llm_feedback")
    feedback_for = Column(String, ForeignKey("students.id"))
    student = relationship("Student", back_populates="llm_feedback")

class StudentSupport(Base) : 
    __tablename__ = "student_support"
    id = Column(Integer, primary_key= True, autoincrement=True)
    feedback = Column(String, nullable= False)
    tag = Column(String, nullable= False)
    feedback_date = Column(Date, nullable= False)
    like_count = Column(Integer, nullable= True)
    comment_count = Column(Integer, nullable= True) 
    feedback_by = Column(String, ForeignKey('students.id'))
    project_id = Column(String, ForeignKey('projects.id'))

    student = relationship("Student", back_populates="student_feedback")
    project_details = relationship('Project', back_populates="feedback")

class Notification(Base):
    __tablename__="notification"
    id=Column(Integer, primary_key=True, autoincrement=True)
    role=Column(String, nullable=False)
    content=Column(String, nullable=False)
    status=Column(String, nullable=False)
    milestone_id=Column(String, nullable=False, default="not_a_milestone")