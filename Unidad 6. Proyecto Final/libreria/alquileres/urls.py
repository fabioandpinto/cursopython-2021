from django.contrib import admin
from django.urls import path, include

from .views import Bienvenida, ListarLibros

urlpatterns = [
    path('', Bienvenida.as_view(), name = 'inicio'),
    path('libros/', ListarLibros.as_view(), name = 'libros')
]
