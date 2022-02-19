from django.contrib import admin
from django.urls import path, include

from . import  views

app_name = 'departamento_app'

urlpatterns = [
    path('departamento/lista', views.ListaDepartamento.as_view(), name = 'departamentos'),
    path('departamento/nuevo', views.NuevoDepartamento.as_view(), name = 'nuevo_departamento')
]
