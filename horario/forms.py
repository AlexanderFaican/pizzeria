from django import forms
from .models import Horario

class FormularioHorario(forms.ModelForm):
	class Meta:
		model = Horario
		fields=["nombre","hora_inicio","hora_fin","dia"]