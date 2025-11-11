#Álvarez Romero, Jose Antonio

from PySide6.QtWidgets import QApplication, QMainWindow, QDateTimeEdit
from PySide6.QtCore import QDateTime


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calendario") 
        date = QDateTimeEdit()
        date.setDateTime(QDateTime.currentDateTime())                   #crea un qdateTimeEdit y con valor inicial la fecha de hoy
        date.setDisplayFormat("dddd, d 'de' MMMM 'de' yyyy hh:mm")
        date.dateTimeChanged.connect(self.cambio_fecha)

        self.date = date
        self.setCentralWidget(date)


    def cambio_fecha(self):                             #si cambia la fecha u hora miestra por pantalla la fecha nueva.
        fecha = self.date.dateTime()
        print("Fecha elegida: " + fecha.toString("dddd, d 'de' MMMM 'de' yyyy hh:mm"))

app = QApplication()
window = Ventana()
window.show()
app.exec()