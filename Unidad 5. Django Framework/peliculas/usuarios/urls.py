from django.contrib import admin
from django.urls import include, path

from .views import SignUpView, Bienvenida, LogOut, Login

urlpatterns = [
    path('registro/', SignUpView.as_view(), name='registro'),
    path('index/', Bienvenida.as_view(), name='bienvenida'),
    path('salir/', LogOut.as_view(), name='salir'),
    path('entrar/', Login.as_view(), name='entrar')
]
