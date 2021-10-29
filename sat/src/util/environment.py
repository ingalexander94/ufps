import os
from dotenv import load_dotenv

load_dotenv()

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
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
SECRET_KEY = os.getenv("SECRET_KEY")

# SQL
STUDENT_BY_CODE = os.getenv("STUDENT_BY_CODE")
TEACHER_BY_CODE = os.getenv("TEACHER_BY_CODE")