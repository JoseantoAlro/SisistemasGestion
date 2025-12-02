from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton
)
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplo de QSS")
        # --- Widgets ---
        self.label = QLabel("Introduce tu nombre:")
        self.input_nombre = QLineEdit()
        self.boton_aceptar = QPushButton("Aceptar")
        self.boton_cancelar = QPushButton("Cancelar")
        # --- Layout ---
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input_nombre)
        layout.addWidget(self.boton_aceptar)
        layout.addWidget(self.boton_cancelar)

        contenedor = QWidget()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)

        # --- estilos ---
        estilos = """
        QMainWindow{
            background-color: #f5f5f5;
        }

        QLabel{
            font-size: 16px;
            color: #2c3e50;
        }

        QLineedit{
            background-color: white;
            border: 2px solid #2494db;
            border-radius: 5px;
            padding: 10px;
            font-size:14px;
        }

        QPushButton{
            background-color: #3494db;
            color: white;
            border: none;
            border-radius: 10px;
            padding: 10px;
            font-size:14px;
        }

        QPushButton:hover{
            background-color: #2980b9;
        }

        QPushButton:pressed{
            background-color: #1f5f8b;
        }
        """

        self.setStyleSheet(estilos)


app = QApplication([])
app.setStyle("Fusion")
ventana = MainWindow()
ventana.show()
app.exec()
