class Punto:
    def __init__(self, x, y):
        self.X = x
        self.Y = y
    def MostrarPunto(self):
        print("El punto es(", self.X,", ", self.Y, ")")


class Triangulo:
    def __init__(self,v1,v2,v3):
        self.V1 = v1
        self.V2 = v2
        self.V3 = v3
    def MostrarVertices(self):
        self.V1.MostrarPunto()
        self.V2.MostrarPunto()
        self.V3.MostrarPunto()


p1 = Punto(4,6)
p2 = Punto(1,-7)
p1.MostrarPunto()
p2.MostrarPunto()
p2.x = 3
p2.MostrarPunto()
p2 = p1
p2.MostrarPunto()

p3= Punto(5,8)
p4 = Punto(2,9)

triangulo = Triangulo(p1,p3,p4)
print(triangulo.MostrarVertices())

#override si n se sabe cuantos parametros hay
def Sumar2(*valores):       #se pasan varios valores
    resultado = 0
    for item in valores:
        resultado = resultado+item
    return resultado


class Ppublico:
     def __init__(self, x, y):
        self.X = x
        self.Y = y

class Pprivado:
    def __init__(self, x, y):
        self.__x= x
        self.__y= y
    
    def GetX(self):
        return self.__x
    def GetY(self):
        return self.__y
    def SetX(self,x):
        self.__x = x
    def SetY(self,y):
        self.__y = y
    
publico=Ppublico(4,6)
privado=Pprivado(2,7)

print("valores p publico", publico.X, publico.Y)
print("valores privado", privado.GetX(), privado.GetY())