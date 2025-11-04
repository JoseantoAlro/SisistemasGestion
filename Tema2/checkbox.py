from PySide6.QtWidgets import QApplication,QMainWindow,QCheckBox
from PySide6.QtCore import Qt


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("mi app")

        widget = QCheckBox("esto es un checkbox")
        widget.setCheckState(Qt.Checked)

        widget.stateChanged.connect(self.show_state)

        self.setCentralWidget(widget)

    def show_state(slef, s):                    #s es la señal que emite el widget
        state = Qt.CheckState(s)
        print(state == Qt.CheckState.Checked)       #si esta pulsado o no
        print(s)                                       #enseña un entero
        print(state)                                #enseña el estado





app = QApplication()
window = Ventana()
window.show()
app.exec()
