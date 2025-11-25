from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton

class Ventna(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("aplicacion con mensaje critico")

        boton = QPushButton("Haz clic para var el mensaje critico")
        boton.clicked.connect(self.mostrar_dialogo)
        self.setCentralWidget(boton)

    def mostrar_dialogo(self):
        boton_pulsado = QMessageBox.critical(
            self,
            "titulo ejemplo de mensaje critico",
            "txto que va en la ventana, HA OCURRIDO UN PROBLEMA",
            buttons= QMessageBox.Discard | QMessageBox.NoToAll | QMessageBox.Ignore,
            defaultButton= QMessageBox.Discard
        )
        if boton_pulsado == QMessageBox.Discard:
          print("descartado")
        elif boton_pulsado == QMessageBox.NoToAll:
            print("No a todo")
        else:
            print("Ignorado")

app = QApplication()
window = Ventna()
window.show()
app.exec()           