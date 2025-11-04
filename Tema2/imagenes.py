from PySide6.QtWidgets import QApplication,QMainWindow,QLabel
from PySide6.QtGui import QPixmap

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("mi app")

        etiqueta = QLabel("Hola!")

        etiqueta.setPixmap(QPixmap("Gato.jpg"))

        ##la imagen tiene q estar en el directorio raiz, para cambiarlo mirar ejercicio04T02
        etiqueta.setScaledContents(True)
        self.setCentralWidget(etiqueta)

app = QApplication([])
window = Ventana()
window.show()
app.exec()