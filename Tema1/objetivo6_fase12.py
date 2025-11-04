#Álvarez Romero, Jose Antonio 2DAM

#Ejercicio1   

class Autor:                                                #constructor de las clases con sus metodos
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
    
    def mostrarAutor(self):
        print(self.nombre," ", self.apellidos)

class Libro:
    def __init__(self, titulo, isbn,):
        self.titulo = titulo
        self.isbn = isbn
        self.autor = None
        
    def añadirAutor(self,autor):
        self.autor = autor

    def mostrarLibro(self):                                     
        print("""------ Libro ------
Título: """,self.titulo,"""
ISBN: """,self.isbn,"""
Autor: """, end=""),self.autor.mostrarAutor()               #mostrar autor fuera del print porque ya es un print

    def obtenerTitulo(self):
        return self.titulo

class Biblioteca:
    def __init__(self, listaLibros):
        self.listaLibros = listaLibros

    def numeroLibros (self):
        return len(self.listaLibros)
    
    def añadirLibro(self, libro):
        self.listaLibros.append(libro)
        
    def borrarLibro(self, titulo):                               #por cada libro de la biblioteca obtiene el titulo y si coincide con el parametro lo elimina
        encontrado = 0   
        for libro in self.listaLibros:
            if libro.obtenerTitulo() == titulo:
                self.listaLibros.remove(libro)
                encontrado = 1
                print("¡Libro borrado con exito!")
        if encontrado == 0:    
            print("Libro no encontrado")
    
    def mostrarBiblioteca(self):                                    #llamada a mostrar libro por cada libro de la biblioteca
        print("########################################")
        for libro in self.listaLibros:
            libro.mostrarLibro()



bucle=True
listaAux= []
biblio = Biblioteca(listaAux)                                               ##bucle del programa
while bucle == True:
    opcion = int(input("""Menu
1) Añadir libro a la biblioteca
2) Mostrar biblioteca
3) Borrar libro
4) ¿Número de libros?
5) Salir
"""))
    if opcion == 1:                                                 #pide valores y crea un objeto autor que añade a un objeto libro que añade a un objeto biblioteca
        libroNom = input("Introducir nombre del libro: ")
        libroIsbn = input("Introducir ISBN del libro: ")
        Autornom = input("Introducir nombre del Autor: ")
        AutorAp = input("Introducir nombre del Apellido: ")
        Au = Autor(Autornom, AutorAp)
        libronuevo = Libro(libroNom,libroIsbn)
        libronuevo.añadirAutor(Au)
        biblio.añadirLibro(libronuevo)

    if opcion == 2:
        biblio.mostrarBiblioteca()
    
    if opcion==3:
        libroaBorrar = input("Introduzca el libro a borrar: ")
        biblio.borrarLibro(libroaBorrar)
    
    if opcion == 4:
        print("El numero de libros es ", biblio.numeroLibros())
    
    if opcion == 5:
        bucle=False
        print("¡Hasta la próxima!")
        