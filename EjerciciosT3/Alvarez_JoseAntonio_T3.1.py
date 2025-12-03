import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel,
    QCheckBox,
    QLineEdit,
    QPushButton,
    QRadioButton,
    QComboBox
)

app = QApplication(sys.argv)
app.setStyle("Fusion")
with open("EjerciciosT3/Alvarez_JoseAntonio_T3.1.qss", "r") as f:
    app.setStyleSheet(f.read())

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplo de QSS")
        # --- Widgets ---
        self.t1 = QLabel("checkbox:")
        self.check = QCheckBox("Checkbox")
        self.t2 = QLabel("Boton:")
        self.boton = QPushButton("Aceptar")
        self.t3 = QLabel("ingresar texto:")
        self.input_nombre = QLineEdit()
        self.t4 = QLabel("Boton de radio:")
        self.boton_radio = QRadioButton("Aceptar")
        self.t5 = QLabel("ComboBox")
        self.combo = QComboBox()
        self.combo.addItems(["Muy mala","Mala","Media","Buena", "Muy buena"])
        # --- Layout ---

        layout = QVBoxLayout()
        layout.addWidget(self.t1)
        layout.addWidget(self.check)
        layout.addWidget(self.t3)
        layout.addWidget(self.input_nombre)
        layout.addWidget(self.t2)
        layout.addWidget(self.boton)
        layout.addWidget(self.t4)
        layout.addWidget(self.boton_radio)
        layout.addWidget(self.t5)
        layout.addWidget(self.combo)

        contenedor = QWidget()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)

ventana = MainWindow()
ventana.show()
app.exec()