#Jose Antonio Álvarez Romero 2DAM 

#Ejercicio1
print(" - 1 - ")
num1 = int(input("Escribe 3 numeros. Numero 1: "))      #guardamos tres input como enteros y los compara logicamente dos comparaciones matematicas
num2 = int(input("numero 2: "))
num3 = int(input("numero 3: "))

print("(a < b) and (b < c): ", (num1 < num2) and (num2 < num3))
print("(a == b) or (b == c): ", (num1 == num2) or (num2 == num3))
print("not (a > c): ", not (num1 > num3))