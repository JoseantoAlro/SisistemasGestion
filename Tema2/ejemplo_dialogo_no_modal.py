from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel


class VentanaNoModal(QLabel):
    def __init__(self):
        super().__init__()
        self.setText("flipo")

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana principal")

        self.otraVentana = None

        self.boton = QPushButton("Mostrar/ocultar ventana")
        self.boton.clicked.connect(self.mostrar_ventana)
        self.setCentralWidget(self.boton)

    def mostrar_ventana(self):

        if self.otraVentana is None:
            self.otraVentana = VentanaNoModal()
            self.otraVentana.show()
        else:
            if self.otraVentana.isHidden():
                self.otraVentana.show()
            else:
                self.otraVentana.hide()

app=QApplication([])
ventana=Ventana()
ventana.show()
app.exec()