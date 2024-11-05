from django.urls import path
from ventas import views

app_name = 'ventas'

urlpatterns = [
    # path('', views.productos_vender, name='vender'),
    # path('agregar_al_carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    # path('actualizar_carrito/<int:item_id>/', views.actualizar_carrito, name='actualizar_carrito'),
    # path('eliminar_del_carrito/<int:item_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    # path('generar_comprobante/', views.generar_comprobante, name='generar_comprobante'),
    path('nueva_venta/', views.nueva_venta, name='nueva_venta'), 
    path('generar_comprobante/', views.generar_comprobante, name='generar_comprobante'),
    path('ver_comprobante/<int:comprobante_id>', views.ver_comprobante, name='ver_comprobante'),
    path('listar_ventas', views.listar_ventas, name='listar_ventas'),
    path('eliminar_producto', views.eliminar_producto, name='eliminar_producto'),

]