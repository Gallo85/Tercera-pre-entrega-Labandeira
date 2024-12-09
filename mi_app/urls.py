from django.urls import path
from . import views  

urlpatterns = [
    path('', views.index, name='index'), 
    path('agregar_categoria/', views.agregar_categoria, name='agregar_categoria'),
    path('agregar_autor/', views.agregar_autor, name='agregar_autor'),
    path('agregar_libro/', views.agregar_libro, name='agregar_libro'),
    path('agregar_cliente/', views.agregar_cliente, name='agregar_cliente'),
    path('buscar_libro/', views.buscar_libro, name='buscar_libro'),
    ]