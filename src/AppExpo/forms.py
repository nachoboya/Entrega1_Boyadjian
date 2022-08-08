from django.forms import Form, IntegerField, CharField, EmailField


class ProductoFormulario(Form):

    modelo = CharField()
    articulo = IntegerField()



class ProveedorFormulario(Form):

    razon = CharField()
    email = EmailField()
    ubicacion = CharField()


class MarcaFormulario(Form):

    nombre = CharField()
    nacionalidad = CharField()
