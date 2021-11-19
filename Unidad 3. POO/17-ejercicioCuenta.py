"""
Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona)
y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional.
Construye los siguientes métodos para la clase:
Un constructor, donde los datos pueden estar vacíos.
Los setters y getters para cada uno de los atributos.
El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
mostrar(): Muestra los datos de la cuenta.
ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.

decorador - texto acompañado de @ que le asigna a bloque de codigo un caracteristica o comportamiento
"""
class Cuenta:
    def __init__(self, titular, cantidad = 0):
        self.__titular = titular
        self.__cantidad = cantidad

    # getter - property - para el getter - obtener una propiedad de la clase
    @property
    def titular(self):
        return self.__titular

    @property
    def cantidad(self):
        return self.__cantidad

    # setter
    def setTitular(self, titular):
        self.__titular=titular

    def setCantidad(self, cantidad):
        self.__cantidad = cantidad

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad
        else:
            pass

    def retirar(self, cantidad):
        self.__cantidad -= cantidad

c = Cuenta('Fabio', 450000)
c.ingresar(50000)
c.retirar(600000)

print(c.cantidad)





