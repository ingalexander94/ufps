import re
from database.config import Connection
from util import response, helpers

class Institutional:
    
    def findUser(self, sql, type, value, user):
        if type=="codigo":
            type = type if user == "student" else "cod_profesor"
            if not value or not value.isnumeric() or len(value) < 5 or len(value) > 7 :
                return response.sendError("El código es incorrecto", 400)
        else:
            type = type if user == "student" else "emaili"
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            if not re.fullmatch(regex, value):
                return response.sendError("El correo es incorrecto", 400)
        db = Connection() 
        sql = f"{sql}" %(value, value, "%MOD.ACU.012%", value, value)  if user == "student" else f"{sql}" %(type, value)  
        data = db.querySimple(sql) 
        db.close()
        if data:
            data["nombre"] = data["nombre"].rstrip()
            data["apellido"] = data["apellido"].rstrip()
            if user == "teacher":
                data["esActivo"] = data["esactivo"] == "TRUE"
                del data["esactivo"]
            else:
                data["riesgo"] = 1 if data["ac012"] == "TRUE" else 5
                data["ac012"] = data["ac012"] == "TRUE"
        return response.sendError("No se obtuvierón resultados",404) if not data else response.sendSuccess("Usuario obtenido con exito", data)
    
    def getCourses(self, sql, code, user):
        if not code or not code.isnumeric() or len(code) < 5 or len(code) > 7 :
                return response.sendError("El código es incorrecto", 400)
        db = Connection() 
        if user == "student":
            codeProgram = code[0:3]
            codeStudent = code[3:7]
            sql = f"{sql}" %(codeProgram, codeStudent)
        else:
            sql = f"{sql}" %(code)
        data = db.queryMultiple(sql) 
        db.close()
        
        if data:
            convert = helpers.convertStudent if user == "student" else helpers.convertTeacher
            data = list(map(convert, data))
        return response.sendError("No se obtuvierón resultados",404) if not data else response.sendSuccess("Cursos obtenidos con exito", data)
    
    