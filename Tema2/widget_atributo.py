from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit
from PySide6.QtCore import QSize
class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("mi app")
        self.setMinimumSize(QSize(480,320))

        texto = QLineEdit()
        texto.textChanged.connect(self.textoModificado)

        self.texto=texto    #para q la funcion lo lea ya q el connect no envia el valor del texto

        self.setCentralWidget(texto)

    def textoModificado(self):
        self.setWindowTitle(self.texto.text())

app = QApplication()
window = Ventana()
window.show()
app.exec()
