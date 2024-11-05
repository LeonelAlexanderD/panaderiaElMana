from django import forms
from django.forms import DateInput

from productos.models import Insumo, Producto
from ventas.models import CarritoProducto, Comprobante


class ComprobanteForm(forms.ModelForm):
    class Meta:
        model = Comprobante
        fields = ['tipo_de_venta', 'forma_de_pago', 'tipo_comprobante', 'observacion']
        widgets = {
            'observacion': forms.Textarea(attrs={'rows': 3}),
        }

