from django.db import models

## importamos metodos de usuario
from django.contrib.auth.models import User

# Create your models here.
class Perfil(models.Model):
    """
        Nombre usuario
        contraseña
        correo
        biografia
        titulo
        url_web
    """
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    biografia = models.CharField(max_length=50, blank=True)
    titulo = models.CharField(max_length=20, blank= True )
    url_web = models.CharField(max_length=100)

    def __str__(self):
        return self.usuario.username