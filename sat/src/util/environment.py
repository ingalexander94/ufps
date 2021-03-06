import os
from dotenv import load_dotenv

load_dotenv()

# PING
PING = os.getenv("PING")

# SERVER 
PORT = os.getenv("PORT")

# DB
USER_DB = os.getenv("USER_DB")
PASSSWORD_DB = os.getenv("PASSSWORD_DB")
HOST_DB = os.getenv("HOST_DB")
PORT_DB = os.getenv("PORT_DB")
SERVICE_NAME = os.getenv("SERVICE_NAME")
SERVER = os.getenv("SERVER")

# AUTH
SECRET_KEY = os.getenv("SECRET_KEY")

# SQL
STUDENT_BY_CODE = os.getenv("STUDENT_BY_CODE")
TEACHER_BY_CODE = os.getenv("TEACHER_BY_CODE")
COURSES_STUDENT = os.getenv("COURSES_STUDENT") 
COURSES_TEACHER = os.getenv("COURSES_TEACHER") 
STUDENTS_OF_COURSE = os.getenv("STUDENTS_OF_COURSE") 
TOTAL_PAGES = os.getenv("TOTAL_PAGES") 
STUDENTS_AC012_BY_COURSE = os.getenv("STUDENTS_AC012_BY_COURSE") 
COURSES_AC012 = os.getenv("COURSES_AC012") 
COURSES_BY_SEMESTER = os.getenv("COURSES_BY_SEMESTER") 
GROUPS_BY_COURSE = os.getenv("GROUPS_BY_COURSE") 
GROUP_BY_CODE = os.getenv("GROUP_BY_CODE") 
SEMESTERS_OF_PROGRAM = os.getenv("SEMESTERS_OF_PROGRAM") 
