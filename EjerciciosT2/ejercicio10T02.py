#Álvarez Romero, Jose Antonio 2DAM

from PySide6.QtWidgets import QApplication,QMainWindow
from PySide6.QtGui import QAction,QKeySequence


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana de menu principal")

        barra_menu = self.menuBar()                             #creamos la barra archivo
        menu = barra_menu.addMenu("&Archivo")

        accion1 = QAction("Mostrar mensaje", self)              #creamos las acciones
        accion1.setShortcut(QKeySequence("Ctrl+M"))
        accion2 = QAction("Cambiar titulo", self)
        accion2.setShortcut(QKeySequence("Ctrl+L"))
        accion3 = QAction("Salir", self)
        accion3.setShortcut(QKeySequence("Ctrl+Q"))

        accion1.triggered.connect(self.imprimir_por_consola)    #creamos un metodo por cada accion
        accion2.triggered.connect(self.cambiar_titulo)
        accion3.triggered.connect(self.salir)

        menu.addAction(accion1)                                 #añadimos la accion al menu junto a un separador
        menu.addSeparator()
        menu.addAction(accion2)
        menu.addSeparator()
        menu.addAction(accion3)


    def imprimir_por_consola(self):                             #definimos los metodos
        print("Hola desde el menú")
    def cambiar_titulo(self):
        self.setWindowTitle("Titulo cambiado desde el menu")
    def salir(self):
        self.close()

app = QApplication()
window = Ventana()
window.show()
app.exec()