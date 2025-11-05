#Álvarez Romero, Jose Antonio 2DAM

from PySide6.QtWidgets import QApplication,QMainWindow,QComboBox

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("App ComboBox")

        combo = QComboBox()                                    #creamos el combobox
        combo.addItems(["Python", "Java", "C++", "Kotlin"])    #le añadimos los elementos
        combo.setInsertPolicy(QComboBox.InsertAfterCurrent)    #si se añade uno será despues del actual

        combo.setEditable(True)                                #que sea editable el texto
        combo.setMaxCount(6)                                   #maximo numero de opciones

        combo.lineEdit().returnPressed.connect(self.cambio_texto)          #conecta al presionar enter
        combo.currentIndexChanged.connect(self.cambio_texto)               #conecta al cambiar de opcion

        self.combo = combo
        self.setCentralWidget(self.combo)

    def cambio_texto(self):
        t = self.combo.currentText()            #guarda el texto actual de la opcion
        print("Elemento seleccionado:", t)      
        self.setWindowTitle(t)



app = QApplication()
window = Ventana()
window.show()
app.exec()