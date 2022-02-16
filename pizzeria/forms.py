from django import forms
class FormularioLogin(forms.Form):
	Nombre = forms.CharField()
	Clave = forms.CharField(widget=forms.PasswordInput())