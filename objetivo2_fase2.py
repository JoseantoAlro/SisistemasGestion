#Jose Antonio Álvarez Romero 2DAM 
#Ejercicio1
print(" - 1 - ")				#guardamos cuatro input como strings
nom = input("¿Cual es tu nombre?")
cur = input("¿Cual es tu curso?")
grup = input("¿Cual es tu grupo?")
carp = input("¿Cual es la carpeta del proyecto?")


#Ejercicio2
print(" - 2 - ")		#imprimimos por pantalla los valores anteriormente guardados
print("""------------------------------
	Ficha del alumno/a
------------------------------
Nombre: """+nom+"""
Curso: """+cur+ """ DAM	Grupo: """+grup+""" 
Ruta del proyecto: C:\\Users\\"""+nom+"""\\DAM\\"""+carp+"""
------------------------------""")