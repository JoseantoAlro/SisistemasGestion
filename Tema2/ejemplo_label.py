from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import Qt

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("mi app")

        etiqueta = QLabel("Hola")
        fuente = etiqueta.font()
        fuente.setPointSize(30)

        etiqueta.setFont(fuente)

        etiqueta.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)        ##pa centrar

        self.setCentralWidget(etiqueta)

app = QApplication()    
window = Ventana()
window.show()
app.exec()