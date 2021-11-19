"""
Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y cedula.
Construye los siguientes métodos para la clase:
Un constructor, donde los datos pueden estar vacíos.
Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
mostrar(): Muestra los datos de la persona.
esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.
"""

class Persona:
    def __init__(self, nombre="", edad=0, cedula=""):
        self.__nombre = nombre
        self.__edad = edad
        self.__cedula = cedula

    ## setter
    def setNombre(self, nombre):
        self.__nombre=nombre

    def setEdad(self, edad):
        self.__edad = edad

    def setCedula(self, cedula):
        self.__cedula = cedula

    ## getter
    def getNombre(self):
        return self.__nombre

    def getEdad(self):
        return self.__edad

    def getCedula(self):
        return self.__cedula

    # metodo mostrar
    def mostrar(self):
        return "Nombre: " + self.__nombre + " , Edad: " + str(self.__edad) + " , Cedula: " + str(self.__cedula)

    def esMayor(self):
        if self.__edad >= 18:
            return True
        else:
            return False

per = Persona()
print(per.mostrar())

per.setNombre("Juan David")

print(per.mostrar())
per.setEdad(30)
print(per.mostrar())

per.setCedula(1098888999)
print(per.mostrar())
print(per.getNombre())

print(per.getEdad())
print(per.getCedula())

if per.esMayor():
    print("Es mayor de edad")
else:
    print("no es mayor")



