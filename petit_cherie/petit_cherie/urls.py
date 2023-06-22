"""
URL configuration for petit_cherie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
<<<<<<< Updated upstream
from tienda.views import index,carrito,login,tienda,registro,panaderia,pasteleria,tortas,quienesSomos,recuperarContrasena,recuperarCuenta,incercion,editar,eliminar
=======
from tienda.views import agregar_producto_carito, eliminar_producto_carito, limpiar_carrito, restar_producto_carito
from tienda.views import index,carrito,login,tienda,registro,panaderia,pasteleria,tortas,quienesSomos,recuperarContrasena,recuperarCuenta
from django.conf import settings
from django.conf.urls.static import static

from tienda.views import index,carrito,login,tienda,registro,panaderia,pasteleria,tortas,quienesSomos,recuperarContrasena,recuperarCuenta,insercion,editar,eliminar
>>>>>>> Stashed changes
	

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index,name='index'),
    path('carrito',carrito,name='carrito'),
    path('login',login,name='login'),
    path('tienda',tienda,name='tienda'),
    path('registro',registro,name='registro'),
    path('tienda/panaderia',panaderia,name='panaderia'),
    path('tienda/pasteleria',pasteleria,name='pasteleria'),
    path('tienda/tortas',tortas,name='tortas'),
    path('quienes_somos',quienesSomos,name='quienesSomos'),
    path('recuperar_contrasena',recuperarContrasena,name='recuperarContrasena'),
    path('recuperar_cuenta',recuperarCuenta,name='recuperarCuenta'),
    path('incercion',incercion,name='incercion'),
    path('editar',editar,name='editar'),
    path('eliminar',eliminar,name='eliminar'),
    path('agregar/<int:producto_id>/',agregar_producto_carito,name='add'),
    path('eliminar/<int:producto_id>/',eliminar_producto_carito,name='del'),
    path('restar/<int:producto_id>/',restar_producto_carito,name='sub'),
    path('limpiar/<int:producto_id>/',limpiar_carrito,name='cli'),
]
