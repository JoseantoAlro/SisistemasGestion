#Álvarez Romero, Jose Antonio

from PySide6.QtWidgets import QApplication, QMainWindow, QProgressBar
from PySide6.QtCore import QTimer

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Progreso manual") 
        self.progreso_actual = 0

        barra = QProgressBar()      #Valores por defecto de 0 a 100
        self.barra = barra
        
        timer = QTimer(self)
        timer.timeout.connect(self.preguntar_usuario)
        timer.start(2000)
        self.timer = timer
        

        self.setCentralWidget(barra)

    def preguntar_usuario(self):
        print("""=== Control de progreso ===
1 → Aumentar progreso
2 → Retroceder progreso
0 → salir""")
        opcion = int(input(""))
        if opcion == 1:
            self.cambiar_progreso("aumentar")
        elif opcion == 2:
            self. cambiar_progreso("disminuir")
        elif opcion == 0:
            self.timer.stop()
            self.close()
        else:
            opcion = input("Numero no valido. Introduzca otro ")

    def cambiar_progreso(self , p):
        if p == "aumentar":
            
            if self.progreso_actual == 80:
                self.progreso_actual = self.progreso_actual + 20
                self.setWindowTitle("Tarea Completada")   
            elif self.progreso_actual !=80 and self.progreso_actual !=100:
                self.progreso_actual = self.progreso_actual + 20
                self.setWindowTitle("Progreso actual: "+ str(self.progreso_actual)+"%")
        else:
            if self.progreso_actual != 0:
                self.progreso_actual = self.progreso_actual - 20
            self.setWindowTitle("Progreso actual: "+ str(self.progreso_actual)+"%")

        self.barra.setValue(self.progreso_actual)

        print("Progreso: "+str(self.progreso_actual)+"%")


app=QApplication()
window=Ventana()
window.show()
app.exec()