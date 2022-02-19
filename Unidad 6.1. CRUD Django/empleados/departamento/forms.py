from django import forms
from .models import Departamento

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ('__all__')

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Coloque el texto completo del Departamento'
                }
            )
        }
