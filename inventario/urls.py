from django.urls import path
from . import views

app_name = 'inventario'

urlpatterns = [
    # product views ,
    path('', views.product_list, name='product_list'),
    path('<slug:prod>/', views.product_detail, name='product_detail'),
]

