from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit




class VentanaPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicacion")

        texto = QLineEdit()
        texto.setMaxLength(10)
        texto.setPlaceholderText("escribe aqui")

        texto.returnPressed.connect(self.mostrar_mensaje)
        texto.textChanged.connect(self.texto_modificado)        #usuario o maquina
        texto.textEdited.connect(self.texto_editado)            #solo usuario

        self.setCentralWidget(texto)

        self.texto = texto
    
    def mostrar_mensaje(self):
        print("se pulso enter")
        self.texto.setText("hola")

    def texto_modificado(self,s):
        print("Texto modificado: ", s)

    def texto_editado(self,s):
        print("Texto editado por el usuario: ",s)

app=QApplication()
window=VentanaPrincipal()
window.show()
app.exec()