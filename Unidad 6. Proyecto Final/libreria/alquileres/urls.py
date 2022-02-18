from django.contrib import admin
from django.urls import path, include

from .views import Bienvenida, ListarLibros, registro, perfil_de_usuario, LoginUser, Logout, MisLibros


urlpatterns = [
    path('', Bienvenida.as_view(), name = 'inicio'),
    path('libros/', ListarLibros.as_view(), name = 'libros'),
    path('ingfa', MisLibros.as_view(), name = 'mislibros'),
    ## Usuarios
    path('usuario/registro', registro, name = 'registro'),
    path('usuario/perfil', perfil_de_usuario, name = 'perfil'),
    path('usuario/login', LoginUser.as_view(), name = 'login'),
    path('usuario/logout', Logout.as_view(), name = 'salir')
]
