#Álvarez Romero, Jose Antonio 2DAM
#Ejercicio1
print(" - 1 - ")
num1 = int(input("numero 1: "))  #guardamos dos input como enteros y realizamos las operaciones matematicas
num2 = int(input("numero 2: "))
print("suma: ",num1+num2)
print("resta: ",num1-num2)
print("multiplicación: ", num1*num2)
print("division: ",(num1/num2))

#Ejercicio2
print(" - 2 - ")
num1 = float(input("Escribe tres numeros reales. Numero 1: "))  #guardamos tres input como reales y calculamos el promedio, con round() para redondear
num2 = float(input("numero 2: "))
num3 = float(input("numero 3: "))

print("el valor promerdio es", round((num1+num2+num3)/3, 2))

#Ejercicio3
print(" - 3 - ")
num1 = int(input("Escribe 2 numeros. Numero 1: "))      #guardamos dos input como enteros y los compara entre ellos o si es distinto a 0
num2 = int(input("numero 2: "))
print("el primero es mayor que el segundo", (num1>num2))
print("son iguales: ",num1==num2)
print("El segundo es distinto de 0: " ,num2!=0)

#Ejercicio4
print(" - 4 - ")
val1 = eval(input("introduce valor lógico: "))      #guardamos dos input como booleanos y realizamos operaciones logicas con ellos
val2 = eval(input("introduce otro valor lógico: "))
print("And:", val1 and val2)
print("Or: ", val1 or val2)
print("not 1: ", not val1 )
print("not 2: ", not val2 )

#Ejercicio5
print(" - 5 - ")
num1 = input("Escribe 2 numeros. Numero 1: ")       #guardamos dos input como strings, los sumamos convirtiendolos a enteros y calculamos el promedi
num2 = input("numero 2: ")                              #usando round() con un decimal
sum = int(num1)+int(num2)
print("suma: ", sum, "promedio: ", round(sum/2, 1))

#Ejercicio6
print(" - 6 - ")
num1 = float(input("Escribe 2 numeros. Numero 1: "))        #guardamos dos input como reales y realizamos operaciones logicas entre dos comparaciones numericas
num2 = float(input("numero 2: "))
print("(a > 10) and (b < 5): ",(num1 > 10) and (num2 < 5))
print("(a == b) or (b > 0): ", (num1 == num2) or (num2 > 0))
print("not (a < b): ", not (num1 < num2))

#Ejercicio7
print(" - 7 - ")
num1 = float(input("Escribe 2 reales. Numero 1: "))     #guardamos dos input como reales y los dividimos con un solo decimal con round()
num2 = float(input("numero 2: "))
print("division: ", round(num1/num2, 1))
