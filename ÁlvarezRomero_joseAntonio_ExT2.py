import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow,                  #imports standar

    QDialog, QTabWidget, QWidget, QLabel,       #import widgets
    QLineEdit, QComboBox, QDockWidget,
    QCheckBox, QRadioButton, QToolBar,
    QMessageBox,QDialogButtonBox,

    QFormLayout, QVBoxLayout, QHBoxLayout       #import layouts
)
from PySide6.QtCore import Qt                   #import flags
from PySide6.QtGui import QAction,QKeySequence  #import acciones
# Importar lo necesario


# ===================================================================
#                            LOGIN
# ===================================================================
class DialogoLogin(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Iniciar sesión")

        botones = QDialogButtonBox.Ok | QDialogButtonBox.Cancel     #dialogo de inicio de sesion
        self.caja = QDialogButtonBox(botones)

        #elementos y layouts a usar
        self.inicio = QVBoxLayout()
        self.inicioini=QWidget()
        self.inicio_layout = QFormLayout()
        self.nombreini = QLineEdit()
        self.contrasenaini = QLineEdit()
        self.tituloini= QLabel("introduzca sus credenciales")

        #formulario
        self.inicio_layout.addRow(QLabel("nombre: "), self.nombreini)
        self.inicio_layout.addRow(QLabel("contraseña: "), self.contrasenaini)

        self.inicioini.setLayout(self.inicio_layout)


        self.inicio.addWidget(self.tituloini)   #titulo
        self.inicio.addWidget(self.inicioini)   #formulario
        self.inicio.addWidget(self.caja)        #boton de enviar o cancelar
        self.setLayout(self.inicio)
        
        
        self.caja.accepted.connect(self.aceptar)
        self.caja.rejected.connect(self.reject)

        

    def aceptar(self):
        if self.nombreini != "" and self.contrasenaini.text()=="interfaces":
            self.parent.nombre.setText(self.nombreini.text())     #deberia ir al padre y cambiar esa variable pero no lo hace
            self.close()                                          #he probado intentando devolverlo con un return o guardandolo desde el metodo que crea el dialogo(no me ha salido)
            
        else:       #si no es correcto manda una alerta
            QMessageBox.critical(
            self,
            "Error de validacion",
            "Credenciales no validas",
            buttons=QMessageBox.Ok,
        )
            
        # TODO: Crear el diseño y los widgets del diálogo de login


# ===================================================================
#                        VENTANA PRINCIPAL
# ===================================================================
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Encuesta de satisfacción")
        self.setMinimumSize(800, 600)

        # TODO: declarar variables necesarias
        #declaramos las pestañas y los layouts a usar
        self.pest = QTabWidget()  
        self.layout_formulario1 = QFormLayout()
        self.layout_formulario2 = QFormLayout()
        self.pestana2 = QVBoxLayout()
        self.botones_radio = QHBoxLayout()

        #form1 elementos
        self.nombre= QLineEdit()
        self.telefono = QLineEdit()
        self.compania = QComboBox()
        self.satisfaccion = QComboBox()

        #form2 elementos
        self.cobertura = QComboBox()
        self.velocidad = QComboBox()
        self.atencion = QComboBox()
        self.calidad = QComboBox()

        
        #checkboxs  
        self.titulocheck= QLabel("Preferencias del servicio")
        self.check1 = QCheckBox("Valoro mas la cobertura que el precio")
        self.check2 = QCheckBox("Valoro mas el precio que la velocidad")
        self.check3 = QCheckBox("Me interesan las ofertas y promociones")
        self.check4 = QCheckBox("Estoy pensando en cambiar de compañia")

        #radiobutons
        self.tituloradio = QLabel("¿Recomienda la compañia?:")
        self.radio1 = QRadioButton("Si")
        self.radio2 = QRadioButton("No")


        self.crear_central()
        self.crear_acciones()
        self.crear_menus()
        self.crear_toolbar()
        self.crear_statusbar()
        self.crear_dock_notas()
        self.conectar_senales()

    # ---------------------------------------------------------------
    def crear_central(self):

        self.setCentralWidget(self.pest)

        #pestaña 1
        self.nombre.setPlaceholderText("Inicia sesión para rellenar el nombre")
        self.nombre.setEnabled(False)
        self.telefono.setPlaceholderText("Número de telefono")
        self.compania.addItems(["MoviPlus","Orange","Avatel","Vodafone"])
        self.satisfaccion.addItems(["Muy mala","Mala","Media","Buena", "Muy buena"])

        #pestaña 2
            #formulario
        self.cobertura.addItems(["Muy mala","Mala","Media","Buena", "Muy buena"])
        self.velocidad.addItems(["Muy mala","Mala","Media","Buena", "Muy buena"])
        self.atencion.addItems(["Muy mala","Mala","Media","Buena", "Muy buena"])
        self.calidad.addItems(["Muy mala","Mala","Media","Buena", "Muy buena"])


            #radioButtons
        self.radio1.setChecked(True)  #si recomienda por defecto
        


        #construccion de layouts y pestañas
            #rellenamos el formulario de la pestaña 1
        self.layout_formulario1.addRow(QLabel("Nombre:"), self.nombre)
        self.layout_formulario1.addRow(QLabel("Telefono:"), self.telefono)
        self.layout_formulario1.addRow(QLabel("Compañia:"), self.compania)
        self.layout_formulario1.addRow(QLabel("Satisfaccion:"), self.satisfaccion)

            #rellenamos el formulario de la pestaña 2
        self.layout_formulario2.addRow(QLabel("Calidad de cobertura:"), self.cobertura)
        self.layout_formulario2.addRow(QLabel("Nivel de velocidad:"), self.velocidad)
        self.layout_formulario2.addRow(QLabel("Calidad de atención al cliente:"), self.atencion)
        self.layout_formulario2.addRow(QLabel("Puntuacion Calidad-precio:"), self.calidad)

        self.botones_radio.addWidget(self.radio1)
        self.botones_radio.addWidget(self.radio2)

        self.pestana2.addLayout(self.layout_formulario2)
        self.pestana2.addWidget(self.titulocheck)
        self.pestana2.addWidget(self.check1)
        self.pestana2.addWidget(self.check2)
        self.pestana2.addWidget(self.check3)
        self.pestana2.addWidget(self.check4)
        self.pestana2.addWidget(self.tituloradio)
        self.pestana2.addLayout(self.botones_radio)


        opcion1 = QWidget()
        opcion1.setLayout(self.layout_formulario1)
        opcion2 = QWidget()
        opcion2.setLayout(self.pestana2)        
        self.pest.addTab(opcion1,"Datos de la persona")         #añadimos los layouts a las pestañas
        self.pest.addTab(opcion2,"opinion sobre el servicio")                       
        #pest.addTab(opcion2,"Opinion sobre el servicio")

        

    # ---------------------------------------------------------------
    def crear_dock_notas(self):
        #dock inferior
        panel3 = QDockWidget("Notas Internsa", self)            #creamos el dock
        notas = QLineEdit()
        notas.setPlaceholderText("Notas Internas sobre la encuesta")
        notas.setMinimumHeight(200)
        panel3.setWidget(notas)
        panel3.setFeatures(QDockWidget.DockWidgetClosable | QDockWidget.DockWidgetFloatable) #propiedades (cerrable y fotable)
        self.notas=notas
        self.addDockWidget(Qt.BottomDockWidgetArea, panel3) #posicion abajo

    # ---------------------------------------------------------------
    def crear_acciones(self):
        # TODO: Crear las acciones del menú y la toolbar
        self.accion1 = QAction("Iniciar sesion", self)   #acciones con sus atajos
        self.accion1.setShortcut(QKeySequence("Ctrl+P"))
        self.accion2 = QAction("Nueva encuesta", self)
        self.accion3 = QAction("Ver resumen", self)
        self.accion3.setShortcut(QKeySequence("Ctrl+L"))
        self.accion4 = QAction("Salir", self)
        self.accion5 = QAction("Acerca de...", self)

        self.nombre.textChanged.connect(self.slot_nombre_cambiado)
        self.satisfaccion.currentIndexChanged.connect(self.slot_satisfaccion_cambiada)
        pass

    # ---------------------------------------------------------------
    def crear_menus(self):
        
        barra_menu = self.menuBar()                 #creamos la barra de menu

        menu_encuesta = barra_menu.addMenu("&Encuesta") #añadimos las pestañas del menu (dos menus)
        menu_ayuda = barra_menu.addMenu("&Ayuda")

        menu_encuesta.addActions([self.accion1,self.accion2,self.accion3]) #asignamos las acciones al menu
        menu_encuesta.addSeparator()  #esto no añade el separador a no ser que añada un separador entre cada accion
        menu_encuesta.addAction(self.accion4)
        
        menu_ayuda.addAction(self.accion5)
        pass

    # ---------------------------------------------------------------
    def crear_toolbar(self):
        # TODO: Crear la toolbar y añadir las acciones
        barra_herramientas = QToolBar("Barra principal")        #creamos un toolbar y agregamos las acciones que qeremos usar
        barra_herramientas.addActions([self.accion2,self.accion3])
        self.addToolBar(barra_herramientas)
        pass

    # ---------------------------------------------------------------
    def crear_statusbar(self):
        self.barra_estado = self.statusBar()
        self.barra_estado.addPermanentWidget(QLabel(""))
        self.barra_estado.showMessage("Esperando accion...", 3000)
        pass

    # ---------------------------------------------------------------
    def conectar_senales(self):
        self.accion1.triggered.connect(self.slot_login)             #conectamos las acciones a un slot
        self.accion2.triggered.connect(self.slot_nueva_encuesta)
        self.accion3.triggered.connect(self.slot_ver_resumen)
        self.accion4.triggered.connect(self.slot_salir)
        self.accion5.triggered.connect(self.slot_acerca_de)
        pass

    # ---------------------------------------------------------------
    def slot_login(self):
        dialogo =DialogoLogin(self)  #crea un dialogo y lo ejecuta
        dialogo.exec() 

    # ---------------------------------------------------------------
    def slot_nueva_encuesta(self):
        # TODO: Limpiar los datos tras confirmación
        boton_limpiar = QMessageBox.question(
            self,
            "Limpiar Datos",
            "¿Seguro que quieres limpiar todo?",
            buttons=QMessageBox.Yes | QMessageBox.No,
            defaultButton=QMessageBox.No
        )
        if boton_limpiar == QMessageBox.Yes:  #si confirma los valores son los predeterminados
            self.nombre.setText("")
            self.notas.setText("")
            self.telefono.setText("")
            self.compania.setCurrentIndex(0)
            self.satisfaccion.setCurrentIndex(0)

            self.cobertura.setCurrentIndex(0)
            self.velocidad.setCurrentIndex(0)
            self.atencion.setCurrentIndex(0)
            self.calidad.setCurrentIndex(0)

            self.check1.setChecked(False)
            self.check2.setChecked(False)
            self.check3.setChecked(False)
            self.check4.setChecked(False)
            self.radio1.setChecked(True)
            self.radio2.setChecked(False)
        else:
            pass 

        pass

    # ---------------------------------------------------------------
    def slot_ver_resumen(self):
        # TODO: Mostrar un resumen de la encuesta
        recom = "No"
        if self.radio1.isChecked():   #coje el valor del radio 1 si esta activado, valor no si no lo esta
            recom= "si"
        QMessageBox.information(
            self
            ,"Resumen de aplicacion"
            ,"nombre: "+self.nombre.text()+"\n"
            +"telefono:"+self.telefono.text()+"\n"
            +"compañia"+self.compania.itemText(self.compania.currentIndex())+"\n"
            +"Recomienda: "+recom
            )

       
    # ---------------------------------------------------------------
    def slot_salir(self):
        # TODO: Confirmar y cerrar la aplicación
        boton_salir = QMessageBox.warning(
            self,
            "salir",
            "¿Seguro que quieres Salir?",
            buttons=QMessageBox.Yes | QMessageBox.No,
            defaultButton=QMessageBox.No
        )
        if boton_salir == QMessageBox.Yes:  #si pulsa si cierra la aplicacion
            self.close()
        pass

    # ---------------------------------------------------------------
    def slot_acerca_de(self):
        # TODO: Mostrar información sobre la aplicación
        QMessageBox.information(
            self
            ,"Acerca de..."
            ,"Aplicacion de satisfaccion del cliente \n"+"los datos seran analizados con cuidado \n"+
            "Curso Dam")

        pass

    # ---------------------------------------------------------------
    def slot_compania_cambiada(self, nueva):
        # TODO: Mensaje en la barra de estado
        pass

    # ---------------------------------------------------------------
    def slot_satisfaccion_cambiada(self, nueva):
        # TODO: Mensaje en la barra de estado
        #self.barra_estado.showMessage(nueva)  #no me ha dao timepo de mostrarlo por barra de estado pero tmp lo pide el enunciado
        pass

    # ---------------------------------------------------------------
    def slot_recomienda_cambiado(self, checked):
        # TODO: Mensaje en la barra de estado
        pass

    # ---------------------------------------------------------------
    def slot_nombre_cambiado(self, nuevo_nombre):
        # TODO: Actualizar el título de la ventana
        pass


# ===================================================================
#                       EJECUCIÓN DE LA APP
# ===================================================================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()

