from PySide6.QtWidgets import (
    QMainWindow,QApplication,QWidget,QFormLayout,QPushButton,
    QLabel,QLineEdit,QSpinBox,QDoubleSpinBox
)

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Formulario")

        layout_formulario = QFormLayout()

        componente_principal = QWidget()
        componente_principal.setLayout(layout_formulario)

        self.setCentralWidget(componente_principal)

        layout_formulario.addRow(QLabel("Texto: "), QLineEdit())
        layout_formulario.addRow(QLabel("entero: "), QSpinBox())
        layout_formulario.addRow(QLabel("decimal: "), QDoubleSpinBox())
        layout_formulario.addRow(QPushButton("enviar"))  #es decorativo no envia
        


app = QApplication([])
ventana = Ventana()
# Mostramos la ventana
ventana.show()
app.exec()