from audioop import maxpp
from dataclasses import field
from tkinter import Widget
from django import forms
from .models import Contacto, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validators import MaxSizeFileValidator    
from django.forms import ValidationError

class ContactoForms(forms.ModelForm):
    class Meta:
        model = Contacto
        #fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]
        fields = '__all__'

        
class ProductoForm (forms.ModelForm):

    nombre = forms.CharField(min_length=3, max_length=50)
    image = forms.ImageField( required=False, validators=[MaxSizeFileValidator(max_file_size=2)])
    precio = forms.IntegerField(min_value=1, max_value=1500000)

    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]
        existe = Producto.objects.filter(nombre__iexact=nombre).exists()

        if existe:
            raise ValidationError("Este nombre ya existe")

        return nombre

    class Meta:
        model = Producto
        #fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]
        fields = '__all__'
    
        Widget = {
            "fecha_fabricacion" : forms.SelectDateWidget()
        }


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1","password2" ]