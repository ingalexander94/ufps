from flask import Blueprint
from database.models import Teacher
from middleware.validate_token import token_required
from util import environment

instance = Teacher.Teacher()
teacher_rest = Blueprint("teacher_rest", __name__)

@teacher_rest.route("/code/")
@teacher_rest.route("/code/<code>")
@token_required
def findUserByCode(_,code=None):
    return instance.findUser(environment.TEACHER_BY_CODE, "codigo", code, "teacher")

@teacher_rest.route("/email/")
@teacher_rest.route("/email/<email>")
def findUserByEmail(email=None):
    return instance.findUser(environment.TEACHER_BY_CODE,"email", email, "teacher")