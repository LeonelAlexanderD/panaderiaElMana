"""
URL configuration for panaderiaElMana project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import include, path
from productos import views as productos_views
from ventas import views as ventas_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', productos_views.pagina_principal, name='inicio'),
    path('gestion/', productos_views.pagina_gestion, name="gestion"),
    path('ventas/', include('ventas.urls', namespace='ventas')),
    path('proveedores', include('proveedores.urls', namespace='proveedores')),
    path('productos/', include('productos.urls', namespace='productos')),
    path('usuarios/', include('usuarios.urls', namespace='usuarios')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
