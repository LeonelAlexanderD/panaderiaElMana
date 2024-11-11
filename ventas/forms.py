from django import forms
from django.forms import DateInput

from productos.models import Insumo, Producto
from ventas.models import CarritoProducto, Cliente_Mayorista, Comprobante


class ComprobanteForm(forms.ModelForm):
    class Meta:
        model = Comprobante
        fields = ['tipo_de_venta', 'forma_de_pago', 'tipo_comprobante', 'observacion']
        widgets = {
            'observacion': forms.Textarea(attrs={'rows': 3}),
        }



class ClienteForm(forms.ModelForm):    
    class Meta:
        model = Cliente_Mayorista
        fields = ['razon_social', 'cuit', 'telefono']