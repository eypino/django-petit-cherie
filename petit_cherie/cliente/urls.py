
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from tienda.views import *
from carro.views import *
from cliente.views import *
	

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index,name='index'),
    path('carrito',carrito,name='carrito'),
    path('login',login_view,name='login'),
    path('tienda',tienda,name='tienda'),
    path('registro',register,name='registro'),
    path('tienda/panaderia',panaderia,name='panaderia'),
    path('tienda/pasteleria',pasteleria,name='pasteleria'),
    path('tienda/tortas',tortas,name='tortas'),
    path('quienes_somos',quienesSomos,name='quienesSomos'),
    path('recuperar_contrasena',recuperarContrasena,name='recuperarContrasena'),
    path('recuperar_cuenta',recuperarCuenta,name='recuperarCuenta'),
    path('insercion',agregarProducto,name='agregarProducto'),
    path('modificarProducto/<int:pk>/', modificarProducto, name='modificarProducto'),
    path('eliminar/<int:pk>/', eliminarProducto, name='eliminarProducto'),
    path('administracion',administracion,name='administracion'),
    path('carro/', include('carro.urls')),
    path('logout/',exit,name='exit'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
