from flask import Blueprint
from database.models import Student
from util import environment
from middleware.validate_token import token_required

instance = Student.Student()
student_rest = Blueprint("student_rest", __name__)

@student_rest.route("/email/")
@student_rest.route("/email/<email>")
def findUserByEmail(email=None):
    return instance.findUser(environment.STUDENT_BY_CODE,"email", email, "student")

@student_rest.route("/code/")
@student_rest.route("/code/<code>")
@token_required
def findUserByCode(_,code=None):
    return instance.findUser(environment.STUDENT_BY_CODE,"codigo", code, "student")

@student_rest.route("/courses/")
@student_rest.route("/courses/<code>")
@token_required
def getCourses(_,code=None):
    return instance.getCourses(environment.COURSES_STUDENT, code, "student")

@student_rest.route("/courses/ac012/")
@student_rest.route("/courses/ac012/<code>")
@token_required
def getCoursesAc012(_,code=None):
    return instance.getCoursesAc012(environment.COURSES_AC012, code)

