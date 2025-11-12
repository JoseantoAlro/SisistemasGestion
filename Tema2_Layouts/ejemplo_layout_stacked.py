from PySide6.QtWidgets import (
    QMainWindow,QApplication,QWidget,QStackedLayout,QPushButton,QLabel, QVBoxLayout, QHBoxLayout
)


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("appilado")

        layout_principal = QHBoxLayout()

        componente_principal = QWidget()
        componente_principal.setLayout(layout_principal)

        self.setCentralWidget(componente_principal)


        self.capas = QStackedLayout()

        self.capas.addWidget(QLabel("Capa 1"))
        self.capas.addWidget(QLabel("Capa 2"))
        self.capas.addWidget(QLabel("Capa 3"))

        layout_botones = QVBoxLayout()
        boton1 = QPushButton("Ver capa 1")
        boton2 = QPushButton("Ver capa 2")
        boton3 = QPushButton("Ver capa 3")
        layout_botones.addWidget(boton1)
        layout_botones.addWidget(boton2)
        layout_botones.addWidget(boton3)

        boton1.clicked.connect(self.cambio_capa1)
        boton2.clicked.connect(self.cambio_capa2)
        boton3.clicked.connect(self.cambio_capa3)
        layout_principal.addLayout(self.capas)
        layout_principal.addLayout(layout_botones)


    def cambio_capa1(self):
        self.capas.setCurrentIndex(0)
    def cambio_capa2(self):
        self.capas.setCurrentIndex(1)
    def cambio_capa3(self):
        self.capas.setCurrentIndex(2)

app = QApplication([])
ventana = Ventana()
# Mostramos la ventana
ventana.show()
app.exec()