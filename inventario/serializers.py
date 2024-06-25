from rest_framework import serializers
from .models import Producto, Nota, Linea


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('id', 'nombre', 'descripcion', 'precio', 'costo', 'categoria')


class LineaSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer()

    class Meta:
        model = Linea
        fields = ('id', 'nota_id', 'producto', 'cantidad')


class NotaSerializer(serializers.ModelSerializer):
    lineas_nota = LineaSerializer(many=True, read_only=True)

    class Meta:
        model = Nota
        fields = ('id', 'code_note', 'body', 'name_customer', 'created_date', 'anotations', 'lineas_nota')