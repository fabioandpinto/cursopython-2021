from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, FormView, CreateView

from django.views.generic.edit import FormView

from django.contrib.auth.views import LoginView, LogoutView
from .models import Usuario, Libro, Alquiler

from .forms import RegistroForm, UserForm , UsuarioForm, LoginForm


class Bienvenida(TemplateView):
    template_name = 'bienvenida.html'

class ListarLibros(ListView):
    model = Libro
    template_name = 'libros/lista_libros.html'
    context_object_name = 'libro'

# Vistas de usuario
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('inicio')
    else:
        form = RegistroForm(request.POST)
    return render(request, 'usuarios/registro.html', {'form':form})


def perfil_de_usuario(request):
    if request.method == 'POST':
        form_1 = UserForm(request.POST, instance = request.user)
        if form_1.is_valid():
            form_1.save()
            return redirect('bienvenida')

    else:
        form_1 = UserForm(instance = request.user)

    context = {
        'form1' : form_1,
    }
    return render(request, 'usuarios/perfil.html', context)

class LoginUser(LoginView):
    pass

class Logout(LogoutView):
    pass

class MisLibros(ListView):
    template_name = 'libros/mislibros.html'

    def get_queryset(self):
        gen = self.kwargs['username']
        list = Libro.objects.filter(
            usuario = gen
        )
        return list

class CreateAlquiler(CreateView):
    pass
