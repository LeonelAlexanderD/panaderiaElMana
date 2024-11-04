from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse


# Create your views here.


def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('inicio')
        else:
            return render(request,'usuarios/login.html',{"msj":"Datos incorrectos"})
    return render(request,'usuarios/login.html')

def logout_view(request):
    logout(request)
    return redirect('inicio')