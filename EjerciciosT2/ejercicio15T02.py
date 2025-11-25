#Álvarez Romero. Jose Antonio


from PySide6.QtWidgets import QApplication,QMainWindow, QPushButton, QDialog, QMessageBox


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QMessageBox")

        boton = QPushButton("Gestionar tarea")      
        boton.clicked.connect(self.mostrar_dialogo) #boton con el dialogo

        self.setCentralWidget(boton)

    def mostrar_dialogo(self):                      #definimos la ventana que abre el boton
        boton_pulsado = QMessageBox.critical(
            self,
            "Acción sobre la tarea",
            "¿Qué quieres hacer con la tarea seleccionada?",
            buttons=QMessageBox.Yes | QMessageBox.No | QMessageBox.Ignore,      #tiene tres botones
            defaultButton=QMessageBox.Ignore
        )
        if boton_pulsado == QMessageBox.Yes:            #segun el boton pulsado enseña un mensaje informativo u otro
             QMessageBox.information(
                self, "Mensaje de información","La tarea se ha marcado como completada.")
        elif boton_pulsado == QMessageBox.No:
             QMessageBox.information(
                self, "Mensaje de información","La tarea se ha pospuesto para más tarde.")
        else:
             QMessageBox.information(
                self, "Mensaje de información","La tarea se mantiene sin cambios.")



app=QApplication()
window=Ventana()
window.show()
app.exec()