#Álvarez Romero, Jose antonio
import os
from PySide6.QtWidgets import (QApplication
                               ,QMainWindow
                               ,QPushButton
                               ,QWidget
                               ,QColorDialog
                               ,QLabel
                               ,QFileDialog
                               ,QFontDialog
                               ,QVBoxLayout
)


class Ventana(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestion de archivos y preferencias")

       
        self.layout_vertical = QVBoxLayout()        #layout con todos los componentes
        
        componente_principal = QWidget()
        componente_principal.setLayout(self.layout_vertical)

        boton1 = QPushButton("abrir archivo de texto")      #botones con sus acciones
        boton1.clicked.connect(self.abrir_archivo)
        boton2 = QPushButton("Guardar archivo como")
        boton2.clicked.connect(self.guardar_archivo)
        boton3 = QPushButton("Elegir color de fondo")
        boton3.clicked.connect(self.elegir_color)
        boton4 = QPushButton("CAmbiar fuente de texto")
        boton4.clicked.connect(self.elegir_fuente)

        self.layout_vertical.addWidget(boton1)      
        self.layout_vertical.addWidget(boton2)
        self.layout_vertical.addWidget(boton3)
        self.layout_vertical.addWidget(boton4)
        self.setCentralWidget(componente_principal)

    def abrir_archivo(self):
        ventana_dialogo = QFileDialog.getOpenFileName(  #abre un arechivo
        self,
        caption="Abrir archivo ...",
        dir="./",
        filter="Documentos de texto (*.txt);",
        selectedFilter="Documentos de texto (*.txt)"
        )
        archivo = ventana_dialogo[0]            #guarda el archivo
        nombre = os.path.basename(archivo)      #guarda el nombre
        self.texto = QLabel("archivo: "+nombre) # guarda en un qlabel el nombre del archuivo
        self.layout_vertical.addWidget(self.texto)
         

    def guardar_archivo(self):
           
        ventana_dialogo = QFileDialog.getSaveFileName(
        self,
        caption="Guardar archivo ...",
        dir="./",
        filter="Documentos de texto (*.txt);",
        selectedFilter = "Documentos de texto (*.txt);" 
        )
        archivo = ventana_dialogo[0]
        print(archivo)
    

    def elegir_color(self):   
        color = QColorDialog.getColor()     #si elige color cambia el qlabel
        if color.isValid():
            self.texto.setStyleSheet(f"background-color: {color.name()}")

    def elegir_fuente(self):        #si elige fuente cambia el qlabel
        seleccionada, fuente = QFontDialog.getFont(self)
        if seleccionada:
            self.texto.setFont(fuente)

app=QApplication()
window=Ventana()
window.show()
app.exec()
