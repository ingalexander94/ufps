from database.models.Institutional import Institutional
from database.config import Connection
from util import response

class Student(Institutional):
    
    def getCoursesAc012(self, sql, code):
        if not code or not code.isnumeric() or len(code) != 7 :
            return response.sendError("El código es incorrecto", 400)
        db = Connection() 
        sql = f"{sql}" %(code)
        data = db.queryMultiple(sql) 
        db.close()
        return response.sendError("No se obtuvierón resultados", 404) if not data else response.sendSuccess("Cursos obtenidos con exito", data)
    