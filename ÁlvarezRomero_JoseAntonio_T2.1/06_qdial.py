#Álvarez Romero, Jose Antonio

from PySide6.QtWidgets import QApplication, QMainWindow, QDial


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dial")

        dial = QDial()
        dial.setRange(0,10)
        dial.setNotchesVisible(True)        #crea una dial con valores del 0 al 10 con las marcas de valor visibles

        dial.valueChanged.connect(self.cambio_valor)

        self.setCentralWidget(dial)


    def cambio_valor(self,i):               #muestra el valor actual en el titulo de la ventana
        self.setWindowTitle("Volumen: "+str(i)+"/10")
        if (i==10):                         #si el valor es maximo muestra un mensaje especial
            self.setWindowTitle("Volumen máximo alcanzado")

app = QApplication()
window = Ventana()
window.show()
app.exec()

