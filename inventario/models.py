from django.db import models
from django.urls import reverse
from datetime import datetime, timezone
from model_utils import Choices


class Categoria(models.Model):
    nombre = models.CharField(max_length=250)


class Producto(models.Model):
    nombre = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    descripcion = models.CharField(max_length=250)
    sku = models.CharField(max_length=250, default='0')
    costo = models.FloatField()
    precio = models.FloatField()
    margen = models.FloatField(default='0')
    existencia = models.IntegerField(default='0')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    categoria = models.ForeignKey(Categoria, related_name='productos_cat', on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('inventario:product_detail', args=[self.slug])


class Nota(models.Model):
    code_note = models.CharField(max_length=100)  # venta id ML
    body = models.TextField(max_length=2000)   # actualmente no se usa
    name_customer = models.CharField(max_length=250)
    name_recibe = models.CharField(max_length=250, default='')
    created_date = models.DateTimeField(auto_now_add=True)
    anotations = models.CharField(max_length=250)

    @property
    def total(self):
        sum = 0
        for linea in self.lineas_nota:
            sum += linea.total
        return sum


class Linea(models.Model):
    nota_id = models.ForeignKey(Nota, related_name='lineas_nota', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)

    @property
    def total(self):
        return self.cantidad * self.producto.precio





