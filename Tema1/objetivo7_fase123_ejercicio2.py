#Álvarez Romero, Jose Antonio 2DAM


class Video:
    def __init__(self,tituloV,duracionV,categoriaV):        #creacion de la clase video
        self.TituloV = tituloV
        self.DuracionV = duracionV
        self.CategoriaV = categoriaV

    def mirar_video(self):
        print("Iniciando video...")
        print("El video que estas viendo se titula ", self.TituloV," de la categoría ", self.CategoriaV, " y duración ", self.DuracionV, "minutos")

    def detener_video(self):
        print("Deteniendo video.")



class Audio:                                                #creacion de la clase audio
    def __init__(self,tituloA,artistaA):
        self.__TituloA = tituloA
        self.__ArtistaA = artistaA

    def escuchar_audio(self):
        print("Iniciando audio...")
        print("El audio que estas escuchando se titula", self.__TituloA, " del artista ",self.__ArtistaA)

    def detener_audio(self):
        print("Deteniendo audio.")


class Media(Video,Audio):                                               #creacion de clase medio heredando de las clases video y audio, las cuales comparten atributos
    def __init__(self,titulo,duracionV,categoriaV,artistaA):
        Video.__init__(self,titulo,duracionV,categoriaV)
        Audio.__init__(self,titulo,artistaA)
        self.TituloM = titulo
        self.CategoriaM = categoriaV
        self.DuracionM = duracionV
        self.ArtistaM = artistaA


medio_1 = Media("Titulo 1", 180, "infantil", "Artista 1")                       #test de metodos
medio_1.escuchar_audio()
medio_1.mirar_video()
medio_1.detener_audio()
medio_1.detener_video()