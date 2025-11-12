#Álvarez Romero, Jose Antonio 2DAM

from PySide6.QtWidgets import QApplication,QMainWindow,QTextEdit

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Qtextedit")

        texto = QTextEdit()                                         #crea el textedit
        texto.setPlainText("Bienvenido/a al editor de texto.")      #escribe un texto inicial
        texto.setPlaceholderText("Escribe aquí tu mensaje...")      #crea un texto de ayuda cuando esta vacio

        texto.textChanged.connect(self.cambio_texto)                #llama a la funcion cada vez que se varia el texto

        self.setCentralWidget(texto)
        self.texto = texto

    def cambio_texto(self):                                         #muestra por consola
        text = self.texto.toPlainText()
        print(text)



app = QApplication([])
ventana = Ventana()
# Mostramos la ventana
ventana.show()
app.exec()
