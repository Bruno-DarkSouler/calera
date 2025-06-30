from PySide6 import QtWidgets as QW

def saludar():
    print("Hola mundo!")


# app = QW.QApplication()

# ventana = QW.QMainWindow()
# ventana.resize(200, 100)

# boton = QW.QPushButton("Hola", ventana)
# boton.clicked.connect(saludar)


# ventana.show()

# app.exec()

class VentanaPrincipal(QW.QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(768, 450)

        #Contenedor central
        contenedor_central = QW.QWidget(self)
        self.setCentralWidget(contenedor_central)

        #Contenedor
        contenedor = QW.QVBoxLayout(contenedor_central)

        #Etiqueta
        etiqueta = QW.QLabel("Etiqueta: ")

        #Lista tipo comboBox
        comboBox = QW.QComboBox()
        comboBox.addItems(["Robot SUMO", "SONUS", "Mesa Abatible"])


        #Boton
        boton = QW.QPushButton("Salude")
        boton.clicked.connect(saludar)
        boton.pressed.connect(lambda:print("Voy a decir...\n"))
        boton.resize(50, 50)
        boton.setStyleSheet(
            "QPushButton{" \
            "color:#ff0000;" \
            "border: 3px dotted #000000;" \
            "background-color: rgb(255, 0, 255);}"
            "QPushButton:hover{" \
            "color:#ffeeee;" \
            "border: 3px solid #000000;" \
            "background-color: rgb(0, 0, 255)}"
        )

        contenedor.addWidget(comboBox)
        contenedor.addWidget(etiqueta)
        contenedor.addWidget(boton)

        self.show()

app = QW.QApplication()
# app.setStyle("windows")
app.setStyle("fusion")
#puede no haber app.setStyle()
ventana = VentanaPrincipal()
app.exec()
