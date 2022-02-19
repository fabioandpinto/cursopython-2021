from django.shortcuts import render

from django.views.generic import TemplateView, CreateView, ListView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy

#Importamos nuestros modelos y formularios
from .models import Persona
from .forms import PersonaForm

# Create your views here.
class Home(TemplateView):
    """ Homepage """
    template_name = 'index.html'

# CreateView - Creamos un empleado
class CreatePersona(CreateView):
    """ Creación de Empleado """
    model = Persona
    template_name = "persona/crear.html"
    form_class = PersonaForm
    success_url = reverse_lazy('persona_app:lista')

class ListarPersona(ListView):
    """ Listamos todos los empleados """
    model = Persona
    template_name = 'persona/lista_persona.html'
    context_object_name = 'empleados'
    ordering = 'first_name' #criterio de ordenacion
    paginate_by = 5

    def get_queryset(self):
        key = self.request.GET.get('nombre', '')
        _list = Persona.objects.filter(
            first_name__icontains = key
        )
        return _list

class DeletePersona(DeleteView):
    """ delete/<pk> """
    model = Persona
    template_name = 'persona/delete.html'
    success_url = reverse_lazy('persona_app:lista')

class UpdatePersona(UpdateView):
    model = Persona
    template_name = "persona/update.html"
    fields = ('__all__')
    success_url = reverse_lazy('persona_app:lista')

class DetallePersona(DetailView):
    model = Persona
    template_name = 'persona/detalle.html'

class ListaPersonaPorArea(ListView):
    template_name = 'persona/lista_persona.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        depart = self.kwargs['depart']
        _list = Persona.objects.filter(
            departament=depart
        )
        return  _list


