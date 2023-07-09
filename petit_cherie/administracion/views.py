from django.shortcuts import render
from tienda.models import *


def insercion(request):
    context={}
    return render(request,'html/insercion.html', context) 

def editar(request):
    context={}
    return render(request,'html/editar.html', context)

def eliminar(request):
    context={}
    return render(request,'html/eliminar.html', context)    


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

def modificarProducto(request, pk):
    if request.method == "POST":
        idProducto = request.POST.get("id_producto")
        nombreProducto = request.POST.get("Nombre_producto")
        descripcionProducto = request.POST.get("Descripcion_producto")
        precioProducto = request.POST.get("Precio")
        tipoProductoID = request.POST.get("Seccion")
        imagen = request.FILES.get("formFile") 

        objtipoProducto = TipoProducto.objects.get(id_tipo_producto=tipoProductoID)

        try:
            producto = Producto.objects.get(id_producto=idProducto)
        except Producto.DoesNotExist:
            context = {'mensaje': 'Error, el ID del producto no existe'}
            return render(request, 'html/editar.html', context)

        producto.nombre_producto = nombreProducto
        producto.descripcion_prod = descripcionProducto
        producto.valor_prod = precioProducto
        producto.id_tipo_producto = objtipoProducto
        if imagen:
            producto.imagen_prod = imagen
        producto.save()

        context = {
            'mensaje': 'OK, datos actualizados con éxito',
            'tipoProducto': producto.id_tipo_producto,
            'producto': producto
        }
        return render(request, 'html/editar.html', context)
    else:
        if pk:
            try:
                producto = Producto.objects.get(id_producto=pk)
                tipoProductos = TipoProducto.objects.all()
                context = {'producto': producto, 'tipo_producto': tipoProductos}
                return render(request, 'html/editar.html', context)
            except Producto.DoesNotExist:
                context = {'mensaje': 'Error, el ID del producto no existe'}
                return render(request, 'html/editar.html', context)
        else:
            context = {'mensaje': 'Error, el ID del producto no existe'}
            return render(request, 'html/editar.html', context)

def administracion(request): 
    productos=Producto.objects.all()  
    context={'productos':productos}
    return render(request, 'html/administracion.html', context)    


# Create your views here.
