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