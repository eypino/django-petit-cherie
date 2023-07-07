from django.contrib import admin
from .models import *




admin.site.register(Producto)
admin.site.register(Compra)
admin.site.register(DetalleCompra)
admin.site.register(TipoProducto)

