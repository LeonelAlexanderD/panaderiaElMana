from audioop import reverse
from pyexpat.errors import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404 
from proveedores.forms import ProveedorForm
from proveedores.models import Proveedor

# Create your views here.
def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedores\lista_proveedores.html', {'proveedores': proveedores})



def registrar_proveedor(request):
    if request.method == "POST":
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proveedores:listar_proveedores')
        return JsonResponse({'success': False, 'errors': form.errors})
    
def detalle_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    return render(request, 'proveedores/detalle_proveedor.html',{'proveedor':proveedor})



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


def eliminar_proveedor(request, pk):
    if request.method == 'POST':
        proveedor = get_object_or_404(Proveedor, pk=pk)
        proveedor.delete()
        
    return redirect('proveedores:listar_proveedores')