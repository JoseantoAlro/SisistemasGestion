from PySide6.QtWidgets import(
    QApplication
    ,QMainWindow
    ,QVBoxLayout
    ,QWidget
    ,QPushButton
)
from PySide6.QtGui import QPainter, QColor, QPen
from PySide6.QtCore import QRect, Qt

class IndicadorSimple(QWidget):
    def __init__(self):
        super().__init__()

        self.__texto = "ok"

    def setTexto(self, texto):
        self.__texto = texto
        self.update()

    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(QPainter.Antialiasing) #lineas mas bonitas

        painter.setBrush(QColor("#4CAF50"))

        painter.setPen(QPen(Qt.black))

        lado = min(self.width(), self.height())

        recto = QRect((self.width() - lado) // 2        # la // es para una division sin decimales
        ,(self.height() - lado)//2
        ,lado
        ,lado)  

        painter.drawEllipse(recto)

        painter.setPen(QPen(Qt.white))

        painter.drawText(recto, Qt.AlignCenter, self.__texto)

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Indicador con texto")
        self.resize(300,300)
        contenedor = QWidget()

        layout = QVBoxLayout()

        self.indicador = IndicadorSimple()
        boton = QPushButton("Cambiar Texto")
        boton.clicked.connect(self.cambiar_texto)

        layout.addWidget(self.indicador)
        layout.addWidget(boton)
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)

    def cambiar_texto(self):
        self.indicador.setTexto("Ready")
        

app = QApplication([])
ventana = VentanaPrincipal()
ventana.show()
app.exec()
