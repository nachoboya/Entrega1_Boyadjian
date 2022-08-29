from django.contrib import admin
from AppExpo.models import Avatar, Producto, Proveedores, Marcas

# Register your models here.

admin.site.register(Producto)
admin.site.register(Proveedores)
admin.site.register(Marcas)
admin.site.register(Avatar)