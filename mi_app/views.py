from django.shortcuts import render, redirect
from .forms import CategoriaForm, AutorForm, LibroForm, ClienteForm
from .models import Libro
from django.http import HttpResponse

def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_categoria')
    else:
        form = CategoriaForm()
    return render(request, 'mi_app/agregar_categoria.html', {'form': form})

def agregar_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_autor')
    else:
        form = AutorForm()
    return render(request, 'mi_app/agregar_autor.html', {'form': form})

def agregar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_libro')
    else:
        form = LibroForm()
    return render(request, 'mi_app/agregar_libro.html', {'form': form})

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_cliente')
    else:
        form = ClienteForm()
    return render(request, 'mi_app/agregar_cliente.html', {'form': form})

def buscar_libro(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')
        libros = Libro.objects.filter(titulo__icontains=query)
        return render(request, 'mi_app/buscar_libro.html', {'libros': libros, 'query': query})
    
def index(request):
    return HttpResponse("¡Bienvenido a la Libreria!")
