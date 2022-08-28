from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppExpo.models import Producto, Proveedores, Marcas, Avatar
from AppExpo.forms import ProductoFormulario, ProveedorFormulario, MarcaFormulario, UserEditForm, AvatarForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

#Auth imports
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

from AppExpo.forms import UserCustomCreationForm

#Permisos de usuario
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.

def inicio(request):

    avatar = Avatar.objects.filter(usuario=request.user).first()

    return render(request, "AppExpo/index.html", {"imagen":avatar.imagen.url})

@login_required 
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

class ProveedoresList(LoginRequiredMixin, ListView):

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

def iniciar_sesion(request):
    if request.method == "GET":
        formulario = AuthenticationForm()

        contexto = {
            "form" : formulario
        }
        
        return render(request ,"AppExpo/login.html" , contexto)
    else:
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            usuario = authenticate(username=data.get("username"), password=data.get("password"))

            if usuario is not None:
                login(request, usuario)
                return redirect("inicio")
            else:
                contexto= {
                    "error": "Credenciales no válidas",
                    "form": formulario
                }
                return render(request ,"AppExpo/login.html" , contexto)
        else:
            contexto= {
                    "error": "Formulario no válido",
                    "form": formulario
                }
            return render(request ,"AppExpo/login.html" , contexto)


def registrar_usuario(request):
    if request.method == "GET":
        formulario = UserCustomCreationForm()
        return render(request, "AppExpo/registro.html", {"form":formulario})

    else:
        formulario = UserCustomCreationForm(request.POST)

        if formulario.is_valid():
            formulario.save()

            return redirect("inicio")
        else: 
            return render(request, "AppExpo/registro.html", {"form":formulario, "error": "Formulario no válido"})


@login_required
def editar_usuario(request):

    if request.method == "GET":
        form = UserEditForm(initial={"email":request.user.email,"first_name":request.user.first_name, "last_name":request.user.last_name})
        return render(request, "AppExpo/update_user.html",{"form": form})
    else:
        form = UserEditForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            usuario = request.user

            usuario.email = data["email"]
            usuario.password1 = data["password1"]
            usuario.password2 = data["password2"]
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]

            usuario.save()
            return redirect("inicio")
        return render(request, "AppExpo/update_user.html",{"form": form})

@login_required
def agregar_avatar(request):

    if request.method == "GET":
        form = AvatarForm()
        contexto = {"form":form}
        return render(request, "AppExpo/agregar_avatar.html", contexto)
    else:
        form = AvatarForm(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data

            usuario = User.objects.filer(username=request.user.username).first()
            avatar = Avatar(usuario=usuario, imagen=data["imagen"])

            avatar.save()
            