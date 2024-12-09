# mi_app/forms.py
from django import forms
from .models import Categoria, Autor, Libro, Cliente

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre']

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'categoria', 'autor']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email']
