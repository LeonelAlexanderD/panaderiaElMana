from decimal import Decimal
import json
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
# from django.core.serializers.json import DjangoJSONEncoder
from productos.forms import InsumoForm, ProductoForm
from productos.models import Insumo, Producto
from usuarios.decorators import perfil_administrador, perfil_gerente_o_superior

# Create your views here.

## generales:
def pagina_principal(request):
    return render(request, 'index.html')

@login_required(login_url='usuarios:login')
def pagina_gestion(request):
    return render(request, 'gestion/gestion.html')


## productos
@login_required(login_url='usuarios:login')
def listar_productos(request):
    productos = Producto.objects.all()
    medidas = dict(Producto.UNIDADES)
    categorias = dict(Producto.CATEGORIAS)
    
    context = {
        'productos': productos,
        'medidas_choices': json.dumps(medidas),
        'categorias_choices': json.dumps(categorias),
    }
    return render(request, 'productos/lista_productos.html', context)


@perfil_gerente_o_superior
def registrar_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('productos:listar_productos')
        return JsonResponse({'success': False, 'errors': form.errors})
    

@login_required(login_url='usuarios:login')
def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    medidas = dict(Producto.UNIDADES)
    categorias = dict(Producto.CATEGORIAS)
    context = {
        'producto': producto,
        'medidas_choices': json.dumps(medidas),
        'categorias_choices': json.dumps(categorias),
    }
    return render(request,'productos/detalle_producto.html', context)

@perfil_gerente_o_superior
def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('productos:detalle_producto', pk=producto.id)
    else:
        form = ProductoForm(instance=producto)
    
    return render(request, 'productos/detalle_producto.html', {'form': form, 'producto': producto})


@perfil_administrador
def eliminar_producto(request, pk):
    if request.method == 'POST':
        producto = get_object_or_404(Producto, pk=pk)
        producto.delete()
        
    return redirect('productos:listar_productos')


@perfil_gerente_o_superior
def agregar_stock(request, pk):
    if request.method == 'POST':
        producto = get_object_or_404(Producto, pk=pk)
        stock_adicional = request.POST.get('stock_adicional', 0)
        
        try:
            stock_adicional_decimal = Decimal(stock_adicional)
            if stock_adicional_decimal <= 0:
                return JsonResponse({'error': 'La cantidad debe ser mayor a 0'}, status=400)
            
            producto.stock += stock_adicional_decimal
            producto.save()
            
            return redirect('productos:listar_productos')
        except ValueError:
            return JsonResponse({'error': 'Valor de stock invalido'}, status=400)
    return JsonResponse({'error':'metodo no permitido'}, status=405)
    

@perfil_gerente_o_superior
def cambiar_precio(request, pk):
    if request.method == 'POST':
        producto = get_object_or_404(Producto, pk=pk)
        precio_nuevo = request.POST.get('precio_nuevo', 0)
        
        try:
            precio_nuevo_decimal = Decimal(precio_nuevo)
            if precio_nuevo_decimal <= 0:
                return JsonResponse({'error': 'El precio debe ser mayor a 0'}, status=400)
            
            producto.precio = precio_nuevo_decimal
            producto.save()
            
            return redirect('productos:listar_productos')
        except ValueError:
            return JsonResponse({'error': 'Precio invalido'}, status=400)
    return JsonResponse({'error':'metodo no permitido'}, status=405)



## INSUMOS
@login_required(login_url='usuarios:login')
def listar_insumos(request):
    insumos = Insumo.objects.all()
    unidades_choices = dict(Insumo.UNIDADES)
    # unidades_choices_json = json.dumps(unidades_choices, cls=DjangoJSONEncoder)
    context = {
        'insumos': insumos,
        'unidades_choices': json.dumps(unidades_choices),
        # 'unidades_choices_json': unidades_choices_json,
    }
    return render(request, 'insumos/lista_insumos.html', context)


@perfil_gerente_o_superior
def cargar_insumo(request):
    if request.method == "POST":
        form = InsumoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos:listar_insumos')
        return JsonResponse({'success': False, 'errors': form.errors})


@login_required(login_url='usuarios:login')
def detalle_insumo(request, id):
    insumo = get_object_or_404(Insumo, id=id)
    medidas = dict(Insumo.UNIDADES)
    contexto = {
        'insumo': insumo,
        'medidas': medidas,
    }
    return render(request, 'insumos/detalle_insumo.html', contexto)


@perfil_gerente_o_superior
def insumo_stock(request, id):
    if request.method == 'POST':
        insumo = get_object_or_404(Insumo, id=id)
        stock_adicional = request.POST.get('stock_adicional', 0)
        
        try:
            stock_adicional_decimal = Decimal(stock_adicional)
            if stock_adicional_decimal <= 0:
                return JsonResponse({'error': 'La cantidad debe ser mayor a 0'}, status=400)
            
            insumo.stock += stock_adicional_decimal
            insumo.save()
            
            return redirect('productos:listar_insumos')
        except ValueError:
            return JsonResponse({'error': 'Valor de stock invalido'}, status=400)
    return JsonResponse({'error':'metodo no permitido'}, status=405)


@perfil_administrador
def eliminar_insumo(request, id):
    if request.method == 'POST':
        insumo = get_object_or_404(Insumo, id=id)
        insumo.delete()
        
    return redirect('productos:listar_insumos')