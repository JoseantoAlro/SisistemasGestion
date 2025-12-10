from PySide6.QtWidgets import(
    QApplication
    ,QMainWindow
    ,QVBoxLayout
    ,QWidget
    
)
from PySide6.QtGui import QPainter, QColor, QPen
from PySide6.QtCore import QRect, Qt, QTimer




class PanelSemaforo(QWidget):
    def __init__(self):
        self.__estado_actual = "rojo"
        super().__init__()

        #se define fuera del paintevent porque si no al hacer update se repinta por encima de rojo
        self.circulo1 = QColor("red")
        self.circulo2 = QColor("Gray")
        self.circulo3 = QColor("Gray")

        #pintar el semaforo
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        # --- SEMAFORO ---  
        painter.setBrush(QColor("darkGray"))
                #Tamaño y posicion
        alto = (self.height()//5)*4
        ancho = (alto//2)
        x=(self.width()-ancho)//2
        y=(self.height()/-alto)//2
                #dibujarlo
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

    def cambiar_color(self):  #segun el estado actual cambia el color de la bombilla encendida a gris y enciende la siguiente
        if self.__estado_actual == "rojo":
            self.circulo1 = QColor("Gray")
            self.circulo2 = QColor("Yellow")
            self.__estado_actual = "amarillo"
            self.update()
        elif self.__estado_actual == "amarillo":
            self.circulo2 = QColor("Gray")
            self.circulo3 = QColor("Green")
            self.__estado_actual = "verde"
            self.update()
        else:
            self.circulo3 = QColor("Gray")
            self.circulo1 = QColor("Red")
            self.__estado_actual = "rojo"
            self.update()

    def estado(self): #devuelve el estado actual
        return self.__estado_actual       

       







class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Semaforo con temporizador")
        self.resize(300,300)

        #elementos
        contenedor = QWidget()
        layout = QVBoxLayout()
        self.semaforo = PanelSemaforo()

        
        #layouts
        layout.addWidget(self.semaforo)
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)

        self.temporizador = QTimer(self)
        self.temporizador.timeout.connect(self.cambiar_semaforo)
        self.temporizador.setInterval(1000)
        self.temporizador.start()


        
    #funcion de los botones
    def cambiar_semaforo(self):
        self.semaforo.cambiar_color()
        print("Estado actual del semaforo: "+self.semaforo.estado())

        

app = QApplication([])
ventana = VentanaPrincipal()
ventana.show()
app.exec()
