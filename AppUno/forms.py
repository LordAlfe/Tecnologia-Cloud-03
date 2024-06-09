from django import forms
from AppUno.models import Formulario
from .validators import *


class Form(forms.ModelForm):
    nombre = forms.CharField(min_length=3, max_length=50, widget=forms.TextInput(
        attrs={"placeholder": "Debe contener un minimo de tres palabras"}))
    apellido = forms.CharField()
    fecha = forms.CharField(widget=forms.TextInput(
        attrs={"placeholder": "Formato: DD/MM/AAAA"}))
    tipo = forms.ChoiceField
    descripcion = forms.Textarea()
    rut = forms.CharField(widget=forms.TextInput(
        attrs={"placeholder": "Formato: XX.XXX.XXX-X"}))

    class Meta:
        model = Formulario
        fields = ("nombre", "apellido", "rut", "fecha",
                  "tipo", "descripcion")
