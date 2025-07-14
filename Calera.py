from clases import *

app = QW.QApplication()

sesion = {
    "id": 0,
    "nombre": "",
    "permiso": "UE"
}
grupos_proyecto = VentanaPrincipal(sesion)

app.exec()