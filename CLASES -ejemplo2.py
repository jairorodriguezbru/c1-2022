


class Personas():
    __nombre = ""
    __apellido = ""
    __direccion = ""
    __telefono =""
    activo__ = True



    def __init__(self):
        self.__nombre = input("digite nombre:")
        self.__apellido =input("digite apellido:")
        self.__direccion = input("digite direcicon:")
        self.__telefono = input("digite teledono:")



    def  mostrarPersonas(self):
        print (f"nombre:{self.__nombre}")
        print (f"apellido:{self.__apellido}")
        print (f"direccion:{self.__direccion}")
        print (f"telefono:{self.__telefono}")


    def inactivo(self):
        self.activo__ = False


p1=Personas()
p1.inactivo()
p1.mostrarPersonas()


