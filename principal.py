from clases import *

app = QW.QApplication()

sesion = {
    "id": 0,
    "nombre": "",
    "permiso": "UE"
}
grupos_proyecto = TablaUsuarios(sesion)

app.exec()