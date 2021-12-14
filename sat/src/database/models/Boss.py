from database.config import Connection
from util import response

class Boss:
    def getCoursesOfSemester(self, sql, semester, program):
        if not program or not program.isnumeric() or len(program) != 3:
            return response.sendError("El código del programa es incorrecto", 400)
        db = Connection() 
        sql = f"{sql}" %(program, semester)
        data = db.queryMultiple(sql) 
        db.close()
        return response.sendError("No se obtuvierón resultados", 404) if not data else response.sendSuccess("Cursos obtenidos con exito", data)
    
    def getGroupsOfCourse(self, sql, course, program):
        if not program or not program.isnumeric() or len(program) != 3:
            return response.sendError("El código del programa es incorrecto",400)
        db = Connection() 
        sql = f"{sql}" %(program, course)
        data = db.queryMultiple(sql) 
        db.close()
        return response.sendError("No se obtuvierón resultados", 404) if not data else response.sendSuccess("Grupos obtenidos con exito", data)
    
    def getSemestersOfProgram(self, sql, program):
        if not program or not program.isnumeric() or len(program) != 3:
            return response.sendError("El código del programa es incorrecto",400)
        db = Connection() 
        sql = f"{sql}" %(program, '%CURSO DE%')
        data = db.querySimple(sql) 
        db.close()
        return response.sendError("No se obtuvierón resultados", 404) if not data["semestres"] else response.sendSuccess("Cantidad de semestres obtenida con exito", data)
    
