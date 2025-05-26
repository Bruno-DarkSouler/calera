import mysql.connector
# import customtkinter
import tkinter as TK


conexion = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "calera"
)

def consultaInsert(consulta, conjunto_datos):
    cursor = conexion.cursor()

    cursor.execute(consulta, conjunto_datos)

    conexion.commit()
    



def consultaSelect(consulta, conjunto_datos):
    cursor = conexion.cursor()

    cursor.execute(consulta, conjunto_datos)

    return cursor.fetchall()



def consultaSelectUnica(consulta, conjunto_datos):
    cursor = conexion.cursor()

    cursor.execute(consulta, conjunto_datos)

    return cursor.fetchone()

ventana = TK.Tk()

ventana.geometry("700x450")