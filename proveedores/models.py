from datetime import date
from django.db import models

from productos.models import Insumo
from usuarios.models import Empleado

# Create your models here.
class Proveedor (models.Model):
    razon_social = models.CharField(max_length=30)
    cuit = models.BigIntegerField()
    contacto = models.BigIntegerField() 
    
    def __str__(self):
        return f"{self.razon_social}, contacto: {self.contacto}"
    
class Pedido (models.Model):
    ESTADO = [
        ('Pendiente', 'Pendiente'),
        ('Recibido', 'Recibido'),
        ('Cancelado', 'Cancelado'),
    ]
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    fecha_pedido = models.DateField(default=date.today)
    observacion = models.TextField(blank=True)
    estado = models.CharField(
        choices= ESTADO,
        default='Pendiente',
    )

class Item_Pedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='items_pedido')
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE)
    cantidad = models.PositiveSmallIntegerField()

    
class Recepcion (models.Model):
    empleado_receptor = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE)
    fecha_recepcion = models.DateField(default=date.today)
    conformidad = models.TextField()
    observacion = models.TextField(blank=True)
    
class Item_Recepcion(models.Model):
    recepcion = models.ForeignKey(Recepcion, on_delete=models.CASCADE, related_name='items_recibido')
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE)
    cantidad_recibida = models.PositiveSmallIntegerField()
    precio_unitario = models.DecimalField(max_digits=8, decimal_places=2)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)