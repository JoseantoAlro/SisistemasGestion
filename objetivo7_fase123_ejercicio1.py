#Álvarez Romero, Jose Antonio 2DAM

class Vehiculo:                                     #creación de clase vehiculo con sus metodos
    def __init__(self, marca, velIni=0):
        self.__Marca = marca
        self.__VelIni = velIni
    
    def Acelerar(self, v):
        self.__VelIni = (self.__VelIni + v)
    
    def Desacelerar(self, v):
        self.__VelIni = (self.__VelIni - v)

    def getMarca(self):
        return self.__Marca
    
    def setMarca(self, marca):
        self.__Marca = marca

    def getVelIni(self):
        return self.__VelIni
    
    def setVelIni(self, v):
        self.__VelIni = v

    def MostrarVelocidad(self):
        print("la velocidad actual es ", self.getVelIni())


class Coche(Vehiculo):                                       #para llamar a la clase padre vehiculo con velIni iniciada en 0
    def __init__(self,marca,velIni, bocina = "¡tuuut!"):
        super().__init__(marca,velIni)
        self.__Bocina =  bocina
    
    def tocar_claxon(self):
        print(self.__Bocina)



coche_1 = Coche("Peugeot 208", 10.5)                    #test de metodos

print(coche_1.getMarca())
coche_1.MostrarVelocidad()

coche_1.Acelerar(50)
coche_1.Desacelerar(15)
coche_1.MostrarVelocidad()

coche_1.tocar_claxon()
        
