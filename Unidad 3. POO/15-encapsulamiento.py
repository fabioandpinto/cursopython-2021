"""
Encapsulamiento: ocultar los atributos internos de la clase
solo dentro del objeto se podria modificar
tengo que crear métodos que me permitan acceder y modificar esos atributos

getter y setter
"""
class Clase:
    atri = "Eliana"
    __atri = "Fabio"
    #no es accesible o que esta oculto o privado
    def __metodo(self):
        print("hola " + self.__atri)
    #si es accesible
    def getAtri(self):
        print(self.__atri)
    def setAtri(self, nombre):
        self.__atri = nombre

cl = Clase()
cl.getAtri()
cl.setAtri("Cristobal")
cl.getAtri()