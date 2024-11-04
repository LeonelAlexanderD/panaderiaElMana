from decimal import Decimal
import json
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required



from productos.models import Producto
from usuarios.models import Empleado
from ventas.models import CarritoProducto, Comprobante, Venta

# Create your views here.
@login_required
def nueva_venta(request):
    productos = Producto.objects.order_by('categoria', 'subcategoria')
    productos_dict = {}
    for producto in productos:
        if producto.categoria not in productos_dict:
            productos_dict[producto.categoria] = {}
        if producto.subcategoria not in productos_dict[producto.categoria]:
            productos_dict[producto.categoria][producto.subcategoria] = []
        productos_dict[producto.categoria][producto.subcategoria].append(producto)
        
        
    
    #creo un comprobante temporal para la sesion
    if 'comprobante_temp' not in request.session:
        request.session['comprobante_temp'] = {
            'tipo_de_venta': None,
            'forma_de_pago': None,
            'tipo_comprobante': None,
            'observacion': '',
            'items': []
        }
    
    if request.method == 'POST':
        producto_id = request.POST.get('producto_id')
        cantidad = Decimal(request.POST.get('cantidad',1))        
        producto = Producto.objects.get(id=producto_id)
        
        ##
        
        comprobante_temp = request.session['comprobante_temp']
        subtotal = producto.precio * cantidad
        
        comprobante_temp['items'].append({
            'producto_id': producto.id,
            'nombre': producto.nombre,
            'cantidad': float(cantidad),
            'precio': float(producto.precio),
            'subtotal': float(subtotal)
        })
        request.session['comprobante_temp'] = comprobante_temp
        return redirect('ventas:nueva_venta')
    
    
    total_carrito = sum(item['subtotal'] for item in request.session['comprobante_temp']['items'])
    

    
    tipo_venta_choices = dict(Comprobante.TIPO_VENTA)
    forma_pago_choices = dict(Comprobante.FORMA_DE_PAGO)
    tipo_comprobante_choices = dict(Comprobante.TIPO_COMPROBANTE)
    
    
    return render(request, 'venta/nueva_venta.html',{
        'productos':productos_dict,
        'comprobante_temp': request.session['comprobante_temp'],
        'tipo_venta_choices': json.dumps(tipo_venta_choices),
        'forma_pago_choices': json.dumps(forma_pago_choices),
        'tipo_comprobante_choices': json.dumps(tipo_comprobante_choices),
        'total_carrito': total_carrito,
        })
    
@login_required
def generar_comprobante(request):
    if request.method == 'POST':        
        tipo_venta = request.POST.get('tipo_de_venta')
        forma_pago = request.POST.get('forma_de_pago')
        tipo_comprobante = request.POST.get('tipo_comprobante')
        observacion = request.POST.get('observacion')
        
        if not all([tipo_venta, forma_pago, tipo_comprobante]):
            return redirect('ventas:nueva_venta')
        
        ## creando comprobante
        comprobante = Comprobante(
            tipo_de_venta = tipo_venta,
            forma_de_pago = forma_pago,
            tipo_comprobante = tipo_comprobante,
            total_comprobante = 0,
            observacion = observacion
        )
        comprobante.save()
        
        for item in request.session['comprobante_temp']['items']:
            producto = Producto.objects.get(id=item['producto_id'])
            cantidad = item['cantidad']
            carrito_producto = CarritoProducto.objects.create(
                comprobante = comprobante,
                producto = producto,
                cantidad = item['cantidad']                
            )
            producto.stock -= Decimal(cantidad)
            producto.save()
            
        
        empleado = Empleado.objects.get(usuario=request.user)
        venta = Venta(comprobante = comprobante, vendedor = empleado)
        venta.save()
        
        del request.session['comprobante_temp']
        
        return redirect('ventas:ver_comprobante', comprobante_id=comprobante.id)
    
    return redirect('ventas:nueva_venta')

@login_required
def eliminar_producto(request, carrito_id):
    carrito_producto = CarritoProducto.objects.get(id=carrito_id)
    carrito_producto.delete()
    return redirect('ventas:nueva_venta')

@login_required
def modificar_producto(request, carrito_id):
    carrito_producto = CarritoProducto.objects.get(id=carrito_id)
    if request.method == 'POST':
        cantidad = Decimal(request.POST.get('cantidad'))
        carrito_producto.cantidad = cantidad
        carrito_producto.save()
    return redirect('ventas:nueva_venta')




@login_required
def ver_comprobante(request, comprobante_id):
    comprobante = Comprobante.objects.get(id=comprobante_id)
    items = comprobante.items.all()
    total_comprobante = sum(item.subtotal for item in items)
    
    return render(request, 'venta/comprobante.html', {
        'comprobante': comprobante,
        'items': items,
        'total_comprobante': total_comprobante,
        })




@login_required
def detalle_venta(request, venta_id):
    venta = get_object_or_404(Venta, id=venta_id, vendedor=request.user.empleado)
    return render(request, 'detalle_venta.html', {'venta': venta})


@login_required
def listar_ventas(request):
    comprobantes = Comprobante.objects.all()
    return render(request, 'venta/lista_ventas.html', {'comprobantes': comprobantes})