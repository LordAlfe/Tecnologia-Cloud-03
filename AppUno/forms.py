from django import forms
from AppUno.models import Formulario
from .validators import *


class Form(forms.ModelForm):
    nombre = forms.CharField(min_length=3, max_length=50, widget=forms.TextInput(
        attrs={"placeholder": "Debe contener un minimo de tres palabras"}))
    tipo = forms.ChoiceField
    descripcion = forms.Textarea()
    evidencia = forms.ImageField(required=False)

    class Meta:
        model = Formulario
        fields = ("nombre", "tipo", "descripcion", "evidencia")
