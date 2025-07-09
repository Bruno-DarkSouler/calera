from clases import *

app = QW.QApplication()

sesion = {}
grupos_proyecto = BuscadorProyectos(sesion)

app.exec()