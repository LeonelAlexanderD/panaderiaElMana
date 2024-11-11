
import json
from django.contrib import messages
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404 
from productos.models import Insumo
from proveedores.forms import ItemRecepcionForm, ProveedorForm, RecepcionForm
from proveedores.models import Item_Pedido, Item_Recepcion, Pedido, Proveedor, Recepcion
from django.contrib.auth.decorators import login_required
from django.db import transaction

from usuarios.decorators import perfil_administrador, perfil_gerente_o_superior
from usuarios.models import Empleado

# Create your views here.
@login_required(login_url='usuarios:login')
def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    insumos = Insumo.objects.all()
    form = ProveedorForm()
    return render(request, 'proveedores\lista_proveedores.html', {
        'proveedores': proveedores,
        'insumos': insumos,
        'form': form,
        })


@perfil_gerente_o_superior
def registrar_proveedor(request):
    if request.method == "POST":
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proveedores:listar_proveedores')
        return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = ProveedorForm()
    return render(request, 'proveedores/lista_proveedores.html', {'form':form})

@login_required(login_url='usuarios:login')
def detalle_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    insumos = proveedor.insumos.all()
    return render(request, 'proveedores/detalle_proveedor.html',{'proveedor':proveedor, 'insumos': insumos})


@perfil_gerente_o_superior
def editar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('proveedores:detalle_proveedor', pk=proveedor.id)
    else:
        form = ProveedorForm(instance=proveedor)
    
    return render(request, 'proveedores/detalle_proveedor.html', {'form': form, 'proveedor': proveedor})

@perfil_gerente_o_superior
def eliminar_proveedor(request, id):
    if request.method == 'POST':
        proveedor = get_object_or_404(Proveedor, id=id)
        proveedor.delete()
        print('se tuvo que haber borrado')
        return redirect('proveedores:listar_proveedores')
    else:
        print('no se pudo eliminar')
    return redirect('proveedores:listar_proveedores')
        
    



## pedidos
@login_required(login_url='usuarios:login')
def listar_pedidos(request):
    pedidos = Pedido.objects.all()
    estados = dict(Pedido.ESTADO)
    contexto = {
        'pedidos': pedidos,
        'estados': json.dumps(estados),
    }
    return render(request, 'pedidos/lista_pedidos.html', contexto)

@login_required(login_url='usuarios:login')
def ver_detalles_pedido(request, id):
    if request.method == 'POST':
        pedido = get_object_or_404(Pedido, id=id)
        items = pedido.items_pedidos.all()
        contexto = {
            'pedido':pedido,
            'items':items,
        }
    return render(request, 'pedidos/detalle_pedido.html', contexto)


@perfil_gerente_o_superior
def nuevo_pedido(request):
    if request.method == 'POST':
        proveedor_id = request.POST.get('proveedor')
        observacion = request.POST.get('observacion', '')
        proveedor = Proveedor.objects.get(id=proveedor_id)

        pedido = Pedido.objects.create(proveedor=proveedor, observacion=observacion)

        for insumo_id, cantidad_str in request.POST.items():
            if insumo_id.startswith('insumo_'):
                cantidad = int(cantidad_str)  
                if cantidad > 0: 
                    insumo_real_id = insumo_id.split('_')[1]
                    insumo = Insumo.objects.get(id=insumo_real_id)
                    Item_Pedido.objects.create(pedido=pedido, insumo=insumo, cantidad=cantidad)

        return redirect('proveedores:detalle_pedido', id=pedido.id)

    else:
        proveedores = Proveedor.objects.all()
        return render(request, 'pedidos/pedido_nuevo.html', {'proveedores': proveedores})


# Vista para obtener insumos del proveedor
@login_required(login_url='usuarios:login')
def obtener_insumos(request, proveedor_id):
    proveedor = Proveedor.objects.get(id=proveedor_id)
    insumos = [{'id': insumo.id, 'nombre': insumo.nombre} for insumo in proveedor.insumos.all()]
    return JsonResponse({'insumos': insumos})



@login_required(login_url='usuarios:login')
def detalle_pedido(request,id):
    pedido = get_object_or_404(Pedido, id=id)
    items = pedido.items_pedidos.all()
    empleado = Empleado.objects.get(usuario=request.user)
    contexto = {
        'pedido': pedido,
        'items': items,
        'empleado': empleado,
    }
    return render(request,'pedidos/detalle_pedido.html', contexto)

@perfil_gerente_o_superior
def cancelar_pedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    if pedido.estado == 'Pendiente':
        pedido.estado = 'Cancelado'
        pedido.save()  
        messages.success(request, f"El pedido fue cancelado.")

        return redirect('proveedores:detalle_pedido', id=id)
    else:
        messages.info(request, f'El pedido no puede ser cancelado.')
        return redirect('proveedores:detalle_pedido', id=id)



#######recepciones
@login_required(login_url='usuarios:login')
def recepcion_pedido(request, id):
    pedido = get_object_or_404(Pedido, pk=id)
    
    if pedido.estado != 'Pendiente':
        messages.error(request, 'El pedido ya no puede recibirse')
        return redirect('proveedores:detalle_pedido', id=id)
    
    pedido.estado = 'Recibido'
    pedido.save()
    
    items_pedidos = Item_Pedido.objects.filter(pedido=pedido)    
    empleado = Empleado.objects.get(usuario=request.user)
    
    recepcion = Recepcion.objects.create(
        empleado_receptor=empleado,
        pedido=pedido,
        conformidad=request.POST.get('conformidad'),
        observacion=request.POST.get('observacion'),
        total_pedido = 0,
    )
   
        

    total_pedido = 0
    
    for item in items_pedidos:
        cantidad_recibida = int(request.POST.get(f'cantidad_recibida_{item.id}'))
        precio_unitario = float(request.POST.get(f'precio_unitario_{item.id}'))
        precio_total = cantidad_recibida * precio_unitario  # subtotal por item
        total_pedido += precio_total  # total del pedido
        
        # creao el item_recepcion con la cantidad recibida, el precio unitario y subtotal
        Item_Recepcion.objects.create(
            recepcion=recepcion,
            insumo=item.insumo,
            cantidad_recibida=cantidad_recibida,
            precio_unitario=precio_unitario,
            precio_total=precio_total,
        )
        
        insumo = item.insumo
        insumo.stock += cantidad_recibida
        insumo.save()
    
    recepcion.total_pedido = total_pedido
    recepcion.save()   
    
    return redirect('proveedores:detalle_recepcion', id=recepcion.id)      
    
    
@login_required(login_url='usuarios:login')
def listar_recepciones(request):
    recepciones = Recepcion.objects.all()
    print(recepciones)

    return render(request,'pedidos/lista_recepciones.html', {'recepciones':recepciones})



@login_required(login_url='usuarios:login')
def detalle_recepcion(request, id):
    recepcion = get_object_or_404(Recepcion, id=id)
    items_recibidos = recepcion.items_recibido.all()
    
    contexto = {
        'recepcion': recepcion,
        'items': items_recibidos,
    }
    return render(request,'pedidos/detalle_recepcion.html', contexto)