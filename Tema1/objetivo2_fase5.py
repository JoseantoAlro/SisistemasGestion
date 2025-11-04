#Jose Antonio Álvarez Romero 2DAM 

#Ejercicio1
st= input("Introduzca una frase: ")             #Modificación de mayúsculas y minúsculas
print(st.capitalize(),st.upper(),st.lower(),st.swapcase())

#Ejercicio2         #comprueba que es la cadena
print(st.isalpha(), st.isdigit(), st.isalnum(), st.islower(), st.isupper())

#Ejercicio3          #cuenta la cantidad de caracteres con y sin espacios
print(len(st), len(st.replace(" ", "")))

#Ejercicio4         #elimina espacios a los extremos de la cadena
print(st.strip(), st.lstrip(), st.rstrip())

#Ejercicio5         #reemplaza unos caracteres por otros
print(st.replace("Hola", "Adios"))

#Ejercicio6         # devuelve cual es el ultimo caracter alfabeticamente(max()) y cual el primero (min())
print("mayor: ",max(st),"menor", min(st))

#Ejercicio7     #divide la cadena por espacios y cuenta cuantas hay
print(st.split(), len(st.split()))

#Ejercicio8         # divide la cadena por / en vez de espacios
print(st.split("/"))