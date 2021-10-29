import re
from database.config import Connection
from util import response

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
        data = db.querySimple(f"{sql} WHERE {type}='{value}'") 
        db.close()
        if data:
            data["nombre"] = data["nombre"].rstrip(),
            data["apellido"] = data["apellido"].rstrip(),
            if user == "student":
                 data = {
                     **data,
                    "foto":"http://placehold.it/32x32",
                    "sexo": "male",
                    "semestre":1,
                    "promedio": 3.25,
                    "promedioPonderadoAcomulado": 3.25,
                    "creditosAprobados": 132,
                    "creditosTotales": 141,
                    "telefono": "+1 (822) 570-2027",
                    "direccion": "736 Java Street, Wakulla, Illinois, 4799",
                    "fechaIngreso": "Tue Jun 29 2018 19:29:00 GMT-0500"
                }
            else:
                data = {
                    **data,
                    "foto":"http://placehold.it/32x32",
                    "sexo": "male",
                    "esActivo": True,
                    "programa": "Ingeniería de Sistemas",
                    "telefono": "+1 (819) 517-2534",
                    "direccion": "348 Saratoga Avenue, Woodruff, Iowa, 5612"
                }
        return response.sendError("No se obtuvierón resultados",404) if not data else response.sendSuccess("Usuario obtenido con exito", data)
    