from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from .models import Perfil
from django.contrib.auth.models import User

from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LogoutView, LoginView

from .forms import SignUpForm

# Sign Up - registro
class SignUpView(CreateView):
    model = Perfil
    form_class = SignUpForm

    def form_valid(self, form):
    # con esta funcion va a validar
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username = usuario, password = password)
        login(self.request, usuario)
        return redirect('bienvenida')

class Bienvenida(TemplateView):
    template_name = 'usuarios/bienvenida.html'

class LogOut(LogoutView):
    pass

class Login(LoginView):
    pass
# Sign In - inicio de sesion