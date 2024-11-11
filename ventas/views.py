from decimal import Decimal
import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required



from productos.models import Producto
from usuarios.models import Empleado
from ventas.forms import ClienteForm
from ventas.models import CarritoProducto, Cliente_Mayorista, Comprobante, Venta

# Create your views here.
# 

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
    
    tipo_venta_choices = dict(Comprobante.TIPO_VENTA)
    forma_pago_choices = dict(Comprobante.FORMA_DE_PAGO)
    tipo_comprobante_choices = dict(Comprobante.TIPO_COMPROBANTE)
        
    if 'comprobante_temp' not in request.session:
        request.session['comprobante_temp'] = {
            'tipo_de_venta': None,
            'forma_de_pago': None,
            'tipo_comprobante': None,
            'observacion': '',
            'items': []
        }
    
    return render(request, 'venta/nueva_venta.html',{
        'productos': productos_dict, 
        'comprobante_temp': request.session['comprobante_temp'],
        'tipo_venta_choices': json.dumps(tipo_venta_choices),
        'forma_pago_choices': json.dumps(forma_pago_choices),
        'tipo_comprobante_choices': json.dumps(tipo_comprobante_choices),
        })

@login_required
def agregar_producto_carrito(request):
    if request.method == 'POST':
        producto_id = request.POST.get('producto_id')
        cantidad = Decimal(request.POST.get('cantidad', 1))
        producto = Producto.objects.get(id=producto_id)
        
        # Crear o actualizar el comprobante temporal en la sesión
        # if 'comprobante_temp' not in request.session:
        #     crear_comprobante_temp(request)
        #inicialmente tengo la vista crear_comprobante_temp donde creo un comprobante temporal, pero 
        #movi la logica hacia listar productos
        
        comprobante_temp = request.session['comprobante_temp']
        item_existente = next((item for item in comprobante_temp['items'] if item['producto_id'] == producto.id), None)
        
        if item_existente:
            # Si el producto ya está en el carrito, actualiza la cantidad
            item_existente['cantidad'] += float(cantidad)
            item_existente['subtotal'] = item_existente['cantidad'] * float(producto.precio)
        else:
            # Si no está en el carrito, agregarlo como nuevo
            subtotal = producto.precio * cantidad
            comprobante_temp['items'].append({
                'imagen': producto.imagen.url,
                'producto_id': producto.id,
                'nombre': producto.nombre,
                'cantidad': float(cantidad),
                'precio': float(producto.precio),
                'subtotal': float(subtotal)
            })
        
        # Actualizar la sesión
        request.session['comprobante_temp'] = comprobante_temp
        return redirect('ventas:nueva_venta') 

@login_required
def actualizar_o_eliminar_producto(request):
    if request.method == 'POST':
        producto_id = int(request.POST.get('producto_id'))
        accion = request.POST.get('accion')
        comprobante_temp = request.session.get('comprobante_temp', {})

        item = next((item for item in comprobante_temp['items'] if item['producto_id'] == producto_id), None)

        if item:
            if accion == 'actualizar':
                nueva_cantidad = int(request.POST.get('cantidad', 1))
                item['cantidad'] = nueva_cantidad  
                item['subtotal'] = nueva_cantidad * item['precio']  
            elif accion == 'eliminar':
                comprobante_temp['items'].remove(item)

            request.session['comprobante_temp'] = comprobante_temp
            request.session.modified = True
            
            total_carrito = sum(i['subtotal'] for i in comprobante_temp['items'])
            return JsonResponse({'success': True, 'total_carrito': total_carrito, 'subtotal': item['subtotal'] if accion == 'actualizar' else 0})

    return JsonResponse({'success': False}, status=400)
        

##    
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
                cantidad = cantidad
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
def ver_comprobante(request, comprobante_id):
    comprobante = Comprobante.objects.get(id=comprobante_id)
    items = comprobante.items.all()
    # total_comprobante = sum(item.subtotal for item in items)
    comprobante.actualizarTotalComprobante()
    
    return render(request, 'venta/comprobante.html', {
        'comprobante': comprobante,
        'items': items,
        # 'total_comprobante': total_comprobante,
        })




@login_required
def ver_detalles_venta(request, id):
    venta = get_object_or_404(Venta, id=id)
    empleado = venta.vendedor
    comprobante = venta.comprobante
    contexto = {
        'empleado': empleado,
        'comprobante': comprobante,
        'items': comprobante.items.all(),
    }
    return render(request, 'venta/detalles_venta.html', contexto)


@login_required
def listar_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'venta/lista_ventas.html', {'ventas': ventas})


@login_required
def registrar_cliente(request):   
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ventas:listar_clientes')
    else:
        form = ClienteForm()
    return render(request, 'gestion/lista_clientes.html', {'form':form})

@login_required
def listar_clientes(request):        
    clientes = Cliente_Mayorista.objects.all()
    form = ClienteForm()
    print(clientes)
    return render(request,'gestion/lista_clientes.html', {'clientes': clientes, 'form':form})