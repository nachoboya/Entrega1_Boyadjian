from django.urls import path
from AppExpo.views import *

urlpatterns = [
    path("", inicio, name='inicio'),
    path("productos/", productos, name='productos'),
    path("proveedores/", proveedores, name='proveedores'),
    path("marcas/", marcas, name='marcas'),
    path("producto/crear",crear_producto, name='producto_crear'),
    path("proveedor/crear",crear_proveedor, name='proveedor_crear'),
    path("marca/crear",crear_marca, name='marca_crear'),
    path("busqueda/", formulario_busqueda, name="formulario_busqueda"),
    path("resultados/", buscar, name="buscar"),
]