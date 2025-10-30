#Álvarez Romero, Jose Antonio 2DAM
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import Qt

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi app")

        label = QLabel("Sistema en espera")         #crea un labe y ajusta el tamaño
        fuente = label.font()
        fuente.setPointSize(24)

        label.setFont(fuente)
        label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)        #alinea abajo y centrado el texto

        self.setCentralWidget(label)

        label.setText("Sistema iniciado")           #cambia el texto del Qlabel


app = QApplication()
window = Ventana()
window.show()
app.exec()