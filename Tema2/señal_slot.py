from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("mi Aplicacion")

        boton = QPushButton("pulsame")  
        boton.setCheckable(True)         ##hace el boton un interruptor

        boton.clicked.connect(self.el_boton_fue_pulsado)

        boton.clicked.connect(self.el_boton_esta_on)

        self.setCentralWidget(boton)

    
    def el_boton_fue_pulsado(self):
        print("Pulsado!")

    def el_boton_esta_on(self, checkeado):
        print("Esta on?", checkeado)

    


app=QApplication()
window=Ventana()
window.show()

app.exec()