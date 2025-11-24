import os
import platform
from PySide6.QtWidgets import QApplication,QMainWindow, QToolBar, QLabel
from PySide6.QtGui import QAction,QKeySequence,QIcon


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana de barra de herramientas y barra de estado principal")

        barra_menu = self.menuBar()

        menu = barra_menu.addMenu("&Menú")   #con & surralla la letra m y se puede acceder por teclado con alt m

        #######

        #ruta icono
        ruta_icono = os.path.join(os.path.dirname(__file__), "printer.png")
        #acion con icono texto y descripcion

        
        accion = QAction(QIcon(ruta_icono),"imprimir por consola", self)
        accion.setShortcut(QKeySequence("Ctrl+P"))
        accion.setWhatsThis("imprime un texto por consola al pulsar el botón o atajo")
        accion.triggered.connect(self.imprimir_por_consola)
        menu.addAction(accion)
        

        barra_herramientas = QToolBar("Barra principal")
        barra_herramientas.addAction(accion)
        self.addToolBar(barra_herramientas)
        ########
        
        ######barra estado
        barra_estado = self.statusBar()

        barra_estado.addPermanentWidget(QLabel(platform.system()))

        barra_estado.showMessage("listo esperando", 3000)





    def imprimir_por_consola(self):
        print(("Accion lanzada desde el menu o mediante el atajo de teclado"))


app = QApplication()
window = Ventana()
window.show()
app.exec()

