from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *


# Create your views here.
def index(request):
    #tiendas=tienda.objects.all()
    # context={'tiendas':tiendas}
    context={}
    return render(request,'index.html', context)

def tienda (request):
    template = loader.get_template('tienda.html')
    return HttpResponse(template.render())

def carrito(request):
    context={}
    return render(request,'html/CarroDeCompras.html', context)

def tienda(request):
    context={}
    return render(request,'html/Compra.html', context)    

def login(request):
    context={}
    return render(request,'html/login.html', context)    

def registro(request):
    context={}
    return render(request,'html/paginaRegistro.html', context)    
    
def panaderia(request):
    context={}
    return render(request,'html/Panaderia.html', context)         

def pasteleria(request):
    context={}
    return render(request,'html/pasteleria.html', context)       

def tortas(request):
    context={}
    return render(request,'html/tortas.html', context)   

def quienesSomos(request):
    context={}
    return render(request,'html/QuienesSomos.html', context) 

def recuperarContrasena(request):
    context={}
    return render(request,'html/recuperarContrasena.html', context) 

def recuperarCuenta(request):
    context={}
    return render(request,'html/recuperarCuenta.html', context)

def insercion(request):
    context={}
    return render(request,'html/insercion.html', context) 

def editar(request):
    context={}
    return render(request,'html/editar.html', context)

def eliminar(request):
    context={}
    return render(request,'html/eliminar.html', context)    


def panaderia(request):
    productos=Producto.objects.all()
    context={'productos':productos}
    return render(request, 'html/Panaderia.html', context)

def pasteleria(request):
    productos=Producto.objects.all()
    context={'productos':productos}
    return render(request, 'html/pasteleria.html', context)

def tortas(request):
    productos=Producto.objects.all()
    context={'productos':productos}
    return render(request, 'html/tortas.html', context)

def administracion(request): 
    productos=Producto.objects.all()  
    context={'productos':productos}
    return render(request, 'html/administracion.html', context)    