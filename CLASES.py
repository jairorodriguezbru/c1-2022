


class Personas():
    nombre = ""
    apellido = ""
    direccion = ""
    telefono =""
    activo = True



    def agregarPersonas(self):
        self.nombre = "jairo"
        self.apellido = "apellido"
        self.direccion = "direccion"
        self.telefono = "telefono"



    def  mostrarPersonas(self):
        print (f"nombre:{self.nombre}")
        print (f"apellido:{self.apellido}")
        print (f"direccion:{self.direccion}")
        print (f"telefono:{self.telefono}")


    def inactivo(self):
        self.activo=False


p1=Personas()
p1.agregarPersonas()
p1.mostrarPersonas()
p1.nombre = "jair"
p1.activo

