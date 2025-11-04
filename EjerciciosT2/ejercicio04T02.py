#Álvarez Romero, Jose Antonio 2DAM

import os
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QPixmap


basedir = os.path.dirname(__file__)         #Guarda la ruta actual del archivo del ejercicio

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi app")

        etiqueta = QLabel("etiqueta")
        etiqueta.setPixmap(QPixmap(os.path.join(basedir, "Gato.jpg")))  #muestra la imagen del mismo directorio que el archivo
        #etiqueta.setPixmap(QPixmap(os.path.join(basedir,imagenes, "Gato.jpg"))) si la imagen estuviera en una carpeta imagenes junto al archivo
        etiqueta.setScaledContents(True)         #Permite redimensionar la imagen junto a la ventana

        self.setCentralWidget(etiqueta)

app = QApplication()
window = Ventana()
window.show()
app.exec()

        
        
