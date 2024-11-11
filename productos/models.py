from django.db import models


# Create your models here.
class Insumo(models.Model):
    UNIDADES = [
        ('unidad', 'u.'),
        ('gramo', 'gr.'),
        ('kilogramo', 'kg.')
    ]
    nombre = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)    
    stock = models.DecimalField(max_digits=10, decimal_places=2)
    medida = models.CharField(max_length=30, choices=UNIDADES)
    punto_de_pedido = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return f"{self.nombre}, marca: {self.marca}"


class Producto(models.Model):
    UNIDADES = [
        ('unidad', 'u.'),
        ('gramo', 'gr.'),
        ('kilogramo', 'kg.')
    ]
    CATEGORIAS = [
        ('Panaderia', 'panaderia'),
        ('Pasteleria', 'pasteleria')
    ]
    imagen = models.ImageField(blank=False)
    nombre = models.CharField(max_length=30, blank=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    unidad_medida = models.CharField(max_length=10, choices=UNIDADES)
    descripcion = models.TextField(blank=True)
    stock = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    categoria = models.CharField(max_length=30, choices=CATEGORIAS)
    subcategoria = models.CharField(max_length=30, blank=False)