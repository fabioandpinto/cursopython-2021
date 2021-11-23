""" formulario para crear pelicula """

from django import forms
from .models import Movies

# Formulario para peliculas
class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ('__all__')
