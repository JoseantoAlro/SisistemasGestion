#Álvarez Romero, Jose Antonio 2DAM

from PySide6.QtWidgets import QApplication,QMainWindow,QCheckBox
from PySide6.QtCore import Qt

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__() 
        self.setWindowTitle("Preferencias de usuario")

        checkbox = QCheckBox("Checkbox a marchar")          #inicialmente sin marcar

        #checkbox.setCheckState(Qt.Checked)                 #para inicializar con el checkbox ya marcado

        #checkbox.setTristate(True)                         #para que este la opcion parcial
        #checkbox.setCheckState(Qt.PartiallyChecked)        #para que se inicie con la opcion parcial marcada

        checkbox.stateChanged.connect(self.mostrar_estado)  #conecta el checkbox con la funcion

        self.setCentralWidget(checkbox)                     #centra el checkbox

    def mostrar_estado(self, estado):                       #funcion que devueve como esta el checkbox por consola
        s = Qt.CheckState(estado)        
        if(s == Qt.CheckState.Checked):
            print("Marcado")
        if(s == Qt.CheckState.Unchecked):
            print("Desmarcado")
        if(s == Qt.CheckState.PartiallyChecked):
            print("Parcialmente marcado")

app = QApplication()
window = Ventana()
window.show()
app.exec()
        