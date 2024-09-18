from django.urls import path, include
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('accounts/', include("django.contrib.auth.urls")),
    path('register/', views.register, name='register'),
    path('config/', views.config, name='config'),
    path('tabla/', views.tabla, name='tabla'),
    path('graficas/', views.graficas, name='graficas'),
    path('eliminar_instrumento/<int:pk>', views.eliminarInstrumento, name='eliminar_instrumento'),

]

''' 
urls for accounts/              
login
logout
password_change
password_change/done
password_reset
password_reset/done
reset/<uidb64>/<token>
reset/done
'''