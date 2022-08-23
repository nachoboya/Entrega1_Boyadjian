from django.urls import path
from AppExpo.views import *

urlpatterns = [
    path("", inicio, name='inicio'),

    path("productos/", productos, name='productos'),
    path("productos/borrar/<id_producto>", borrar_producto, name="borrar_producto"),
    path("productos/editar/<id_producto>", actualizar_producto, name="editar_producto"),
    path("busqueda/", formulario_busqueda, name="formulario_busqueda"),
    path("resultados/", buscar, name="buscar"),

    path("proveedores/", ProveedoresList.as_view(), name='proveedores'),
    path("proveedores/crear", ProveedoresCreate.as_view(), name='proveedores_creat'),
    path("proveedores/borrar/<pk>", ProveedoresDelete.as_view(), name='proveedores_delete'),
    path("proveedores/actualizar/<pk>", ProveedoresUpdate.as_view(), name='proveedores_update'),
    path("proveedores/<pk>", ProveedoresDetail.as_view(), name='proveedores_detail'),
    
    path("marcas/", marcas, name='marcas'),
    path("marcas/borrar/<id_marca>", borrar_marca, name="borrar_marca"),

    

    
]