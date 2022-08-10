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
