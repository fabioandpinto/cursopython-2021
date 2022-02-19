from django.contrib import admin
from django.urls import path, include

from . import  views

app_name = 'persona_app'

urlpatterns = [
    path('', views.Home.as_view(), name = 'inicio'), # Pagina de home
    path('persona/crear', views.CreatePersona.as_view(), name = 'nuevo'), #Pagina de crear
    path('persona/lista', views.ListarPersona.as_view(), name = 'lista'), #Pagina de listar
    path('persona/eliminar/<pk>', views.DeletePersona.as_view(), name = 'delete'),
    path('persona/actualizar/<pk>', views.UpdatePersona.as_view(), name='actualizar'),
    path('persona/detalle/<pk>', views.DetallePersona.as_view(), name='detalle'),
    path('persona/listarArea/<depart>', views.ListaPersonaPorArea.as_view(), name='lista_area'),
]
