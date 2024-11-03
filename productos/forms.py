from django import forms
from django.forms import DateInput

from productos.models import Insumo, Producto



class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['imagen', 'nombre', 'precio', 'unidad_medida', 'descripcion', 'stock', 'categoria', 'tipo']
        widgets = {
            'imagen':forms.ClearableFileInput(),
        }
        

# class InsumoForm(forms.ModelForm):
#     class Meta:
#         model = Insumo
#         fields = ('marca', 'tipo', 'nombre', 'cantidad', 'medida', 'punto_de_pedido')
#         widgets = {
            
#         }
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field in self.fields.values():
#             if not isinstance(field.widgets, forms.CheckboxInput):
#                 field.widget.attrs['class'] = 'form-control'
#             else:
#                 field.widget.attrs['class'] = 'form-check-input'
    
class InsumoForm(forms.ModelForm):
    class Meta:
        model = Insumo
        fields = ('marca', 'tipo', 'nombre', 'cantidad', 'medida', 'punto_de_pedido')