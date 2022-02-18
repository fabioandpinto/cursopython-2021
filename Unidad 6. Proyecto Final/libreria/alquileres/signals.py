from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import Usuario


@receiver(post_save, sender = User )
def crear_usuario(sender, instance, created, **kwargs):
    if created:
        Usuario.objects.create(usuario=instance)

@receiver(post_save, sender = User )
def crear_perfil(sender, instance, **kwargs):
    instance.usuario.save()