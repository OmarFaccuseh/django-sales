from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from inventario import views
from sales import settings

router = routers.DefaultRouter()
router.register(r'productos', views.ProdcutoView, 'producto')
router.register(r'lineas', views.LineaView, 'linea')
router.register(r'notas', views.NotaView, 'nota')
router.register(r'orders', views.OrderView, 'order')  #
# router.register(r'orders/(?P<order_id>\d+)', views.OrderView, 'order_detail')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventario/', include('inventario.urls', namespace='invetario')),
    path('ordenes/', include('ordenes.urls', namespace='ordenes')),
    path('api/', include(router.urls)),
]

#  urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


