from PySide6.QtWidgets import QApplication, QWidget, QLabel, QGraphicsOpacityEffect, QVBoxLayout
from PySide6.QtCore import QPropertyAnimation, QEasingCurve

app = QApplication([])

# Crear un widget simple (una ventana con texto)
widget = QWidget()
widget.setWindowTitle("Animación de Opacidad")
widget.setFixedSize(300, 200)

contenedor = QVBoxLayout(widget)

label = QLabel("Hola, soy un widget animado!")
label.move(50, 80)



# Aplicar un efecto de opacidad al widget
opacity_effect = QGraphicsOpacityEffect(contenedor)
contenedor.setGraphicsEffect(opacity_effect)

# Crear una animación para la propiedad 'opacity' del efecto
animation = QPropertyAnimation(opacity_effect, b"opacity")
animation.setDuration(100)           # 1 segundo
animation.setStartValue(0.0)          # Comienza totalmente transparente
animation.setEndValue(1.0)            # Termina totalmente visible
animation.setEasingCurve(QEasingCurve.InOutQuad)

# Mostrar el widget
animation.start()
widget.show()

# Iniciar la animación justo después de mostrarlo

app.exec()
