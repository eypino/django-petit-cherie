from django.urls import path
from .import views
from .views import *


app_name="carro"

urlpatterns = [
    path("agregarCarrito/<int:producto_id>/",agregar_producto, name="agregarCarrito" ),
    path("eliminarCarrito/<int:producto_id>/",eliminar_producto,name="eliminarCarrito"),
    path("restarCarrito/<int:producto_id>/", restar_producto, name="restarCarrito"),
    path("limpiarCarrito", limpiar_carro, name="limpiarCarrito"),
]