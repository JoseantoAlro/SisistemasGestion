from PySide6.QtWidgets import (
    QMainWindow,QApplication,QWidget,QHBoxLayout,QPushButton
)

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Layout horizontal")

        layout_vertical = QHBoxLayout()

        componente_principal = QWidget()
        componente_principal.setLayout(layout_vertical)

        self.setCentralWidget(componente_principal)

        layout_vertical.addWidget(QPushButton("uno"))
        layout_vertical.addWidget(QPushButton("dos"))
        layout_vertical.addWidget(QPushButton("tres"))
        layout_vertical.addWidget(QPushButton("cuatro"))


app = QApplication([])
ventana = Ventana()
# Mostramos la ventana
ventana.show()
app.exec()