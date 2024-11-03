from django.shortcuts import render

from productos.models import Producto
from ventas.models import Comprobante

# Create your views here.
def productos_vender(request):
    productos = Producto.objects.all()
    productos_organizados = {}
    
    for producto in productos:
        categoria = producto.categoria
        subcategoria = producto.tipo
        
        if categoria not in productos_organizados:
            productos_organizados[categoria] = {}
        
        if subcategoria not in productos_organizados:
            productos_organizados[categoria][subcategoria] = {}
            
        productos_organizados[categoria][subcategoria].append(producto)
    
    contexto = {
        'productos': productos_organizados
    }
        
    return render(request, 'venta/nueva_venta.html', contexto)


def listar_ventas(request):
    comprobantes = Comprobante.object.all()
    return render(request, 'ventas/lista_ventas.html', {'comprobantes': comprobantes})