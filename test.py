from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QScrollArea, QPushButton
)
from PySide6.QtCore import Qt

app = QApplication([])

# Ventana principal
ventana = QWidget()
layout_principal = QVBoxLayout(ventana)

# ScrollArea que contendrá otros widgets
scroll_area = QScrollArea()
scroll_area.setWidgetResizable(True)  # Importante para que el contenido se adapte

# Contenedor interno con layout vertical
contenedor_scroll = QWidget()
layout_scroll = QVBoxLayout(contenedor_scroll)

# Agregamos muchos widgets para que se genere scroll
for i in range(30):
    etiqueta = QLabel(f"Elemento #{i+1}")
    etiqueta.setFixedHeight(40)
    etiqueta.setStyleSheet("background-color: lightgray; border: 1px solid black;")
    layout_scroll.addWidget(etiqueta)

scroll_area.setWidget(contenedor_scroll)

# Agregamos el scroll al layout principal
layout_principal.addWidget(scroll_area)

ventana.resize(300, 400)
ventana.show()
app.exec()
