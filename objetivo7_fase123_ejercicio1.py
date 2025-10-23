#Álvarez Romero, Jose Antonio 2DAM

class Vehiculo:
    def __init__(self, marca, VelIni=0):
        self.__marca = marca
        self.__VelIni = VelIni
    
    def Acelerar(self, v):
        self.__VelIni = (self.__VelIni + v)
    
    def Desacelerar(self, v):
        self.__VelIni = (self.__VelIni - v)

    def getMarca(self):
        return self.__marca
    
    def setMarca(self, marca):
        self.__marca = marca

    def getVelIni(self):
        return self.__VelIni
    
    def setVelIni(self, v):
        self.__VelIni = v

    def MostrarVelocidad(self):
        print("la velocidad actual es ", self.getVelIni())


class Coche(Vehiculo):          #para llamar a la clase padre vehiculo con velIni iniciada en 0
    def __init__(self, bocina = "¡tuuut!"):
        super().__init__(self)
        self.__bocina =  bocina
    
    def tocar_claxon(self):
        print(self.__bocina)



coche_1 = Coche("Peugeot 208")
coche_1.setVelIni(10.5)
print(coche_1.getMarca())
coche_1.MostrarVelocidad()
coche_1.Acelerar(50)
coche_1.Desacelerar(15)
coche_1.MostrarVelocidad()
coche_1.tocar_claxon()
        
