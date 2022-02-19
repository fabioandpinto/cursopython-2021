from django.db import models
import departamento.models as model

# Create your models here.
class Persona(models.Model):
    """ Modelo para la tabla empleado """

    level = (
        ('Directivo', 'Directivo'),
        ('Asesor', 'Asesor'),
        ('Operativo', 'Operativo'),
        ('Asistencial', 'Asistencial'),
        ('Tecnico', 'Tecnico')
    )

    id = models.IntegerField(unique=True, primary_key=True)
    departament = models.ForeignKey(model.Departamento, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    edad = models.IntegerField(blank=True, default=1)
    position = models.CharField(choices=level, max_length=50)


    def __str__(self):
        return self.first_name + ' ' + self.last_name
