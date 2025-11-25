#Álvarez Romero. Jose Antonio


from PySide6.QtWidgets import QApplication,QMainWindow, QPushButton, QLabel
from PySide6.QtGui import QAction,QKeySequence,QIcon
from PySide6.QtCore import Qt

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Selección de modo de operación")