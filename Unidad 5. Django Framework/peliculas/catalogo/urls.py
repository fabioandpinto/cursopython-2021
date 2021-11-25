from django.urls import path

from . import views

urlpatterns = [
    path('prueba', views.Prueba.as_view(), name = 'prueba'), #localhost/catalogo/prueba
    path('listado', views.listarMovies.as_view(), name = 'lista'),
    path('action', views.listarGenero.as_view(), name = 'action'),
    path('listaporgenero', views.listaPorBusqueda.as_view(), name = 'busqueda'),
    path('buscarnombre', views.buscarNombre.as_view(), name = 'busqueda'),
    path('detalle/<pk>', views.detallePeli.as_view(), name = 'detalle'),
    path('crear', views.crearPelicula.as_view(), name = 'crear'),
    path('delete/<pk>', views.eliminarPelicula.as_view(), name = 'eliminar'),
    path('update/<pk>', views.updatePelicula.as_view(), name = 'actualizar')
]
