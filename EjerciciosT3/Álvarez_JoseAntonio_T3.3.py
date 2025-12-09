from PySide6.QtWidgets import(
    QApplication
    ,QMainWindow
    ,QVBoxLayout
    ,QWidget
    ,QPushButton
)
from PySide6.QtGui import QPainter, QColor, QPen
from PySide6.QtCore import QRect, Qt




class PanelSemaforo(QWidget):
    def __init__(self):
        self.__estado_actual = "rojo"
        super().__init__()

        #se define fuera del paintevent porque si no al hacer update se repinta por encima de rojo
        self.circulo1 = QColor("red")
        self.circulo2 = QColor("Gray")
        self.circulo3 = QColor("Gray")


    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        # --- SEMAFORO ---  
        painter.setBrush(QColor("darkGray"))

        alto = (self.height()//5)*4
        ancho = (alto//2)
        x=(self.width()-ancho)//2
        y=(self.height()//5)//2

        painter.drawRect(x, y, ancho, alto)


        # --- BOMBILLAS ---



        diametro = ancho * 0.6 #circulos al 60% del ancho del semaforo
        espacio = (alto - 3 * diametro) // 4 #para que no esten pegados los circulos

        EjeX = x + (ancho - diametro) // 2 #centrar dentro del semaforo

        EjeY1 = y + espacio
        EjeY2 = y + espacio * 2 + diametro     #eje y es el vertice y del semaforo mas el espacio entre circulos mas las bombillas anteriores
        EjeY3 = y + espacio * 3 + diametro * 2


        # --- BOMBILLA 1 ---
        painter.setBrush(self.circulo1)
        painter.setPen(Qt.black)
        painter.drawEllipse(EjeX, EjeY1, diametro, diametro)

        # --- BOMBILLA 2 ---
        painter.setBrush(self.circulo2)
        painter.setPen(Qt.black)
        painter.drawEllipse(EjeX, EjeY2, diametro, diametro)

        # --- BOMBILLA 3 ---
        painter.setBrush(self.circulo3)
        painter.setPen(Qt.black)
        painter.drawEllipse(EjeX, EjeY3, diametro, diametro)

    def cambiar_color(self):
        if self.__estado_actual == "rojo":
            self.circulo1 = QColor("Gray")
            self.circulo2 = QColor("Yellow")
            self.__estado_actual = "amarillo"
            self.update()
        elif self.__estado_actual == "amarillo":
            self.circulo2 = QColor("Gray")
            self.circulo3 = QColor("Green")
            self.__estado_actual = "Verde"
            self.update()
        else:
            self.circulo3 = QColor("Gray")
            self.circulo1 = QColor("Red")
            self.__estado_actual = "rojo"
            self.update()
            

       







class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Indicador con texto")
        self.resize(300,300)
        contenedor = QWidget()

        layout = QVBoxLayout()

        self.semaforo = PanelSemaforo()
        boton = QPushButton("Cambiar semaforo")
        boton.clicked.connect(self.cambiar_semaforo)

        layout.addWidget(self.semaforo)
        layout.addWidget(boton)

        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)

    def cambiar_semaforo(self):
        self.semaforo.cambiar_color()
        

app = QApplication([])
ventana = VentanaPrincipal()
ventana.show()
app.exec()
