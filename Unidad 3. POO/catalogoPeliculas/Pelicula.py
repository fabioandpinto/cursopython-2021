class Pelicula:
    def __init__(self, nombre):
        self.__nombre = nombre

    def __str__(self):
        return 'Titulo de la pelicula: ' + self.__nombre

    @property
    def nombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    