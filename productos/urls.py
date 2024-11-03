from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path('listar_insumos', views.listar_insumos, name='listar_insumos'),
    
    path('listar_productos', views.listar_productos, name='listar_productos'),
    path('registrar_producto', views.registrar_producto, name='registrar_producto'),
    path('detalle_producto/<int:pk>', views.detalle_producto, name='detalle_producto'),
    path('editar_producto/<int:pk>', views.editar_producto, name='editar_producto'),
    path('eliminar_producto/<int:pk>', views.eliminar_producto, name='eliminar_producto'),
    path('agregar_stock/<int:pk>', views.agregar_stock, name='agregar_stock'),
    path('cambiar_precio/<int:pk>', views.cambiar_precio, name='cambiar_precio'),
]