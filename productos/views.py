from decimal import Decimal
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404

from productos.forms import ProductoForm
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
    return render(request, 'productos/lista_productos.html', {'productos': productos})



# def registrar_producto(request):
#     if request.method == "POST":
#         form = ProductoForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('productos:listar_productos')
#         return JsonResponse({'success': False, 'errors': form.errors})
    
def registrar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('productos:listar_productos')
    else:
        form = ProductoForm()

    context = {
        'form': form,
        'categoria_choices': Producto.CATEGORIAS,
        'unidad_medida_choices': Producto.UNIDADES,
    }
    return render(request, 'productos/registro_producto.html', context)

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request,'productos/detalle_producto.html', {'producto':producto})

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

def listar_insumos(request):
    insumos = Insumo.objects.all()
    return render(request, 'insumos/lista_insumos.html', {'insumos': insumos})
