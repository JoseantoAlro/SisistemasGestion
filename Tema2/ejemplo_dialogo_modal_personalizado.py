from PySide6.QtWidgets import QApplication,QMainWindow, QDialog, QPushButton, QVBoxLayout, QLabel,QDialogButtonBox
from PySide6.QtCore import QTranslator, QLibraryInfo



class DialogPers(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Dialog personalizado")
        
        botones = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        caja = QDialogButtonBox(botones)

        caja.accepted.connect(self.accept)
        caja.rejected.connect(self.reject)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("¿Quiere realizar esta accion?"))
        layout.addWidget(caja)

        self.setLayout(layout)







class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana de dialog")

        boton =QPushButton("boton")
        boton.clicked.connect(self.mostrar_dialog)
        self.setCentralWidget(boton)

    def mostrar_dialog(self):
        print("cositas por consola")  
        dialogo= DialogPers(self)
        dialogo.setWindowTitle("Ventana de dialogo")
        resultado = dialogo.exec()

        if resultado:
            print("Aceptado") 
        else:
            print("cancelado")

def cargar_traductor(self):
    traductor = QTranslator(app)
    ruta = QLibraryInfo.location(QLibraryInfo.TranslationsPath)
    traductor.load("qt_es", ruta)
    app.installTranslator(traductor)


app =QApplication()
cargar_traductor(app)
window=Ventana()
window.show()
app.exec()  
