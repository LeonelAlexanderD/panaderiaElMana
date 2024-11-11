from django.urls import path
from . import views

app_name = 'proveedores'

urlpatterns = [
    path('', views.listar_proveedores, name='listar_proveedores'),
    path('registrar_proveedor/', views.registrar_proveedor, name='registrar_proveedor'),
    path('ver_detalles/<int:pk>/', views.detalle_proveedor, name='detalle_proveedor'),
    path('editar_proveedor/<int:pk>/', views.editar_proveedor, name='editar_proveedor'),
    path('eliminar_proveedor/<int:pk>/', views.eliminar_proveedor, name='eliminar_proveedor'),
    
    path('listar_pedidos', views.listar_pedidos, name='listar_pedidos'),
    path('detalle_pedido/<int:id>', views.detalle_pedido, name='detalle_pedido'),
    path('nuevo_pedido/', views.nuevo_pedido, name='nuevo_pedido'),
    path('obtener_insumos/<int:proveedor_id>', views.obtener_insumos, name='obtener_insumos'),
    path('cancelar_pedido/<int:id>', views.cancelar_pedido, name='cancelar_pedido'),
    
    path('recepcion_pedido/<int:id>', views.recepcion_pedido, name='recepcion_pedido'),
    path('listar_recepciones/', views.listar_recepciones, name='listar_recepciones'),
    path('detalle_recepcion/<int:id>', views.detalle_recepcion, name='detalle_recepcion'),

    
]