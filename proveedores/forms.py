from django import forms

from productos.models import Insumo
from .models import Item_Pedido, Item_Recepcion, Pedido, Proveedor, Recepcion

class ProveedorForm(forms.ModelForm):
    insumos = forms.ModelMultipleChoiceField(
        queryset=Insumo.objects.all(),  # Asegúrate de tener insumos en la BD
        required=False,
        label="Insumos Proveídos",
        widget=forms.CheckboxSelectMultiple
    )
    class Meta:
        model = Proveedor
        fields = ['razon_social', 'cuit', 'contacto', 'insumos']
        
        
#####
class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['proveedor', 'observacion']
        widgets = {
            'proveedor': forms.Select(attrs={'class': 'form-control'}),
            'observacion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class ItemPedidoForm(forms.ModelForm):
    insumo = forms.ModelChoiceField(
        queryset=Insumo.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    cantidad = forms.IntegerField(
        min_value=0,
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Item_Pedido
        fields = ['insumo', 'cantidad']
        
        
        
## recepciones
class RecepcionForm(forms.ModelForm):
    class Meta:
        model = Recepcion
        fields = ['conformidad', 'observacion']
        widgets = {
            'conformidad': forms.Textarea(attrs={'required': True}),
            'observacion': forms.Textarea(attrs={'required': False}),
        }

class ItemRecepcionForm(forms.ModelForm):
    class Meta:
        model = Item_Recepcion
        fields = ['cantidad_recibida', 'precio_unitario']
        widgets = {
            'cantidad_recibida': forms.NumberInput(attrs={'required': True}),
            'precio_unitario': forms.NumberInput(attrs={'required': True, 'step': '0.01'}),
        }