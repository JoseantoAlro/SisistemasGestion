#Álvarez Romero, Jose Antonio 2DAM

#Ejercicio1   

def Sumar(num1,num2):           #Procedimientos con las operaciones matematicas 
    return num1 + num2

def Restar(num1,num2):
    return num1 - num2

def Multiplicar(num1,num2):
    return num1 * num2

def Dividir(num1,num2):
    return num1 / num2

def Potencia(num1,num2):
    return num1 ** num2

def Raiz_Cuadrada(num1):
    return num1 ** (1/2)

def modulo(num1,num2):
    return num1%num2

def EsNum(num):                 #Comprueba si el imput(cadena) es un numero y mientras no lo sea pide que introduzca uno válido
    while not num.isdigit():
        num = input("Introduzca un número válido: ")
    if num.isdigit():           #Si es un numero pero en formato cadena lo convierte a int, fuera del while porque si no pasa
            num  = int(num)     #de cadena pero no número a número pero no cadena y el while no puede leerlo
    return num
    
#Ejercicio2

def menu():
    print("""=========================
  CALCULADORA AVANZADA
=========================
1) Sumar
2) Restar
3) Multiplicar
4) Dividir
5) Operaciones avanzadas
6) Salir""")
    bucle = True
    while bucle == True:                                            #Crea un bucle con el menu mientras no se salga del menu se repite, segun la opcion llama a uno u otro procedimiento
        print("")
        opcion = int(EsNum(input("Elige una opción: ")))
        if opcion==1:
            num1 = int(EsNum(input("Introduce el primer número: ")))
            num2 = int(EsNum(input("Introduce el segundo número: ")))
            print("El resultado de la suma es ", round(Sumar(num1,num2),2))
        if opcion == 2:
            num1 = int(EsNum(input("Introduce el primer número: ")))
            num2 = int(EsNum(input("Introduce el segundo número: ")))
            print("El resultado de la resta es ", round(Restar(num1,num2),2))
        if opcion == 3:
            num1 = int(EsNum(input("Introduce el primer número: ")))
            num2 = int(EsNum(input("Introduce el segundo número: ")))
            print("El resultado de la multiplicación es ", round(Multiplicar(num1,num2),2))
        if opcion == 4:
            num1 = int(EsNum(input("Introduce el dividendo: ")))
            num2 = int(EsNum(input("Introduce el divisor: ")))
            print("El resultado de la multiplicación es ", round(Dividir(num1,num2),2))
        if opcion == 5:                             #crea un submenu y pide una letra en vez de un numero
            print("""Operaciones avanzadas:
a) Potencia
b) Raíz cuadrada
c) Módulo
d) Volver""")
            opcionAvan = input("Selecciona una opción")
            if opcionAvan == "a":
                num1 = int(EsNum(input("Introduce la raiz: ")))
                num2 = int(EsNum(input("Introduce el exponente: ")))
                print("El resultado es ", round(Potencia(num1,num2),2))
            if opcionAvan == "b":
                num1 = int(EsNum(input("Introduce el numero a calcular: ")))
                print("La raiz cuadrada es ", round(Raiz_Cuadrada(num1), 2))
            if opcionAvan == "c":
                num1 = int(EsNum(input("Introduce la raiz: ")))
                num2 = int(EsNum(input("Introduce el exponente: ")))
                print("El modulo de la division es ", round(modulo(num1,num2), 2))
            if opcionAvan == "d":
                print("Volviendo...")
            else: 
                print("letra no valida")
        if  opcion == 6:                        #Por último cierra el bucle y con ello el programa
            bucle = False
            print("Fin del programa. Adios")
        else:
            print("Número no válido")


menu()

