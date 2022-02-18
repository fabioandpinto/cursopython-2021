from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, User

# import nuestro modelo
from .models import Usuario

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm():
    class Meta:
        model = User
        fields = ['username', 'password1']

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['cedula', 'telefono']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username']



