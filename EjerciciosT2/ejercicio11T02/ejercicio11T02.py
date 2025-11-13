import os
from PySide6.QtWidgets import QApplication,QMainWindow, QToolBar 
from PySide6.QtGui import QAction,QKeySequence,QIcon,Qt



class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana de menu principal")

        menu_principal = self.menuBar()                             #creamos el menu archivo
        menu = menu_principal.addMenu("&Archivo")
        
        barra_herramientas = QToolBar("Barra principal")            #creamos las dos barras de herramientas
        barra_secundaria = QToolBar("Barra secundaria")
        self.addToolBar(barra_herramientas)
        self.addToolBar(Qt.BottomToolBarArea, barra_secundaria)     #la segunda la ponemos abajo


        ruta_icono1 = os.path.join(os.path.dirname(__file__), "printer.png")        #ruta de iconos
        ruta_icono2 = os.path.join(os.path.dirname(__file__), "refresh.png")
        ruta_icono3 = os.path.join(os.path.dirname(__file__), "no-connection.png")
        ruta_icono4 = os.path.join(os.path.dirname(__file__), "electricity.png")
        
        accion1 = QAction(QIcon(ruta_icono1), "Mostrar mensaje", self)              #creamos las acciones con su texto y su icono
        accion1.setShortcut(QKeySequence("Ctrl+M"))
        accion2 = QAction(QIcon(ruta_icono2),"Cambiar titulo", self)
        accion2.setShortcut(QKeySequence("Ctrl+L"))
        accion3 = QAction(QIcon(ruta_icono3),"Desactivar acciones", self)
        accion3.setShortcut(QKeySequence("Ctrl+Q"))
        accion4 = QAction(QIcon(ruta_icono4),"Activar acciones", self)
        accion4.setShortcut(QKeySequence("Ctrl+A"))



        accion1.triggered.connect(self.imprimir_por_consola)    #creamos un metodo por cada accion
        accion2.triggered.connect(self.cambiar_titulo)
        accion3.triggered.connect(self.desactivar)
        accion4.triggered.connect(self.activar)

        self.accion1 = accion1
        self.accion2 = accion2
        self.accion3 = accion3
        

        
        barra_herramientas.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)   #añadimos texto debajo de los iconos
        
        

        barra_herramientas.addActions((accion1,accion2,accion3))            #asignamos las acciones a cada menu o barra
        barra_secundaria.addAction(accion4)
        menu.addActions((accion1,accion2,accion3))



    def imprimir_por_consola(self):                             #definimos los metodos
        print("Hola")
    def cambiar_titulo(self):
        self.setWindowTitle("Titulo cambiado")
    def desactivar(self):
        self.accion1.setEnabled(False)
        self.accion2.setEnabled(False)
        self.accion3.setEnabled(False)
    def activar(self):
        self.accion1.setEnabled(True)
        self.accion2.setEnabled(True)
        self.accion3.setEnabled(True)




app = QApplication()
app.setAttribute(Qt.AA_DontShowIconsInMenus)                #eliminamos iconos en el menu
window = Ventana()
window.show()
app.exec()

