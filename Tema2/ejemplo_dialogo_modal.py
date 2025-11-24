from PySide6.QtWidgets import QApplication,QMainWindow, QDialog, QPushButton

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana de dialog")

        boton =QPushButton("boton")
        boton.clicked.connect(self.mostrar_dialog)
        self.setCentralWidget(boton)

    def mostrar_dialog(self):
        print("cositas por consola")  
        dialogo= QDialog(self)
        dialogo.setWindowTitle("Ventana de dialogo")
        dialogo.exec()

app =QApplication()
window=Ventana()
window.show()
app.exec()  
