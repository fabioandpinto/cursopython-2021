"""
Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
CuantaJoven que deriva de la anterior. Cuando se crea esta nueva clase,
además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento.
Construye los siguientes métodos para la clase:
Un constructor.
Los setters y getters para el nuevo atributo.
En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad.,
por lo tanto hay que crear un método esTitularValido() que devuelve verdadero si el titular
es mayor de edad pero menor de 25 años y falso en caso contrario.
Además la retirada de dinero sólo se podrá hacer si el titular es válido.
El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.
Piensa los métodos heredados de la clase madre que hay que reescribir.
"""
from cuenta import Cuenta

class CuentaJoven(Cuenta):
    def __init__(self, titular, boni, edad, cantidad = 0):
        super().__init__(titular = titular, cantidad= cantidad)
        self.__boni = boni
        self.__edad = edad

    @property
    def boni(self):
        print(cj.boni)

    def setBoni(self, boni):
        self.__boni = boni

    @property
    def edad(self):
        print(cj.edad)

    def esTitularValido(self):
        if self.__edad >= 18 and self.__edad<= 25:
            return True
        else:
            return False

    def retirar(self, cantidad):
        if self.esTitularValido():
            super().retirar(cantidad)
        else:
            return print('No es titular valido')

cj = CuentaJoven('Juan', 0.3, 28)
cj.ingresar(35000) #metodo de cuenta
print(cj.cantidad)
cj.retirar(5000)
print(cj.cantidad)


