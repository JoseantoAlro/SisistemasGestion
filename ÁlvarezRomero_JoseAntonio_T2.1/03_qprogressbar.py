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
        timer.start(2000)           #se ejecuta cada 2 segundos.
        self.timer = timer
        

        self.setCentralWidget(barra)

    def preguntar_usuario(self):                #funcion que muestra las opciones y recibe una de ellas.
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

    def cambiar_progreso(self , p):                                                     #funcion para cambiar el progreso
        if p == "aumentar":
            
            if self.progreso_actual == 80:                                              #si es 80 y aumenta llega a 100 y cambia a un titulo especial
                self.progreso_actual = self.progreso_actual + 20
                self.setWindowTitle("Tarea Completada")   
            elif self.progreso_actual !=80 and self.progreso_actual !=100:              #si no es 80 o 100 aumenta en 20 y si es 100 no hace nada.
                self.progreso_actual = self.progreso_actual + 20
                self.setWindowTitle("Progreso actual: "+ str(self.progreso_actual)+"%")
        else:
            if self.progreso_actual != 0:                                               #mientras no sea cero reduce en 20.
                self.progreso_actual = self.progreso_actual - 20
            self.setWindowTitle("Progreso actual: "+ str(self.progreso_actual)+"%")

        self.barra.setValue(self.progreso_actual)

        print("Progreso: "+str(self.progreso_actual)+"%")


app=QApplication()
window=Ventana()
window.show()
app.exec()