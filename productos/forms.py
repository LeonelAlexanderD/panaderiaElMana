from django import forms
from django.forms import DateInput

from productos.models import Producto



class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['imagen', 'nombre', 'precio', 'unidad_medida', 'descripcion', 'stock', 'categoria', 'tipo']
        widgets = {
            'imagen':forms.ClearableFileInput(),
        }
        
      