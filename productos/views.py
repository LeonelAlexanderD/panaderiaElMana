from decimal import Decimal
import json
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
# from django.core.serializers.json import DjangoJSONEncoder
from productos.forms import InsumoForm, ProductoForm
from productos.models import Insumo, Producto

# Create your views here.

## generales:
def pagina_principal(request):
    return render(request, 'index.html')

def pagina_gestion(request):
    return render(request, 'gestion/gestion.html')


## productos
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



def registrar_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('productos:listar_productos')
        return JsonResponse({'success': False, 'errors': form.errors})
    
    
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

def eliminar_producto(request, pk):
    if request.method == 'POST':
        producto = get_object_or_404(Producto, pk=pk)
        producto.delete()
        
    return redirect('productos:listar_productos')

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
#
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


# def cargar_insumo(request):
#     nuevo_insumo = None
#     if request.method == 'POST':
#         insumo_form = InsumoForm(request.POST)
#         if insumo_form.is_valid():
#             nuevo_insumo = insumo_form.save()
#             messages.success(
#                 request, 'Se ha guardado el insumo'
#             )
#             return redirect('productos:listar_insumos')
#     else:
#         insumo_form = InsumoForm()
#     return render(request, 'productos/listar_insumos.html',{'form':insumo_form})

def cargar_insumo(request):
    if request.method == "POST":
        form = InsumoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos:listar_insumos')
        return JsonResponse({'success': False, 'errors': form.errors})