from django.urls import path
from ventas import views

app_name = 'ventas'

urlpatterns = [
    path('nueva_venta/', views.nueva_venta, name='nueva_venta'), 
    path('generar_comprobante/', views.generar_comprobante, name='generar_comprobante'),
    path('ver_comprobante/<int:comprobante_id>', views.ver_comprobante, name='ver_comprobante'),
    path('listar_ventas', views.listar_ventas, name='listar_ventas'),
    path('agregar_producto_carrito', views.agregar_producto_carrito, name='agregar_producto_carrito'),
    path('actualizar_o_eliminar_producto', views.actualizar_o_eliminar_producto, name='actualizar_o_eliminar_producto'),
    path('ver_detalles_venta/<int:id>', views.ver_detalles_venta, name='ver_detalles_venta'),
    
    path('listar_clientes/', views.listar_clientes, name='listar_clientes'),
    path('registrar_cliente', views.registrar_cliente, name='registrar_cliente'),
    
    path('informes', views.informes, name='informes'),
    path('productos_mas_vendidos', views.productos_mas_vendidos, name='productos_mas_vendidos'),
    path('exportar_csv', views.exportar_csv, name='exportar_csv'),
    path('exportar_excel', views.exportar_excel, name='exportar_excel'),
    path('exportar_pdf', views.exportar_pdf, name='exportar_pdf'),
    
    path('insumos_faltantes', views.insumos_faltantes, name='insumos_faltantes'),
    path('exportar_materia_faltante_pdf', views.exportar_materia_faltante_pdf, name='exportar_materia_faltante_pdf'),
    path('exportar_materia_faltante_csv', views.exportar_materia_faltante_csv, name='exportar_materia_faltante_csv'),
    path('exportar_materia_faltante_xlsx', views.exportar_materia_faltante_xlsx, name='exportar_materia_faltante_xlsx'),
]