from functools import wraps
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages

from usuarios.models import Empleado


def perfil_gerente_o_superior(view_func):
    @wraps(view_func)
    @login_required(login_url='usuarios:login')
    def _wrapped_view(request, *args, **kwargs):
        try:
            empleado = Empleado.objects.get(usuario=request.user)
            if empleado.perfil not in ['Gerente', 'Administrador']:
                messages.error(request,'No tenes permiso para acceder a esta sección')
                return redirect('inicio')
        except Empleado.DoesNotExist:
            messages.error(request,'No tenes un perfil de empleado asignado')
            return redirect('inicio')
        return view_func(request, *args, **kwargs)
    
    return _wrapped_view

def perfil_administrador(view_func):
    @wraps(view_func)
    @login_required  
    def _wrapped_view(request, *args, **kwargs):
        try:
            empleado = Empleado.objects.get(usuario=request.user)
            if empleado.perfil != 'Administrador':
                messages.error(request,'No tenes permiso para acceder a esta sección')
                return redirect('inicio')  
        except Empleado.DoesNotExist:
            messages.error(request,'No tenes un perfil de empleado asignado')
            return redirect('inicio')  
        return view_func(request, *args, **kwargs)
    
    return _wrapped_view