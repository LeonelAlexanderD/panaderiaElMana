from datetime import date
from decimal import Decimal
from django.db import models

from productos.models import Producto
from usuarios.models import Empleado

# Create your models here.
class Comprobante(models.Model):
    TIPO_VENTA = [
        ('contado', 'Contado'),
        ('credito', 'Credito')        
    ]
    
    FORMA_DE_PAGO = [
        ('efectivo', 'Efectivo'),
        ('tarjeta', 'Tarjeta'),
        ('transferencia', 'Transferencia')
    ]
    
    TIPO_COMPROBANTE = [
        ('factura', 'Factura'),
        ('ticket', 'Ticket')
    ]
    fecha_de_venta = models.DateField(default=date.today)
    tipo_de_venta = models.CharField(max_length=15, choices=TIPO_VENTA, verbose_name="Tipo de venta")
    forma_de_pago = models.CharField(max_length=15, choices=FORMA_DE_PAGO, verbose_name="Forma de pago")
    tipo_comprobante = models.CharField(max_length=30, choices=TIPO_COMPROBANTE)
    total_comprobante = models.DecimalField(max_digits=10, decimal_places=2)
    observacion = models.TextField(blank=True, null=True)
    
    def actualizarTotalComprobante(self):
        total = self.items.aggregate(total=models.Sum('subtotal'))['total'] or 0
        self.total_comprobante = total
        
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.actualizarTotalComprobante()


class CarritoProducto(models.Model):
    comprobante = models.ForeignKey(Comprobante, on_delete=models.CASCADE, related_name="items")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=20, decimal_places=2)

    def calcular_total(self):
        return self.producto.precio * Decimal(self.cantidad)
        
        
    def save(self, *args, **kwargs):
        self.subtotal = self.calcular_total()
        super().save(*args, **kwargs)
        self.comprobante.actualizarTotalComprobante()
    
    def delete(self, *args, **kwargs):
        comprobante = self.comprobante
        super().delete(*args, **kwargs)
        comprobante.actualizarTotalComprobante()


class Venta(models.Model):
    comprobante = models.OneToOneField(Comprobante, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

class Cliente_Mayorista(models.Model):
    razon_social = models.CharField(max_length=30)
    cuit = models.PositiveSmallIntegerField()
    telefono = models.PositiveSmallIntegerField()