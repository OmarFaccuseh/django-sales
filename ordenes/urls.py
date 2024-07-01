from django.urls import path
from . import views

app_name = 'ordenes'

urlpatterns = [
    path('orders/', views.orders, name='orders'),
    path('order_detail/<int:order_id>/', views.order_detail, name='order_detail'),
]

