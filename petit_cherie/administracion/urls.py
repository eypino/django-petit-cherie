from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name="administracion"

urlpatterns = [

    path('recuperar_cuenta',recuperarCuenta,name='recuperarCuenta'),
    path('insercion',agregarProducto,name='agregarProducto'),
    path('modificarProducto/<int:pk>/', modificarProducto, name='modificarProducto'),
    path('eliminar/<int:pk>/', eliminarProducto, name='eliminarProducto'),
    path('administracion',administracion,name='administracion'),
]