from django.db import models

# Create your models here.

class Producto(models.Model):

    modelo = models.CharField(max_length=40)
    articulo = models.IntegerField()

    def __str__(self):
        return f"{self.modelo} - {self.articulo}"

class Proveedores(models.Model):
    razon = models.CharField(max_length=30)
    email = models.EmailField()
    ubicacion = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.razon}"

class Marcas(models.Model):
    nombre = models.CharField(max_length=30)
    nacionalidad = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nombre}"