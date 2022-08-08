import email
from django.shortcuts import render
from django.http import HttpResponse
from AppExpo.models import Producto, Proveedores, Marcas
from AppExpo.forms import ProductoFormulario, ProveedorFormulario, MarcaFormulario


# Create your views here.

def inicio(request):

    return render(request, "AppExpo/index.html")

def productos(request):

    productos = Producto.objects.all()

    contexto_pro = {
        "mensaje_pro1":"Nuestros productos",
        "mensaje_pro2":"Este es el listado de nuestros productos",
        "productos":productos
    }

    return render(request, "AppExpo/productos.html", contexto_pro)

def proveedores(request):

    proveedores = Proveedores.objects.all()

    contexto_prov = {
        "mensaje_prov1":"Nuestros proveedores",
        "mensaje_prov2":"Trabajamos mano a mano con nuestros proveedores para garantizar la mejor atención",
        "proveedores":proveedores
    }

    return render(request, "AppExpo/proveedores.html", contexto_prov)

def marcas(request):

    marcas = Marcas.objects.all()

    contexto_mar = {
        "mensaje_mar1":"Las marcas",
        "mensaje_mar2":"Trabajamos únicamente con las mejores marcas del mercado",
        "marcas":marcas
    }

    return render(request, "AppExpo/marcas.html", contexto_mar)

def crear_producto(request):

    if request.method == "GET":
        form_producto = ProductoFormulario()
        return render(request, "AppExpo/form_productos.html", {"form_producto":form_producto})
    else:

        form_producto = ProductoFormulario(request.POST)

        if form_producto.is_valid():

            data = form_producto.cleaned_data

            modelo = data.get("modelo")
            articulo = data.get("articulo")
            producto = Producto(modelo=modelo, articulo=articulo)

            producto.save()

            return render(request, "AppExpo/index.html")
        
        else:
            return HttpResponse("Formulario no valido")

def crear_proveedor(request):

    if request.method == "GET":
        form_proveedor = ProveedorFormulario()
        return render(request, "AppExpo/form_proveedores.html", {"form_proveedor":form_proveedor})
    else:

        form_proveedor = ProveedorFormulario(request.POST)

        if form_proveedor.is_valid():

            data = form_proveedor.cleaned_data

            razon = data.get("razon")
            email = data.get("email")
            ubicacion = data.get("ubicacion")
            proveedor = Proveedores(razon=razon, email=email, ubicacion=ubicacion)

            proveedor.save()

            return render(request, "AppExpo/index.html")
        
        else:
            return HttpResponse("Formulario no valido")

def crear_marca(request):

    if request.method == "GET":
        form_marca = MarcaFormulario()
        return render(request, "AppExpo/form_marcas.html", {"form_marca":form_marca})
    else:

        form_marca = MarcaFormulario(request.POST)

        if form_marca.is_valid():

            data = form_marca.cleaned_data

            nombre = data.get("nombre")
            nacionalidad = data.get("nacionalidad")
            marca = Marcas(nombre=nombre, nacionalidad=nacionalidad)

            marca.save()

            return render(request, "AppExpo/index.html")
        
        else:
            return HttpResponse("Formulario no valido")

def formulario_busqueda(request):
    return render(request, "AppExpo/formulario_busqueda.html")

def buscar(request):

    producto_modelo = request.GET.get("producto", None)

    if not producto_modelo:
        return HttpResponse("Completar el campo de búsqueda")

    producto_lista = Producto.objects.filter(modelo__icontains=producto_modelo)
    return render(request, "AppExpo/resultado_busqueda.html", {"productos": producto_lista})
