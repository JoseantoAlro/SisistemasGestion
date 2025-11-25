#Álvarez Romero Jose Antonio



from PySide6.QtWidgets import QApplication,QMainWindow,QToolBar, QDockWidget, QLabel, QTextEdit
from PySide6.QtGui import QAction,QKeySequence,QIcon
from PySide6.QtCore import Qt


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejercicio - Componentes flotantes")

        self.setCentralWidget(QLabel("Área principal de la aplicación"))

        panel1 = QDockWidget("componente TextEdit", self)               #creamos los paneles con el nombre, el widget interno y las caracteristicas
        panel1.setWidget(QTextEdit("Panel de notas"))
        panel1.setFeatures(QDockWidget.NoDockWidgetFeatures)

        panel2 = QDockWidget("Coponente 2", self)
        panel2.setWidget(QLabel("panel de estado"))
        panel2.setFeatures(QDockWidget.DockWidgetFloatable)

        panel3 = QDockWidget("componenete 3", self)
        panel3.setWidget(QLabel("Panel de ayuda"))
        panel3.setFeatures(QDockWidget.DockWidgetClosable | QDockWidget.DockWidgetFloatable)

        self.addDockWidget(Qt.LeftDockWidgetArea, panel1)               #añadimos los paneles a la ventana
        self.addDockWidget(Qt.RightDockWidgetArea, panel2)
        self.addDockWidget(Qt.BottomDockWidgetArea, panel3)

        barra_estado = self.statusBar()                                 #iniciamos la barra de estado con un mensaje
        barra_estado.showMessage("Listo. Paneles creados correctamente.")

        barra_herramientas = QToolBar("Barra principal")                #creamos la barra de herramientas
        self.addToolBar(barra_herramientas)
        accion1 = QAction("Imprimir por consola", self)
        accion1.triggered.connect(self.mostrar_mensaje)
        barra_herramientas.addAction(accion1)

    def mostrar_mensaje(self):
        print("Mensaje por consola")

app = QApplication()
window= Ventana()
window.show()
app.exec()
        
        