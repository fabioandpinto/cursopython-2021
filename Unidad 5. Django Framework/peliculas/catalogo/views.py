from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import Movies

from django.views.generic import (
    TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView)

class Prueba(TemplateView):
    template_name = 'prueba.html'

# Vistas para hacer listado - ListView
## Listado general
# Listar por genero (que yo busque un genero y me de los que sonde ese genero)
# Busqueda

class listaNumero(ListView):
    template_name = 'lista1.html'
    queryset = list(range(1,10))
    context_object_name = 'pelicula'


class listarMovies(ListView):
    template_name = 'catalogo.html'
    model = Movies
    context_object_name = 'pelicula'

class listarGenero(ListView):
    template_name = 'peliculaGenero.html'
    model = Movies
    queryset = Movies.objects.filter(
        genero = 'Infantil'
    )
    context_object_name = 'action'

class listarGeneroUrl(ListView):
    template_name = 'peliculaGenero2.html'

    def get_queryset(self):
       gen = self.kwargs['genero']
       list = Movies.objects.filter(
           genero = gen
       )
       return list

    context_object_name = 'list'

class listaPorBusqueda(ListView):
    template_name = 'peliculaGenero2.html'
    context_object_name = 'peli'

    def get_queryset(self):
        busqueda = self.request.GET.get('genero', '')
        lista = Movies.objects.filter(
            genero=busqueda
        )
        return lista

class buscarNombre(ListView):
    template_name = 'peliculaGenero3.html'
    context_object_name = 'peli'

    def get_queryset(self):
        busqueda = self.request.GET.get('nombre', '')
        lista = Movies.objects.filter(
            nombre__contains=busqueda
        )
        return lista

class detallePeli(DetailView):
    template_name = "detalle.html"
    model = Movies
    context_object_name = 'peli'

class crearPelicula(CreateView):
    model = Movies
    template_name = 'crear.html'
    fields = ['idPeli', 'nombre', 'genero'] # Lista
    success_url = 'listado' #Path de la url

class eliminarPelicula(DeleteView):
    model = Movies
    template_name = 'delete.html'
    context_object_name = 'pelicula'
    success_url = reverse_lazy('lista') #nombre de la url

class updatePelicula(UpdateView):
    model = Movies
    template_name = 'update.html'
    fields = ('__all__')     #global
    context_object_name = 'pelicula'
    success_url = reverse_lazy('lista')