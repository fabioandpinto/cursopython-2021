from django.db import models

# Create your models here.
class Movies(models.Model):
    idPeli = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    genero = models.CharField(max_length=20)

    def __str__(self):
        return ""+self.nombre+" - "+self.genero