class Persona():
    __activo = True

    def __init__(self, nombre, apellido, direccion, telefono):    
        self.__nombre = nombre
        self.__apellido = apellido
        self.__direccion = direccion
        self.__telefono = telefono

    def get_nombre(self):
        return (self.__nombre)

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_apellido(self):
        return (self.__apellido)

    def set_apellido(self, apellido):
        self.__apellido = apellido

    def get_direccion(self):
        return (self.__direccion)

    def set_direccion(self, direccion):
        self.__direccion = direccion

    def get_telefono(self):
        return (self.__telefono)

    def set_telefono(self, telefono):
        self.__telefono = telefono

    nombre = property(get_nombre, set_nombre)
    apellido = property(get_apellido, set_apellido)
    direccion = property(get_direccion, set_direccion)
    telefono = property(get_telefono, set_telefono)


    def mostrarPersona(self):
        print(f"Nombre: {self.__nombre}")
        print(f"Apellido: {self.__apellido}")
        print(f"Direccion: {self.__direccion}")
        print(f"Telefono: {self.__telefono}")
        print(f"Activo: {self.__activo}")

    def inactivoPersona(self):
        self.__activo = False

def inicio():
    nom = input("Ingrese el Nombre ")
    ape = input("Ingrese el Apellido ")
    dire = input("Ingrese la Direccion ")
    tel = input("Ingrese la Cedula ")  
    p1 =  Persona(nom, ape, dire, tel)
    p1.nombre = 'NiCo' 
    print(p1.nombre)
    p1.inactivoPersona()
    p1.mostrarPersona()


if __name__ == "__main__":
    inicio()