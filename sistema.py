import mysql.connector

class Conexion():
    def __init__(self):
        self.conexion = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "calera"
        )
        # self.consultaSelect("SELECT 1 FROM usuarios;", tuple([]))

    def consultaInsert(self, consulta, conjunto_datos):
        cursor = self.conexion.cursor()
        cursor.execute(consulta, conjunto_datos)
        self.conexion.commit()

    def consultaSelect(self, consulta, conjunto_datos):
        cursor = self.conexion.cursor()
        cursor.execute(consulta, conjunto_datos)
        return cursor.fetchall()

    def consultaSelectUnica(self, consulta, conjunto_datos):
        cursor = self.conexion.cursor()
        cursor.execute(consulta, conjunto_datos)
        return cursor.fetchone()
    

conexion = Conexion()

    



