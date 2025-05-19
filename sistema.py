import mysql.connector
import tkinter as TK

conexion = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "calera"
)