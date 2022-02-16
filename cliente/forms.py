from django import forms
from .models import Cliente, Cuenta

class FormularioCliente(forms.ModelForm):
	class Meta:
		model = Cliente
		fields=["cedula","nombre","apellido","direccion","telefono","celular","correo"]

class FormularioCuenta(forms.ModelForm):
	class Meta:
		model = Cuenta
		fields=["username","password"]