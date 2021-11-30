from flask import request
from database.config import Connection
from database.models.Institutional import Institutional
from util import response

class Teacher(Institutional):
    
    def getStudentsOfCourse(self, sql, sql2, code, group):
        if not code or not group or group.isnumeric() or not code.isnumeric() or len(code) != 7 or len(group) != 1 :
                return response.sendError("El código o el grupo es incorrecto", 400) 
        db = Connection() 
        codeProgram = code[0:3]
        codeCourse = code[3:7] 
        page = int(request.args.get("page")) or 1
        limit = int(request.args.get("limit")) or 15
        filter = request.args.get("filter") or ""
        if filter:
            filter = f"AND consulta_estudiante.tmatriculado = '{filter}'"
        page = 1 if page == 0 else page
        limit = 15 if limit == 0 else limit
        nUntil = page * limit
        nFrom = int(nUntil) - int(limit)
        sql = f"{sql}" %("%MOD.ACU.012%", codeProgram, codeCourse, group, filter, str(nUntil), str(nFrom))
        data = db.queryMultiple(sql)   
        if data:
            sql2 = f"{sql2}" %(str(limit), codeProgram, codeCourse, group, filter)
            totalPages = db.querySimple(sql2)
            data = list(map(lambda student : {**student, "riesgo": 1 if student["ac012"] == "TRUE" else 5, "ac012": student["ac012"] == "TRUE"} , data))
            info = { "students": data, "totalPages": totalPages["total"] }
        db.close() 
        return response.sendError("No se obtuvierón resultados",404) if not data else response.sendSuccess("Cursos obtenidos con exito", info)
    
    def getStudentsInAC012(self, sql, code, group):
        if not code or not group or group.isnumeric() or not code.isnumeric() or len(code) != 7 or len(group) != 1 :
                return response.sendError("El código o el grupo es incorrecto", 400)  
        db = Connection() 
        codeProgram = code[0:3]
        codeCourse = code[3:7] 
        sql = f"{sql}" %(codeProgram, codeCourse, group, "%MOD.ACU.012%")
        data = db.queryMultiple(sql)   
        if data:
            data = list(map(lambda student : {**student, "ac012": True} , data))
        db.close() 
        return response.sendSuccess("No se obtuvierón resultados", []) if not data else response.sendSuccess("Estudiante obtenidos con exito", data)


