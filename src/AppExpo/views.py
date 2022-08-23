from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppExpo.models import Producto, Proveedores, Marcas
from AppExpo.forms import ProductoFormulario, ProveedorFormulario, MarcaFormulario
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.

def inicio(request):

    return render(request, "AppExpo/index.html")

def productos(request):

    productos = Producto.objects.all()

    if request.method == "GET":
        form_producto = ProductoFormulario()
        
        contexto_pro = {
        "mensaje_pro1":"Nuestros productos",
        "mensaje_pro2":"Este es el listado de nuestros productos",
        "productos":productos,
        "form_producto":form_producto
        }

        return render(request, "AppExpo/productos.html", contexto_pro)

    else:
        
        form_producto = ProductoFormulario(request.POST)

        if form_producto.is_valid():

            data = form_producto.cleaned_data

            modelo = data.get("modelo")
            articulo = data.get("articulo")
            stock = data.get("stock")
            producto = Producto(modelo=modelo, articulo=articulo, stock=stock)

            producto.save()

            form_producto = ProductoFormulario()

            contexto_pro = {
            "mensaje_pro1":"Nuestros productos",
            "mensaje_pro2":"Nuevo producto cargado!",
            "productos":productos,
            "form_producto":form_producto
            }

            return render(request, "AppExpo/productos.html", contexto_pro)
        else:
            return HttpResponse("Formulario no valido")



    proveedores = Proveedores.objects.all()

    if request.method == "GET":
        form_proveedor = ProveedorFormulario()
        
        contexto_prov = {
            "mensaje_prov1":"Nuestros proveedores",
            "mensaje_prov2":"Trabajamos mano a mano con nuestros proveedores para garantizar la mejor atención",
            "proveedores":proveedores,
            "form_proveedor":form_proveedor
        }

        return render(request, "AppExpo/proveedores.html", contexto_prov)
    else:
        form_proveedor = ProveedorFormulario(request.POST)

        if form_proveedor.is_valid():

            data = form_proveedor.cleaned_data

            razon = data.get("razon")
            email = data.get("email")
            ubicacion = data.get("ubicacion")
            proveedor = Proveedores(razon=razon, email=email, ubicacion=ubicacion)

            proveedor.save()

            form_proveedor = ProveedorFormulario()
            contexto_prov = {
            "mensaje_prov1":"Nuestros proveedores",
            "mensaje_prov2":"Nuevo proveedor cargado!",
            "proveedores":proveedores,
            "form_proveedor":form_proveedor
        }

            return render(request, "AppExpo/proveedores.html", contexto_prov)
        else:
            return HttpResponse("Formulario no valido")

def marcas(request):

    marcas = Marcas.objects.all()
    if request.method == "GET":
        form_marca = MarcaFormulario()

        contexto_mar = {
            "mensaje_mar1":"Las marcas",
            "mensaje_mar2":"Trabajamos únicamente con las mejores marcas del mercado",
            "marcas":marcas,
            "form_marca":form_marca
        }

        return render(request, "AppExpo/marcas.html", contexto_mar)
    else:

        form_marca = MarcaFormulario(request.POST)

        if form_marca.is_valid():

            data = form_marca.cleaned_data

            nombre = data.get("nombre")
            nacionalidad = data.get("nacionalidad")
            marca = Marcas(nombre=nombre, nacionalidad=nacionalidad)

            marca.save()

            form_marca = MarcaFormulario()
            contexto_mar = {
            "mensaje_mar1":"Las marcas",
            "mensaje_mar2":"Nueva marca cargada!",
            "marcas":marcas,
            "form_marca":form_marca
            }
            return render(request, "AppExpo/marcas.html", contexto_mar)
        else:
            return HttpResponse("Formulario no valido")

def borrar_producto(request, id_producto):

    productos = Producto.objects.all()
    form_producto = ProductoFormulario()

    try:
        producto = Producto.objects.get(id=id_producto)
        producto.delete()

        return redirect("productos")
    except:
        contexto_pro = {
        "mensaje_pro1":"Nuestros productos",
        "mensaje_pro2":"Error, no se puede borrar el producto!",
        "productos":productos,
        "form_producto":form_producto
        }

        return render(request, "AppExpo/productos.html",contexto_pro)



    proveedores = Proveedores.objects.all()
    form_proveedor = ProveedorFormulario()

    try:
        proveedor = Proveedores.objects.get(id=id_proveedor)
        proveedor.delete()

        return redirect("proveedores")
    except:
        contexto_prov = {
        "mensaje_prov1":"Nuestros proveedores",
        "mensaje_prov2":"Error, no se puede borrar el proveedor!",
        "proveedores":proveedores,
        "form_proveedor":form_proveedor
        }

        return render(request, "AppExpo/proveedores.html",contexto_prov)

def borrar_marca(request, id_marca):

    marcas = Marcas.objects.all()
    form_marca = MarcaFormulario()

    try:
        marca = Marcas.objects.get(id=id_marca)
        marca.delete()

        return redirect("marcas")
    except:
        contexto_mar = {
        "mensaje_mar1":"Nuestros marcas",
        "mensaje_mar2":"Error, no se puede borrar la marca!",
        "marcas":marcas,
        "form_marca":form_marca
        }

        return render(request, "AppExpo/marcas.html",contexto_mar)

def formulario_busqueda(request):
    return render(request, "AppExpo/formulario_busqueda.html")

def buscar(request):

    producto_modelo = request.GET.get("producto", None)

    if not producto_modelo:
        return HttpResponse("Completar el campo de búsqueda")

    producto_lista = Producto.objects.filter(modelo__icontains=producto_modelo)
    return render(request, "AppExpo/resultado_busqueda.html", {"productos": producto_lista})

def actualizar_producto(request,id_producto):

    if request.method == "GET":
        formulario = ProductoFormulario()
        contexto={
            "mensaje_pro1":"Nuestros productos",
            "mensaje_pro2":"Este es el listado de nuestros productos",
            "formulario":formulario,
        }
        return render(request, "AppExpo/producto_actualizar.html", contexto)
    else:
        formulario = ProductoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            try:
                producto = Producto.objects.get(id=id_producto)

                producto.modelo = data.get("modelo")
                producto.articulo = data.get("articulo")

                producto.save()
            except:
                return redirect("inicio")

        return redirect("productos")

class ProveedoresList(ListView):

    model = Proveedores
    template_name = "AppExpo/proveedores_list.html"

class ProveedoresDetail(DetailView):

    model = Proveedores
    template_name = "AppExpo/proveedores_detail.html"

class ProveedoresCreate(CreateView):

    model = Proveedores
    success_url = "/proveedores/"
    fields = ["razon", "email", "ubicacion"]

class ProveedoresUpdate(UpdateView):

    model = Proveedores
    success_url = "/proveedores/"
    fields = ["razon", "email", "ubicacion"]

class ProveedoresDelete(DeleteView):

    model = Proveedores
    success_url = "/proveedores/"
