from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox

class ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("combobox")

        combo = QComboBox()
        combo.addItems(["uno","dos","tres"])

        combo.currentIndexChanged.connect(self.cambio_indice)
        combo.currentTextChanged.connect(self.cambio_texto)

        combo.setEditable(True)                                                             #para poder añadir al desplegable
        combo.setInsertPolicy(QComboBox.InsertAlphabetically)
        combo.setMaxCount(5)

        self.setCentralWidget(combo)

    def cambio_indice(self, i):
        print("indice seleccionado", i)
    
    def cambio_texto(self, t):
        print("texto seleccionado", t)



app = QApplication([])
window = ventana()
window.show()
app.exec()