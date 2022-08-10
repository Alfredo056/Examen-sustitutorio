from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from requests import request 
from miapp.models import Producto

# Create your views here.

layout = """
                <h1> TA (LP3) |GGV <h1>
                <hr>
          """


def saludo(request):

    return render(request, 'saludo.html', {
        'titulo': 'saludo',
        'saludo': 'Listado de proveedores'

    })

def saludo2(request):

    return render(request, 'Producto.html', {
        'titulo': 'saludo',
        'saludo': 'Listado de proveedors'
    })

def crear_pro(request):

    return render(request, 'crear_proveedor.html', {
        'titulo': 'saludo',
        'saludo': 'Listado de proveedors'
    })

def agre_pro(request):

    return render(request, 'crear_producto.html', {
        'titulo': 'saludo',
        'saludo': 'Listado de proveedors'
    })

