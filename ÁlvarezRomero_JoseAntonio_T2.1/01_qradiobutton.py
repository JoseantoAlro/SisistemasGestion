#Álvarez Romero, Jose Antonio

from PySide6.QtWidgets import QApplication, QMainWindow, QRadioButton

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Botones de radio")

        botones = QRadioButton("Activar funcion")       #creacion del boton

        botones.toggled.connect(self.marcado)           #conectar el boton cada vez que se cambie el estado

        self.setCentralWidget(botones)

    def marcado(self, i):                               #cambia la ventana en función del estado
        if i==1:
            self.setWindowTitle("Función ACTIVADA")
        else:
            self.setWindowTitle("Función DESACTIVADA")

app=QApplication()
window=Ventana()
window.show()
app.exec()