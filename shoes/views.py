
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *


# Create your views here.

def start_index(request):
    return render(request, 'index.html')

def cargar_zapatillas(request):
    shoes_list = Shoes.objects.all()
    return render(request, 'zapatillas.html', {'shoes_list':shoes_list})

def crear_shoes(request):
    # Método para operación CRUD Crear nuevo libro
    if request.method == 'POST':
        # En caso de que no exista id quiere decir que no existe y hay que crearlo
        shoes = Shoes()
        shoes.id = request.POST.get('id')
        shoes.nombre = request.POST.get('nombre')
        shoes.descriptionShoes = request.POST.get('descripcion')
        shoes.priceShoes = request.POST.get('precio')
        shoes.imageUrl = request.POST.get('imageUrl')
        Shoes.save(shoes)
        return redirect('/shoes/zapatillas/')
    else:
        return render(request, 'crear_shoes.html')


def editar_shoes(request,id):
    if request.method == "GET":
        shoes = Shoes.objects.get(id=id)
        return render(request, 'editar_shoes.html', {'shoes': shoes})
    else:
        shoes = Shoes()
        shoes.id = id
        shoes.nombre = request.POST.get('nombre')
        shoes.descriptionShoes = request.POST.get('descripcion')
        shoes.priceShoes = request.POST.get('precio')
        shoes.imageUrl = request.POST.get('imageUrl')
        Shoes.save(shoes)
        return redirect('/shoes/zapatillas/')

def detalle_zapatilla(request, id):
    shoe = Shoes.objects.get(id=id)
    context = {'shoe':shoe}
    return render(request, 'shoes_detalle.html', context)

def borrar_shoes(request, id):
    shoes = Shoes.objects.get(id=id)
    if shoes is not None:
        Shoes.delete(shoes)
    return redirect('shoes/zapatillas')