from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Empleado(models.Model):
    PERFIL_CHOICES = [
        ('Administrativo', 'Administrativo'),
        ('Gerente', 'Gerente'),
        ('Vendedor', 'Vendedor'),
    ]
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='empleado')
    perfil = models.CharField(choices=PERFIL_CHOICES)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cuit = models.CharField(max_length=11, unique=True)
    telefono = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    fecha_ingreso = models.DateField()
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Domicilio(models.Model):
    calle = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    departamento = models.CharField(max_length=100, blank=True)
    localidad = models.CharField(max_length=100)
    empleado = models.OneToOneField(Empleado, on_delete=models.CASCADE, related_name="domicilio")

