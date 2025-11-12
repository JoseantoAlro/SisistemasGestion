from PySide6.QtWidgets import (
    QMainWindow,QApplication,QWidget,QGridLayout,QPushButton
)

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Layout grid")

        layout_cuadricula = QGridLayout()
        
        componente_principal = QWidget()
        componente_principal.setLayout(layout_cuadricula)

        self.setCentralWidget(componente_principal)

        layout_cuadricula.addWidget(QPushButton("0,0"), 0,0)
        layout_cuadricula.addWidget(QPushButton("0,1"), 0,1)
        layout_cuadricula.addWidget(QPushButton("0,2"), 0,2)
        layout_cuadricula.addWidget(QPushButton("0,3"), 0,3)

        layout_cuadricula.addWidget(QPushButton("1,0-3"), 1, 0, 1, 4)  #fila 1 columna1 , ocupa 1 fila y ocupa 4 columnas
        layout_cuadricula.addWidget(QPushButton("2,0-1"), 2, 0, 1, 2)
        layout_cuadricula.addWidget(QPushButton("2,2-3"), 2, 2, 2, 2)

        layout_cuadricula.addWidget(QPushButton("0,3"), 3,0)

app = QApplication([])
ventana = Ventana()
# Mostramos la ventana
ventana.show()
app.exec()