from django.http import JsonResponse
from django.shortcuts import redirect, render

from productos.forms import CrearProductoForm, ProductoForm
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

def cargar_producto(request):
    form = CrearProductoForm()
    print('hola')
    if request.method == 'POST':
        form = CrearProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()        
            return redirect('productos:listar_productos')
        return JsonResponse({'success': False, 'errors': form.errors})

    return render(request, 'productos/lista_productos.html', {'form': form})

def registrar_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('productos:listar_productos')
        return JsonResponse({'success': False, 'errors': form.errors})




def listar_insumos(request):
    insumos = Insumo.objects.all()
    return render(request, 'insumos/lista_insumos.html', {'insumos': insumos})
