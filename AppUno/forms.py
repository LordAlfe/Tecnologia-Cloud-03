from django import forms
from AppUno.models import *
from .validators import *


class Form(forms.ModelForm):
    nombre = forms.CharField(min_length=3, max_length=50, widget=forms.TextInput(
        attrs={"placeholder": "Debe contener un minimo de tres palabras"}))
    tipo = forms.ChoiceField(required=True)
    descripcion = forms.Textarea()
    evidencia = forms.ImageField(required=False)

    class Meta:
        model = Formulario
        fields = '__all__'
