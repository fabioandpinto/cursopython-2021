from django import forms
from .models import Persona



# Model Form - Formulario para acceder al modelo
class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ('__all__')