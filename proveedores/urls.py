from django.urls import path
from . import views

app_name = 'proveedores'

urlpatterns = [
    path('', views.listar_proveedores, name='listar_proveedores'),
    path('registrar_proveedor/', views.registrar_proveedor, name='registrar_proveedor'),
    path('ver_detalles/<int:pk>/', views.detalle_proveedor, name='detalle_proveedor'),
    path('editar_proveedor/<int:pk>/', views.editar_proveedor, name='editar_proveedor'),
    path('eliminar_proveedor/<int:pk>/', views.eliminar_proveedor, name='eliminar_proveedor')
    
]