from django.forms import Form, IntegerField, CharField, EmailField, BooleanField


class ProductoFormulario(Form):

    modelo = CharField()
    articulo = IntegerField()
    stock = BooleanField()



class ProveedorFormulario(Form):

    razon = CharField()
    email = EmailField()
    ubicacion = CharField()


class MarcaFormulario(Form):

    nombre = CharField()
    nacionalidad = CharField()
