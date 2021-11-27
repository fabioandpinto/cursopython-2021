from django.contrib import admin

from .models import Libro, Usuario, Alquiler

# Register your models here.
admin.site.register(Libro)
admin.site.register(Usuario)
admin.site.register(Alquiler)

