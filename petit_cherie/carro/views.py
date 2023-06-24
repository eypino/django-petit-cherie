from django.shortcuts import render, redirect
from .carro import Carro
from tienda.models import *

def agregar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id_producto=producto_id)
    carro.agregar(producto)
    return redirect("carrito")

def eliminar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id_producto=producto_id)
    carro.eliminar(producto)
    return redirect("carrito")

def restar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id_producto=producto_id)
    carro.restar_producto(producto)
    return redirect("carrito")

def limpiar_carro(request):
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect("carrito")
