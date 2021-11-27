from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import pre_save

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

class Usuario(models.Model):
    idUsuario = models.IntegerField(unique=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.IntegerField(blank=True)

    def __str__(self):
        return self.usuario.username

class Alquiler(models.Model):
    idAlquiler = models.IntegerField(unique=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_inicio = models.DateField(auto_now_add = True)
    fecha_fin = models.DateField(blank=False)
    costo = models.DecimalField(blank=False, decimal_places=2, max_digits=10)

    def __str__(self):
        return str(self.usuario.idUsuario) + ' / ' + self.libro.nombre + ' / ' + str(self.fecha_inicio)

    class Meta:
        verbose_name = 'Alquiler'
        verbose_name_plural = 'Alquileres'
