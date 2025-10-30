#Álvarez Romero, Jose Antonio 2DAM

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicación")

        self.boton = QPushButton("Pulsar")      #ponerle self.boton para poder llamarlo desde la funcion
        self.setCentralWidget(self.boton)

        self.boton.pressed.connect(self.presionar)  #llama a una funcion al presionar
        self.boton.released.connect(self.soltar)    #llama a una funcion al soltar

    def presionar(self):
        print("boton presionado")
        self.boton.setText("Soltar")        #cambia el texto del boton

    def soltar(self):
        print("Boton liberado")   
        self.boton.setText("Pulsar")
        

app=QApplication()
window = Ventana()
window.show()

app.exec()
