from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .models import Producto, Linea, Nota
from rest_framework import viewsets
from .serializers import ProductoSerializer, LineaSerializer, NotaSerializer
from django.core import serializers
#  from .apps import getOrders
import json

from django.contrib.auth.models import User


def product_list(request):
    response = {'productos': Producto.objects.all()}
    return render(request, 'inventario/producto/product_list.html', response)


def product_detail(request, prod):
    producto = get_object_or_404(Producto, slug=prod)
    return render(request, 'inventario/producto/product_detail.html', {'producto': producto})


# ViewSet - Proveen tanto la lista como el detalle
class ProdcutoView(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()


class LineaView(viewsets.ModelViewSet):
    serializer_class = LineaSerializer
    queryset = Linea.objects.all()


class NotaView(viewsets.ModelViewSet):
    serializer_class = NotaSerializer
    queryset = Nota.objects.all()
