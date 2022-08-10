from django.db import models

# Create your models here.

class Producto(models.Model):
    idproducto = models.CharField(primary_key=True,max_length=6)
    nombre = models.TextField()
    codigo = models.IntegerField()
    preciocompra = models.TextField()
    precioventa = models.TextField()
    cantidad = models.IntegerField()
    estado = models.TextField()


class Provedor(models.Model):
    idprovedor = models.CharField(primary_key=True,max_length=6)
    razonsocial = models.TextField()
    ruc = models.TextField()
    direccion = models.TextField()
    telefono= models.TextField()
    representantelegal = models.TextField()
    estado = models.TextField()