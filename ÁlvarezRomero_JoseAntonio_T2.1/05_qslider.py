#Álvarez Romero, Jose Antonio

from PySide6.QtWidgets import QApplication, QMainWindow, QSlider


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ajuste de brillo")

        brillo = QSlider()                      #crea una barra deslizable con valores del 0 al 100 y valor inicial 50
        brillo.setMaximum(100)
        brillo.setMinimum(0)
        brillo.setValue(50)

        brillo.valueChanged.connect(self.cambio_brillo)
        self.setCentralWidget(brillo)



    def cambio_brillo(self, i):             #muestra el valor actual de la barra.
        print("Nivel de brillo: " + str(i) +"%" )
        
app = QApplication()
window = Ventana()
window.show()
app.exec()