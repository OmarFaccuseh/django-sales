from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'order_id', 'product', 'customer', 'unit_price', 'qty', 'subtotal', 'total', 'status')
