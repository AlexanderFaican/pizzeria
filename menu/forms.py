from django import forms
from .models import Menu

class FormularioMenu(forms.ModelForm):
	class Meta:
		model = Menu
		fields=["nombre","codigo","cantidad","precio","ingredientes","descripcion"]