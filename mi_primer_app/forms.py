from django import forms
from .models import Receta, Paciente

# class PacienteForm(forms.Form):
#     nombre = forms.CharField()
#     apellido = forms.CharField()
#     edad = forms.IntegerField(min_value=0)
#     fecha_nacimiento = forms.DateField(
#         widget=forms.DateInput(attrs={'type':'date'}))
#     enfermedad = forms.CharField(required=False, max_length=100)

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['nombre', 'ingredientes', 'elaboracion']

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido', 'edad', 'fecha_nacimiento', 'enfermedad']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }   