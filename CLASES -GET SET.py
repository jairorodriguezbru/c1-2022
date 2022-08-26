


class Personas():
    __nombre = ""
    __apellido = ""
    __direccion = ""
    __telefono =""
    
    
    __activo = True



    def __init__(self):
        self.__nombre = input("digite nombre:")
        self.__apellido =input("digite apellido:")
        self.__direccion = input("digite direcicon:")
        self.__telefono = input("digite teledono:")
    
    


    def get_nombre(self):
        return(self.get_nombre)
    
    def set_nombre(self):
        return(self.get_nombre)



    def get_apellido(self):
        return(self.get_nombre)

    def set_apellido(self):
        return(self.get_nombre)
        
    
    def get_direccion(self):
        return(self.get_nombre)


    def set_direccion(self):
        return(self.get_nombre)



    def get_telefono(self):
        return(self.get_nombre)

    def set_telefono(self):
        return(self.get_nombre)



    
    def mostrarPersonas(self):
        print(f"Nombre: {self.__nombre}")
        print(f"Apellido: {self.__apellido}")
        print(f"Direccion: {self.__direccion}")
        print(f"Telefono: {self.__telefono}")
        print(f"Activo: {self.__activo}")

    def inactivo(self):
        self.__activo = False


p1=Personas()
p1.inactivo()
p1.mostrarPersonas()


