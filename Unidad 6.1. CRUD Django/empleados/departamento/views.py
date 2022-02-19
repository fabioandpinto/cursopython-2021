from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView

from .models import Departamento
from .forms import DepartamentoForm


class ListaDepartamento(ListView):
    """ Listamos todos los empleados """
    model = Departamento
    template_name = "departamento/lista_departamento.html"
    context_object_name = 'departamento'

class NuevoDepartamento(CreateView):
    model = Departamento
    template_name = 'departamento/nuevo_departamento.html'
    form_class = DepartamentoForm
    success_url = reverse_lazy('departamento_app:departamentos')