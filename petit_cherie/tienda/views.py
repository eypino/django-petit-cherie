from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.shortcuts import *


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


def agregarProducto(request):
    if request.method != 'POST':
        tipoProductos = TipoProducto.objects.all()
        print(tipoProductos)
        context = {'tipoProductos': tipoProductos}  
        return render(request, 'html/insercion.html', context)
    else:
        nombreProducto = request.POST.get("Nombre_producto")
        descripcionProducto = request.POST.get("Descripcion_producto")
        precioProducto = request.POST.get("Precio")
        tipoProductoID = request.POST.get("Seccion")
        imagen = request.FILES.get("formFile") 

        objtipoProducto = TipoProducto.objects.get(id_tipo_producto=tipoProductoID)

        producto = Producto.objects.create(
            nombre_producto=nombreProducto,
            descripcion_prod=descripcionProducto,
            valor_prod=precioProducto,
            imagen_prod=imagen,
            id_tipo_producto=objtipoProducto
        )
        
        producto.save()
        tipoProductos = TipoProducto.objects.all()
        context = {'mensaje': 'OK, datos guardados con éxito'}
        return render(request, 'html/insercion.html', context)
    

def eliminarProducto(request, pk):
    context={}
    try:
        producto=Producto.objects.get(id_producto=pk)
        producto.delete()
        mensaje="Ok, Producto eliminado satisfactoriamente"
        productos=Producto.objects.all()
        context={'productos':productos, 'mensaje':mensaje}
        return render(request, 'html/administracion.html', context)
    except: 
        mensaje="Error, id producto no existe"
        productos=Producto.objects.all()
        context={'productos':productos, 'mensaje':mensaje}
        return render(request, 'html/administracion.html', context)

def encontrarProducto(request, pk):
    if pk != " ":
        producto = Producto.objects.get(id_producto=pk)
        tipoProductos = TipoProducto.objects.all()
        context = {'producto': producto, 'tipo_producto': tipoProductos}
        if producto:
            return render(request, 'html/editar.html', context)
        else:
            context = {'mensaje': 'Error, el ID del producto no existe'}
            return render(request, 'html/editar.html', context)

def modificarProducto(request):
    if request.method == "POST":
        idProducto = request.POST.get("id_producto")
        nombreProducto = request.POST.get("Nombre_producto")
        descripcionProducto = request.POST.get("Descripcion_producto")
        precioProducto = request.POST.get("Precio")
        tipoProductoID = request.POST.get("Seccion")
        imagen = request.FILES.get("formFile")

        objTipoProducto = TipoProducto.objects.get(id_tipo_producto=tipoProductoID)

        producto = Producto.objects.get(id_producto=idProducto)
        producto.nombre_producto = nombreProducto
        producto.descripcion_prod = descripcionProducto
        producto.valor_prod = precioProducto
        producto.id_tipo_producto = objTipoProducto
        producto.imagen_prod = imagen
        producto.save()

        context = {'mensaje': 'OK, datos actualizados con éxito', 'tipoProducto': tipoProductoID, 'producto': producto}
        return render(request, 'html/editar.html', context)
    else:
        producto = Producto.objects.all()
        context = {'producto': producto}
        return render(request, 'html/editar.html', context)



def administracion(request): 
    productos=Producto.objects.all()  
    context={'productos':productos}
    return render(request, 'html/administracion.html', context)    
