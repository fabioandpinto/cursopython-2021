from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

"""
    Modelo User - el propio de django 
    Modelo Usuario - propio de la aplicación 
    Extender el modelo 
    Usuarios - Tipo usuario - Perfil 
    
    AbstractUserModel 
    Signals 
    
    
    
"""
class Libro(models.Model):
    idLibro = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre + ' - ' + self.autor

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'

# User : Modelo django
# Usuario : modelo nuestro
class Usuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    cedula = models.IntegerField(blank=True, null=True)
    telefono = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.usuario.username

class Alquiler(models.Model):
    idAlquiler = models.IntegerField(unique=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_inicio = models.DateField(auto_now_add = True)
    fecha_fin = models.DateField(blank=True)
    costo = models.DecimalField(blank=True, decimal_places=2, max_digits=10)

    def __str__(self):
        return str(self.usuario.cedula) + ' / ' + self.libro.nombre + ' / ' + str(self.fecha_inicio)

    class Meta:
        verbose_name = 'Alquiler'
        verbose_name_plural = 'Alquileres'
