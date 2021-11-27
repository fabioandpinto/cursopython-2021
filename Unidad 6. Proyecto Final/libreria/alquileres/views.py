from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView
from .models import Usuario, Libro, Alquiler


class Bienvenida(TemplateView):
    template_name = 'bienvenida.html'

class ListarLibros(ListView):
    model = Libro
    template_name = 'libros/lista_libros.html'
    context_object_name = 'libro'
