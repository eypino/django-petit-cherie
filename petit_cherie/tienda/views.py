from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


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
