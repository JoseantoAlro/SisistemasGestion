from PySide6.QtWidgets import(
    QApplication
    ,QMainWindow
    ,QVBoxLayout
    ,QWidget
)
from PySide6.QtGui import QPainter, QColor, QPen
from PySide6.QtCore import Qt

class CirculoRojo(QWidget):
    def paintEvent(self, event):

        painter = QPainter(self)
        painter.setBrush(QColor("red"))
        painter.setPen(QPen(Qt.black))

        painter.drawEllipse(self.rect())

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Circulo Rojo")
        self.resize(300,300)

        self.setCentralWidget(CirculoRojo())

app = QApplication([])
ventana = VentanaPrincipal()
ventana.show()
app.exec()
