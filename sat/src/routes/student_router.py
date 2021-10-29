from flask import Blueprint
from database.models import Student
from util import environment
from middleware.validate_token import token_required

instance = Student.Student()
student_rest = Blueprint("student_rest", __name__)

@student_rest.route("/code/")
@student_rest.route("/code/<code>")
@token_required
def findUserByCode(_,code=None):
    return instance.findUser(environment.STUDENT_BY_CODE,"codigo", code, "student")

@student_rest.route("/email/")
@student_rest.route("/email/<email>")
def findUserByEmail(email=None):
    return instance.findUser(environment.STUDENT_BY_CODE,"email", email, "student")