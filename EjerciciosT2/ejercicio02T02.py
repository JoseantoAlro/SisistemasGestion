#Álvarez Romero, Jose Antonio 2DAM

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QSize

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicación")

        self.boton = QPushButton("Encender")        #crea un boton 
        self.boton.setCheckable(True)               #lo hace un conmutador

        self.boton.clicked.connect(self.pulsar)     #conecta dos funciones a la accion de pulsar
        self.boton.clicked.connect(self.titulo)

        self.boton.setFixedSize(QSize(700,300))     #da un mayor tamaño para poder leer el titulo de la ventana

        self.setCentralWidget(self.boton)

    def pulsar(self):
        print("Botón pulsado")      

    def titulo(self,pulsado):           #si pasa a encendido cambia el titulo y si pasa a apagado lo vuelve a cambiar
        if pulsado==True:
            self.setWindowTitle("Ventana encendida")
        else:
            self.setWindowTitle("Ventana apagada")
        


app= QApplication()
window = Ventana()
window.show()

app.exec()

