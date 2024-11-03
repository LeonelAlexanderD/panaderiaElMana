from django.contrib import admin

# Register your models here.
from .models import Empleado, Domicilio

class DomicilioInline(admin.StackedInline):
    model = Domicilio
    can_delete = False
    verbose_name_plural = 'Domicilio'

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    inlines = [DomicilioInline]
    list_display = ('nombre', 'apellido', 'perfil', 'telefono', 'cuit')
    search_fields = ('nombre', 'apellido', 'cuit')
    list_filter = ('perfil',)