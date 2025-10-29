from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QSize



class VentanaPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicacion")
        boton=QPushButton("Pulsame")
        self.setCentralWidget(boton)
        #self.setFixedSize(QSize(400, 300)) tamaño
        self.setMinimumSize(QSize(200,200))
        self.setMaximumSize(QSize(400,400))






app = QApplication([])
window = VentanaPrincipal()


window.show()
app.exec()