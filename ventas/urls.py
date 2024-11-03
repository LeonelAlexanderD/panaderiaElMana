from django.urls import path
from ventas import views

app_name = 'ventas'

urlpatterns = [
    path('vender/', views.productos_vender, name='vender'),
    # path('', views.pagar, name='comprobante'),
    # path('listar_ventas', views.listar_ventas, name='listar_ventas'),
    # path('listar_ventas/<int:pk>/', views.detalles_venta, name='detalles_venta'),
]