from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path('listar_insumos', views.listar_insumos, name='listar_insumos'),
    path('listar_productos', views.listar_productos, name='listar_productos'),
    path('registrar_producto', views.registrar_producto, name='registrar_producto'),
]