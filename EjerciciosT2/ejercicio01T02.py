#Álvarez Romero, Jose Antonio 2DAM
from PySide6.QtWidgets import QApplication,QMainWindow, QPushButton
from PySide6.QtCore import QSize




class Ventana(QMainWindow):        #creacion de la clase ventana persoalizada
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejercicio1")       #titulo de la ventana
        boton = QPushButton("Boton")            #boton dentro de la ventana
        self.setCentralWidget(boton)            #centrado
        boton.setFixedSize(QSize(400,300))      #tamaño del boton

        #self.setMaximumSize(600,400)
        #self.setMinimumSize(300,200)

app= QApplication([])

botonind = QPushButton("boton independiente")




window= Ventana()

window.show()
botonind.show()
app.exec()