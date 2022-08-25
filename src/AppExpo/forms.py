from django.forms import Form, IntegerField, CharField, EmailField, BooleanField, PasswordInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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

class UserCustomCreationForm(UserCreationForm):

    email = EmailField()
    password1 = CharField(label="Contraseña", widget=PasswordInput)
    password2 = CharField(label="Confirmar Contraseña", widget=PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = { "username":"", "email":"","password1":"", "password2":"  "}
        