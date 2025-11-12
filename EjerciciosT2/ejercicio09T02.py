from PySide6.QtWidgets import (
    QMainWindow,QApplication,QWidget,QPushButton, QVBoxLayout, QHBoxLayout
)


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LayoutAnidados")

        layout_principal = QHBoxLayout()                        #creamos el layout principal

        layout_1 = QVBoxLayout()                                #creamos los secundarios
        layout_2 = QHBoxLayout()

        componente_principal = QWidget()                        #añadimos el layoutprincipal al widget principal
        componente_principal.setLayout(layout_principal)

        layout_1.addWidget(QPushButton("V1"))                   #añadimos los botones a los layout secundarios
        layout_1.addWidget(QPushButton("V2"))
        layout_1.addWidget(QPushButton("V3"))
        layout_1.addWidget(QPushButton("V4"))

        layout_2.addWidget(QPushButton("H1"))
        layout_2.addWidget(QPushButton("H2"))
        layout_2.addWidget(QPushButton("H3"))
        layout_2.addWidget(QPushButton("H4"))

        layout_principal.addLayout(layout_1)                    #añadimos los layouts secundarios al layout principal
        layout_principal.addLayout(layout_2)

        self.setCentralWidget(componente_principal)             


app = QApplication([])
ventana = Ventana()
ventana.show()
app.exec()        
