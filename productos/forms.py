from django import forms
from django.forms import DateInput

from productos.models import Producto

class CrearProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('imagen', 'nombre', 'precio', 'unidad_medida', 'descripcion', 'stock', 'categoria', 'tipo')
        
        widgets = {
            'imagen':forms.ClearableFileInput(),
        }
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.field.values():
            if not isinstance(field.widgetm, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] = 'form-check-input'


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['imagen', 'nombre', 'precio', 'unidad_medida', 'descripcion', 'stock', 'categoria', 'tipo']
        widgets = {
            'imagen':forms.ClearableFileInput(),
        }
        
      