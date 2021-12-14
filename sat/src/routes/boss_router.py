from flask import Blueprint
from database.models import Boss
from middleware.validate_token import token_required
from util import environment

instance = Boss.Boss()
boss_rest = Blueprint('boss_rest', __name__)

@boss_rest.route('/courses/')
@boss_rest.route('/courses/<semester>/<program>')
@token_required
def coursesOfSemester(_, semester=None, program=None):
    return instance.getCoursesOfSemester(environment.COURSES_BY_SEMESTER,semester, program)

@boss_rest.route('/courses/groups/')
@boss_rest.route('/courses/groups/<program>/<course>')
@token_required
def groupsOfCourse(_, program=None, course=None):
    return instance.getGroupsOfCourse(environment.GROUPS_BY_COURSE,course, program)

@boss_rest.route('/semesters/')
@boss_rest.route('/semesters/<program>')
@token_required
def semestersOfProgram(_, program=None):
    return instance.getSemestersOfProgram(environment.SEMESTERS_OF_PROGRAM, program)