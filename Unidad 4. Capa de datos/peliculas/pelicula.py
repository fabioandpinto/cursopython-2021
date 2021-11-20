class Pelicula:
    def __init__(self, name, director):
        self.name = name
        self.director = director

    def __str__(self):
        return print('Pelicula: '+self.name+ ' Director: ' +self.director)
