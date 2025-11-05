#Álvarez Romero, Jose Antonio 2DAM

from PySide6.QtWidgets import QApplication,QMainWindow,QLineEdit

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi ventana")

        texto = QLineEdit()                                 #crea el Qlineedit
        texto.setPlaceholderText("Escribe tu ciudad")       #definimos un placeholder
        texto.setMaxLength(20)                              #numero maximo de caracteres

        texto.returnPressed.connect(self.enter)             #conectamos al pulsar enter

        self.setCentralWidget(texto)
        self.texto = texto

    def enter(self):
        t = self.texto.text()                               #guardamos el texto actual
        if (t == ""):
            self.setWindowTitle("Sin ciudad")               #si esta vacio el texto es sin ciudad
        else:
            self.setWindowTitle(t)
        

app = QApplication()
window = Ventana()
window.show()
app.exec()