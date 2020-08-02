from django import forms
from .models import Producto, Categoria
class ProductoForm(forms.ModelsForm):
	class Meta:
		model=Producto
		fields=['nombre','desc']