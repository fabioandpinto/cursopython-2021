from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import Movies

from django.views.generic import (
    ListView, CreateView, )

from .forms import PeliculaForm

# Creando una nueva pelicula
class create_movie(CreateView):
    model = Movies
    template_name = 'nueva_pelicula.html'
    form_class = PeliculaForm
    success_url = reverse_lazy('lista')

# Create your views here.
# vista de lista - List View
class list_movies(ListView):
    template_name = 'catalogo.html'
    context_object_name = 'pelicula'

    def get_queryset(self):
        key_word = self.request.GET.get('nombre', '')
        _list = Movies.objects.filter(
            nombre__icontains = key_word
        )
        return _list
# vista de agregar




# vista de editar



# vista de eliminar

