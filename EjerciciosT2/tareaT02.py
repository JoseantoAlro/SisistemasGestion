import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLineEdit,
    QLabel,
    QComboBox,
    QRadioButton,
    QTextEdit,
    QToolBar,
    QMessageBox,
    QHBoxLayout,
    QVBoxLayout,
    QFormLayout
)
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt, QSize


class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tarea T2")


  


        # TODO: tÃ­tulo y tamaÃ±o mÃ­nimo de la ventana
        # self.setWindowTitle(...)
        # self.setMinimumSize(...)

        # TODO: declarar atributos de widgets (title, categoria, prioridad, area de texto)
        # self.line_edit_titulo = None
        # ...

        # TODO: declarar acciones (limpiar, imprimir, salir, acerca de)
        # self.accion_limpiar_nota = None
        # ...

        # ConstrucciÃ³n general
        self.crear_central()       # TODO: completar
        self.crear_acciones()      # TODO: completar
        self.crear_menus()         # TODO: completar
        self.crear_toolbar()       # TODO: completar
        self.crear_statusbar()     # TODO: completar
        self.conectar_senales()    # TODO: completar

    # =========================
    # CREACIÃ“N DE LA ZONA CENTRAL
    # =========================
    def crear_central(self):
        estructura_vertical = QVBoxLayout()
        layout_formulario = QFormLayout()
        radio_group = QHBoxLayout()
        widget_central = QWidget()

        widget_central.setLayout(estructura_vertical)

        self.titulo = QLineEdit()
        self.titulo.setPlaceholderText("Escribe aquí un título")
        self.titulo.setMaxLength(12)

        self.combo = QComboBox()
        self.combo.addItems(["Trabajos","Ideas","Otros"])

        self.boton1 =  QRadioButton("Normal")
        self.boton1.setChecked(True)
        self.boton2 = QRadioButton("Alta")
        radio_group.addWidget(self.boton1)
        radio_group.addWidget(self.boton2)

        layout_formulario.addRow(QLabel("Título:"), self.titulo)
        layout_formulario.addRow(QLabel("CAtegoría:"), self.combo)
        layout_formulario.addRow(QLabel("Prioridad:"), radio_group)

        self.escribir = escribir = QTextEdit()
        escribir.setPlaceholderText("Escribe aqui el texto")
        escribir.setMinimumSize(QSize(500,300))

        estructura_vertical.addLayout(layout_formulario)
        estructura_vertical.addWidget(escribir)

        self.setCentralWidget(widget_central)

    # =========================
    # ACCIONES, MENÃš Y TOOLBAR
    # =========================
    def crear_acciones(self):
        self.accion1 = accion1 = QAction("Limpiar nota", self)
        self.accion2 = accion2 = QAction("Imprimir nota", self)
        self.accion3 = accion3 = QAction("Salir", self)
        self.accion4 = accion4 = QAction("Acerca de...", self)
        
        

    def crear_menus(self):

        barra_menu = self.menuBar()                 #creamos el menu 

        menu_archivo = barra_menu.addMenu("&Archivo")
        menu_ayuda = barra_menu.addMenu("&Ayuda")

        menu_archivo.addActions([self.accion1,self.accion2,self.accion3])
        menu_ayuda.addAction(self.accion4)
        

    def crear_toolbar(self):

        barra_herramientas = QToolBar("Barra principal")
        barra_herramientas.addActions([self.accion1,self.accion2])
        self.addToolBar(barra_herramientas)
        

    def crear_statusbar(self):
        self.barra_estado = self.statusBar()
        self.barra_estado.addPermanentWidget(QLabel(""))
        self.barra_estado.showMessage("Esperando accion...", 3000)
        

    # =========================
    # SEÃ‘ALES
    # =========================
    def conectar_senales(self):
        self.accion1.triggered.connect(self.slot_limpiar_nota)
        self.accion2.triggered.connect(self.slot_imprimir_nota)
        self.accion3.triggered.connect(self.slot_salir)
        self.accion4.triggered.connect(self.slot_acerca_de)
        
        self.titulo.textChanged.connect(self.slot_titulo_cambiado)
        self.combo.currentTextChanged.connect(self.slot_categoria_cambiada)
        self.boton1.clicked.connect(self.slot_prioridad_cambiada)
        self.boton2.clicked.connect(self.slot_prioridad_cambiada)
        # TODO conectar seÃ±ales como textChanged, currentTextChanged, toggled...
        pass

    # =========================
    # FUNCIONES DE UTILIDAD
    # =========================
    def obtener_prioridad_actual(self):
        
        # TODO devolver prioridad actual
        prioridad = ""
        if self.boton1.isChecked():
            prioridad = "Normal"
        elif self.boton2.isChecked():
            prioridad = "Alta"
            
        return prioridad    # Ãºnico return

    def limpiar_contenido_nota(self):
        self.titulo.setText("")
        self.combo.setCurrentIndex(0)
        self.escribir.setText("")
        self.boton1.setChecked(True)


    def imprimir_en_consola(self):
        print("====================\n",
              "    NOTA ACTUAL     \n",
              "====================\n",
              "Titulo: ", self.titulo.text(),"\n",
              "Categoria: ", self.combo.itemText(self.combo.currentIndex()), "\n",
              "Prioridad: ", self.obtener_prioridad_actual(), "\n",
              "---------------------- \n",
              "Contenido: \n",
              self.escribir.toPlainText())
        # TODO imprimir la nota completa usando print con comas
        pass

    # =========================
    # SLOTS (LOGICA)
    # =========================
    def slot_limpiar_nota(self):
        boton_limpiar = QMessageBox.question(
            self,
            "Limpiar nota",
            "¿Seguro que quieres limpiar todo?",
            buttons=QMessageBox.Yes | QMessageBox.No,
            defaultButton=QMessageBox.No
        )
        if boton_limpiar == QMessageBox.Yes:
            self.limpiar_contenido_nota()
        else:
            pass 
        

    def slot_imprimir_nota(self):
        self.imprimir_en_consola()
        QMessageBox.information(
            self, "Mensaje de información","La nota se ha impreso correctamente")

    def slot_salir(self):
        boton_salir = QMessageBox.warning(
            self,
            "salir",
            "¿Seguro que quieres Salir?",
            buttons=QMessageBox.Yes | QMessageBox.No,
            defaultButton=QMessageBox.No
        )
        if boton_salir == QMessageBox.Yes:
            self.close()

    def slot_acerca_de(self):
        QMessageBox.information(
            self, "Mensaje de información","Información sobre la app \n" \
            "Hecha en Desarrollo de interfaces \n" \
            "Modulo de DAM")

    def slot_titulo_cambiado(self, nuevo_titulo):
        self.setWindowTitle(nuevo_titulo)
        self.barra_estado.showMessage(nuevo_titulo)
        

    def slot_categoria_cambiada(self, nueva_categoria):
       self.barra_estado.showMessage(nueva_categoria)
        

    def slot_prioridad_cambiada(self, checked):
        if checked:
            if self.obtener_prioridad_actual()=="Normal":
                self.barra_estado.showMessage("Prioridad normal")
            elif self.obtener_prioridad_actual()=="Alta":
                self.barra_estado.showMessage("Prioridad alta")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()