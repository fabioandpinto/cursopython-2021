from django.db import models

# Create your models here.
class Departamento(models.Model):

    types = (
        ('O', 'Operativo'),
        ('A', 'Administrativo'),
    )

    name = models.CharField('Nombre', max_length=50, unique=True)
    type = models.CharField('Area', max_length=50, choices=types)

    def __str__(self):
        return self.name