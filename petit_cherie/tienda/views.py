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

        context = {'mensaje': 'OK, datos guardados con éxito'}
        return render(request, 'html/insercion.html', context)
'''
def eliminarProducto(request, pk):
    context={}
    try:
        mascota=Mascota.objects.get(id_mascota=pk)
        mascota.delete()
        mensaje="Ok, Datos eliminados satisfactoriamente"
        mascotas=Mascota.objects.all()
        context={'mascota':mascotas, 'mensaje':mensaje}
        return render(request, 'admin_mascota.html', context)
    except: 
        mensaje="Error, id mascota no existe"
        mascotas=Mascota.objects.all()
        context={'mascota':mascotas, 'mensaje':mensaje}
        return render(request, 'admin_mascota.html', context)
    
def encontrarProducto(request, pk):
    if pk != " ":
        mascota=Mascota.objects.get(id_mascota=pk)
        sexos=Sexo.objects.all()
        print(type(mascota.id_sexo.sexo))
        context={'mascota':mascota, 'sexo':sexos}
        if mascota:
            return render(request, 'editar_mascota.html', context)
        else: 
            context={'mensaje':'Error, id de mascota no existe'}
            return render (request, 'admin_mascota.html', context)
        
def modificarProducto(request):
    if request.method == "POST":
        idMascota=request.POST["id_mascota"]
        nombre=request.POST["nombre_mascota"]
        fecha_nac=request.POST["fechaNac"]
        raza=request.POST["razaMasc"]
        sexo=request.POST["sexo"]
        
    
        objSexo=Sexo.objects.get(id_sexo = sexo)

        mascota=Mascota()
        mascota.id_mascota=idMascota
        mascota.nombre=nombre
        mascota.fecha_nacimiento=fecha_nac
        mascota.raza=raza
        mascota.id_sexo=objSexo
        mascota.save()
        sexos=Sexo.objects.all()
        context={'mensaje':'OK, datos actualizados con éxito','sexo':sexos,'mascota':mascota}
        return render(request,'editar_mascota.html',context)
    else:
        mascota=Mascota.objects.all()
        context={'mascota':mascota}
        return render(request,'admin_mascota.html',context)
'''
def administracion(request): 
    productos=Producto.objects.all()  
    context={'productos':productos}
    return render(request, 'html/administracion.html', context)    
