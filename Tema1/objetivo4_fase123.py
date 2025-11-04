#Álvarez Romero, Jose Antonio 2DAM

#Ejercicio1
print(" - 1 - ")                     #pido el numero de alumnos, inicializo las tuplas de notas y alumnos y creo un auxiliar para no modificar el total de alumnos
alm = int(input("Introduce el numero de alumnos: "))
noms= ()
medias = ()
almaux=alm
nualum=1 

while 0 < almaux:
    print("Alumno ",numalum)     #mientras los alumnos no sean 0 pide nombre y cantidad de notas, numalum hace que el numero del alumno sea creciente en vez de decreciente
    numalum+=1
    nom = input("¿Como se llama? ")
    notas = int(input("¿Cuantas notas tiene "+nom+"? "))
    sum = 0

    i=0
    for i in range(notas):           #por cada nota sumala a las anteriores y calcula la media entre la suma y la cantidad de notas
        m=int(input("introduce la nota " + str(i+1) + " "))
        sum = sum+m
    med = (sum/notas)

    nota=0                          #muestra si está aprobado o noo
    if 5<=med:
        nota= "Aprobado"
    elif 4<=med<5:
        nota= "Necesita mejorar"
    elif 0<med<4:
        nota="Suspenso"
    print("Media de ",nom, ": ", str(med)," -->", nota )

    noms= noms+(nom,)                #guarda en las tuplas anteriores los valores del nombre y la media por cada alumno
    medias= medias+(med,)
    almaux -=1
    print("\n")

mediasTot=0
ap=0
mej=0
sus=0
for item in medias:                 #Cuenta cuantas veces hay una nota suspensa, aprobada o necesita mejora en la tupla medias
    mediasTot += item                #es lo mismo que ir guardando en una tupla nueva los valores "aprobado,..." y contarlos sin tener que hacer una tupla nueva
    if 5<=item:
        ap +=1
    elif 4<=item<5:
        mej +=1
    elif 0<item<4:
        sus+=1


print("--- RESUMEN FINAL---")                               #enseña por pantalla la media de la clase
print("media del grupo: ", round((mediasTot/alm) , 2),
      "\nAprobados: ", ap,
      "\nNecesitan mejorar: ", mej,
      "\nSuspensos: ", sus)