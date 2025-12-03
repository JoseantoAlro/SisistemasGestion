from PySide6.QtWidgets import QPushButton, QApplication, QMainWindow

class BotonContador(QPushButton):
    def __init__(self, parent=None):
        texto_inicial = "pulsado 0 veces"
        super().__init__(texto_inicial, parent)
        self.__contador = 0

        self.clicked.connect(self.__incrementar)

    def __incrementar(self):
        self.__contador = self.__contador+1
        nuevo_texto= "Puslado "+ str(self.__contador)+ " veces"
        self.setText(nuevo_texto)

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("prueba")

        boton = BotonContador(self)

        self.setCentralWidget(boton)

app = QApplication([])
ventana =Ventana()
ventana.show()
app.exec()