#Álvarez Romero, Jose Antonio

from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget, QLabel

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pestañas con contenido")                   
        opcion1 = QLabel("Bienvenido")     #el interior de las pestañas debe ser un widget
        opcion2 = QLabel("Segunda pestaña")
        opcion3 = QLabel("Tercera pestaña")

        pest = QTabWidget()                                 #creacion del tabwidget
        pest.addTab(opcion1,"opcion 1")                     #adicion de pestañas
        pest.addTab(opcion2,"opcion 2")
        pest.addTab(opcion3,"opcion 3")

        pest.currentChanged.connect(self.cambio_pestaña)    #conectar cada vez que se cambia de pestaña

        self.setCentralWidget(pest)

    def cambio_pestaña(self, i):                        
        self.setWindowTitle("Pestaña " +  str(i+1))         #str(i+1) ya que el indice comienza en 0 y no 
        print("Indice seleccionado:" + str(i+1))            #se puede concatenar str con int

app=QApplication()
window=Ventana()
window.show()
app.exec()