#Álvarez Romero Jose Antonio, 2 DAM

import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,

)
from PySide6.QtGui import QPainter, QColor, QPen, QPalette
from PySide6.QtCore import QRect, Qt, Signal

#Coge los estilos del qss
app = QApplication(sys.argv)
app.setStyle("Fusion")
with open("ExamenT3/Álvarez_JoseAntonio_estilos.qss", "r") as f:
    app.setStyleSheet(f.read())


class CirculoAlerta(QWidget):
    def __init__(self):
        super().__init__()

        self.__color= QColor("white")
        self.__texto = "OK"

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # --- circulo ---
        painter.setBrush(self.__color)
        painter.setPen(QColor("#000000"))

        #        --- tamaño ---
        diametro = self.width() * 0.38  #tamaño en funcion del ancho

        #        --- posicion ---
        x_circulo = (self.width()-diametro)//2
        y_circulo = (self.height()-diametro)//2
        circulo = QRect(x_circulo,y_circulo, diametro, diametro)

        #      --- pintar el circulo ---
        painter.drawEllipse(x_circulo,y_circulo, diametro, diametro)

        # --- texto ---
        painter.setPen(QPen(Qt.black))
        painter.drawText(circulo, Qt.AlignCenter, self.__texto)


        # --- funcion cambiar ---
    def cambiar_aviso(self, cantidad):
        if 1<=cantidad<=3:
            self.__color = QColor("#ffffff")
            self.update()

        elif 4<=cantidad<=7:
            self.__color = QColor("#ebd300")
            self.__texto = "AVISO"
            self.update()
        else:
            self.__color= QColor("#ff0000")
            self.__texto = "ERROR"
            self.update()
    
        # --- funcion reiniciar ---
    def reiniciar_circulo(self):
        self.__color = QColor("#ffffff")
        self.__texto = "OK"
        self.update()


class EtiquetaAviso(QLabel):
    def __init__(self, parent = None):
        super().__init__("Incidencias abiertas: 0", parent)

    #metodo para actualizar el contador, recibe la cantidad de la señal del boton
    def actualizar_contador(self, cantidad):
        
        #cambia el texto del QLabel
        self.setText("Incidencias abiertas: " + str(cantidad))
        

        #no he sabido cambiar el fondo, no se que QPalette. lo cambia.
        paleta = self.palette()
        if cantidad < 4:
            paleta.setColor(QPalette.WindowText, Qt.black)
        elif 4 <= cantidad < 8:
            paleta.setColor(QPalette.WindowText, QColor("#D39015"))
        elif 8 <= cantidad:
            paleta.setColor(QPalette.WindowText, QColor("#EC5656"))
        self.setPalette(paleta)


class BotonAñadir(QPushButton):
    boton_mas = Signal(int)
    def __init__(self, parent = None):
        
        super().__init__("Añadir incidencia", parent)
        self.__contador = 0
        #al hacer clic aumenta
        self.clicked.connect(self.__incrementar)

    def __incrementar(self):
        self.__contador = self.__contador+1
        self.boton_mas.emit(self.__contador)
        #funcion para reiniciar
    def reiniciar(self):
        self.__contador = 0
        



class Botonreset(QPushButton):
    boton_reset = Signal(int)
    def __init__(self, parent = None):
        super().__init__("Reset", parent)
        self.__cantidad=0
        self.clicked.connect(self.__limpiar)

    #metodo para cambiar el color del boton y emitir una señal de pulsado
    def __limpiar(self):
        self.boton_reset.emit(self.__cantidad)


class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Panel de incidencias")
        self.resize(400,400)
        self.setMinimumWidth(400)
        self.setMinimumHeight(400)
        
        #elementos
        contenedor = QWidget()
        layout = QVBoxLayout()
        self.circulo = CirculoAlerta()
        self.etiqueta = EtiquetaAviso()
        self.boton_aumentar = BotonAñadir()
        self.reset = Botonreset()

        self.etiqueta.setAutoFillBackground(True)

        #layout
        layout.addWidget(self.circulo)    
        layout.addWidget(self.etiqueta)   
        layout.addWidget(self.boton_aumentar)   
        layout.addWidget(self.reset)
        contenedor.setLayout(layout)

        self.setCentralWidget(contenedor)

        #conexiones
        self.boton_aumentar.boton_mas.connect(self.circulo.cambiar_aviso)
        self.boton_aumentar.boton_mas.connect(self.etiqueta.actualizar_contador)

        self.reset.boton_reset.connect(self.circulo.reiniciar_circulo)
        self.reset.boton_reset.connect(self.etiqueta.actualizar_contador)
        self.reset.boton_reset.connect(self.boton_aumentar.reiniciar)






ventana = VentanaPrincipal()
ventana.show()
app.exec()
