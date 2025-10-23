#Jose Antonio Álvarez Romero 2DAM 

#Ejercicio1
print(" - 1 - ")                #condicional segun un integer sea mayor, menor o igual a 0
num = int(input("Introduce un numero: "))

if num > 0:
    print("El número es positivo")
elif num < 0: 
    print("El número es negativo")
else:
    print("El número es cero")


#Ejercicio2
print(" - 2 - ")                #Condicional que compara dos integers
num1 = int(input("Introduce dos numeros. Numero 1: "))
num2 = int(input("Numero 2: "))
if num1 > num2:
    print("El primero es mayor que el segundo.")
elif num1 < num2: 
    print("El segundo es mayor que el primero.")
else:
    print("Ambos son iguales.")


#Ejercicio3
print(" - 3 - ")            #Condicional que compara si una cadena(una palabra) esta en otra cadena(una frase)
st = input("Introduce una frase: ")
wr = input("Introduce una palabra: ")

if wr in st:
    print("La palabra está en la frase.")
else: 
    print("La palabra no se encuentra.")

#Ejercicio4
print(" - 4 - ")        #Condicional que comprueba si una cadena empieza con mayuscula o acaba en "."
st = input("Introduce una frase: ")
if st[0].isupper():       
    print("Empieza por mayúscula.")
    if st.endswith("."): 
        print("Termina en punto.")
else: 
    print("El texto no cumple las condiciones.")

#Ejercicio5
print(" - 5 - ")                #Conjunto de condiciones que devuelve una frase en funcion del integer(nota) introducido.
num = int(input("Introduce una nota: (0-10) "))
if 4>= num >= 0 : 
    print("Insuficiente")
elif num == 5 :
    print("Suficiente")
elif num == 6 : 
    print("Bien")
elif num == 7 or num == 8:
    print("Notable")
elif 10>= num >= 9:
    print("Sobresaliente")
else:
    print("Nota no válida")