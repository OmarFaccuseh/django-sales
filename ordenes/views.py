from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .models import Order
from rest_framework import viewsets
from .serializers import OrderSerializer
from django.core import serializers
from .apps import getOrders
import json


@csrf_exempt
def orders(request):
    # Get updated orders
    status_update = getOrders()
    orders = Order.objects.all().order_by('-date')[:99]
    qs_json = serializers.serialize('json', orders)
    data = json.dumps({
        'orders': qs_json,
        'status': status_update
    })
    serialize_resp = HttpResponse(data, content_type='application/json')
    return serialize_resp


# param can also get with:  request.GET.get("order_id")
@csrf_exempt
def order_detail(request, order_id):
    order = Order.objects.filter(order_id=order_id)
    qs_json = serializers.serialize('json', order)
    serialize_resp = HttpResponse(qs_json, content_type='application/json')
    return serialize_resp
