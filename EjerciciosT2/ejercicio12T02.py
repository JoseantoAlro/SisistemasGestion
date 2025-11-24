#Álvarez Romero Jose Antonio

import os
import getpass

from PySide6.QtWidgets import QApplication,QMainWindow, QToolBar, QLabel
from PySide6.QtGui import QAction,QKeySequence,QIcon
from PySide6.QtCore import QTimer


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana de barra de herramientas y barra de estado principal")


        barra_menu = self.menuBar()                 #creamos el menu 
        menu = barra_menu.addMenu("&Archivo") 

        ruta_icono = os.path.join(os.path.dirname(__file__), "printer.png")     #ruta de icono

        accion1 = QAction(QIcon(ruta_icono),"mostrar mensaje temporal", self)           #creamos las acciones del menu y de la barra de herramientas
        accion1.setShortcut(QKeySequence("Ctrl+T"))
        accion1.triggered.connect(self.mostrar_mensaje)
        accion2 = QAction(QIcon(ruta_icono),"limpiar mensaje", self)
        accion2.setShortcut(QKeySequence("Ctrl+L"))
        accion2.triggered.connect(self.limpiar_mensaje)
        accion3 = QAction(QIcon(ruta_icono),"mostrar información del sistema", self)
        accion3.setShortcut(QKeySequence("Ctrl+I"))
        accion3.triggered.connect(self.mostrar_info)


        
        barra_herramientas = QToolBar("Barra principal")                #creamos la barra de herramientas
        self.addToolBar(barra_herramientas)
        
        

        barra_estado = self.statusBar()                             #iniciamos la barra con un mensaje
        barra_estado.showMessage("Aplicación iniciada correctamente", 2000)
        self.barra_estado = barra_estado


        self.valor=1
        self.timer1 = QTimer()                              #creamos un timer que haga una llamada a una funcion cada 3 segundos
        self.timer1.timeout.connect(self.cambiar_mensaje)
        self.timer1.start(3000)

        

        barra_herramientas.addActions((accion1,accion2,accion3))        #enlacamos las acciones al menu y barra
        menu.addActions((accion1,accion2,accion3))

        
    def mostrar_mensaje(self):
        self.barra_estado.showMessage("Mensaje temporal: desaparece en 3 segundos",3000)

    def limpiar_mensaje(self):
        self.barra_estado.clearMessage()  

    def mostrar_info(self):
        self.barra_estado.addPermanentWidget(QLabel(getpass.getuser()))  

    def cambiar_mensaje(self):          #cambia el mensaje de la barra de progreso en funcion de un valor auxiliar
        if self.valor==1:
            self.barra_estado.showMessage("Esperando acción…")
            self.valor=0
        else:
            self.barra_estado.showMessage("Listo para trabajar")
            self.valor=1
   
        
        
    



app = QApplication()
window = Ventana()
window.show()
app.exec()
