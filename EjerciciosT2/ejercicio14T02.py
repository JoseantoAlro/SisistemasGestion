#Álvarez Romero Jose Antonio



from PySide6.QtWidgets import QApplication,QMainWindow, QPushButton, QLabel, QDialog,QDialogButtonBox, QVBoxLayout

class DialogoPersonal(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana modal")

        self.boton_pulsado = None           #declaramos el botons pulsado del dialogo

        botones = QDialogButtonBox.Yes | QDialogButtonBox.No | QDialogButtonBox.Help    #definimos botones y el contenedor
        caja = QDialogButtonBox(botones)

        botonSi = caja.button(QDialogButtonBox.Yes)
        botonNo = caja.button(QDialogButtonBox.No)

        
        botonSi.clicked.connect(self.pulsar_si)     #revisar
        botonNo.clicked.connect(self.pulsar_no)
        caja.helpRequested.connect(self.reject)
        

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Selecciona el modo de operación que quieres activar:"))
        layout.addWidget(caja)
        self.setLayout(layout)

    def pulsar_si(self):
        self.boton_pulsado = 1
        self.accept()

    def pulsar_no(self):
        self.boton_pulsado = 0
        self.accept()


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Selección de modo de operación")

        boton = QPushButton("Elegir modo")
        boton.clicked.connect(self.abrir_dialog)
        self.setCentralWidget(boton)

    def abrir_dialog(self):
        dialogo = DialogoPersonal()
        resultado = dialogo.exec()

        if resultado == QDialog.Accepted:
            if dialogo.boton_pulsado == 1:
                print("Modo A activado")
            elif dialogo.boton_pulsado == 0:
                print("Modo B activado")
        else:
            print("Se ha solicitado ayuda")

app =QApplication()
window=Ventana()
window.show()
app.exec()  