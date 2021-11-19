import os
class catalogoPeliculas():
    def __init__(self, ruta):
        self.__ruta = ruta
        f = open(ruta, 'w')
        print('¡Creado catalogo!')

    def agregaPelicula(self, Pelicula):
        f = open(self.__ruta, 'w')
        f.write(Pelicula.nombre + ", ")
        print("Agregada la pelicula:" + str(Pelicula.nombre))

    def listarPeliculas(self):
        f = open(self.__ruta, 'r')
        print(f.read())

    def eliminarCatalogo(self):
        os.remove(self.__ruta)




