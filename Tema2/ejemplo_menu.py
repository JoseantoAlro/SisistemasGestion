from PySide6.QtWidgets import QApplication,QMainWindow
from PySide6.QtGui import QAction,QKeySequence


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana de menu principal")

        barra_menu = self.menuBar()

        menu = barra_menu.addMenu("&Menú")   #con & surralla la letra m y se puede acceder por teclado con alt m


        accion = QAction("imprimir por consola", self)
        accion.setShortcut(QKeySequence("Ctrl+P"))
        accion.triggered.connect(self.imprimir_por_consola)

        menu.addAction(accion)

    def imprimir_por_consola(self):
        print(("Accion lanzada desde el menu o mediante el atajo de teclado"))


app = QApplication()
window = Ventana()
window.show()
app.exec()


