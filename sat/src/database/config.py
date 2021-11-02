import cx_Oracle
from util import environment

class Connection:
    
    def __init__(self):
        try:
            dsnStr = cx_Oracle.makedsn(environment.HOST_DB, environment.PORT_DB, environment.SERVICE_NAME)
            self.connect = cx_Oracle.connect(user=environment.USER_DB,password=environment.PASSSWORD_DB, dsn=dsnStr, encoding="UTF-8")
        except Exception as error:
            print("No se puede conectar a la base de datos", error)
        else:
            print("Conexión establecida!!")
            
    def close(self):
        self.connect.close()
        
    def querySimple(self, sql):
        cursor = self.connect.cursor()
        cursor.execute(sql) 
        columns = [col[0].lower() for col in cursor.description]
        cursor.rowfactory = lambda *args: dict(zip(columns, args))
        data = cursor.fetchone()
        cursor.close()
        return data
        
    def queryMultiple(self, sql):
        cursor = self.connect.cursor()
        cursor.execute(sql) 
        columns = [col[0].lower() for col in cursor.description]
        cursor.rowfactory = lambda *args: dict(zip(columns, args))
        data = cursor.fetchall()
        cursor.close()
        return data
        