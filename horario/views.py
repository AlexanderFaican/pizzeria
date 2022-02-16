from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import FormularioHorario
from .models import Horario
 
def total(request): 

	lista = Horario.objects.all()#elemnto del orm objetss.all oltengo los elementos y los almaceno en lista

	return render (request,'horario/all.html',{'lista':lista})

 
def crear(request):
	if request.method =='POST':
		formulario = FormularioHorario(request.POST)
		if formulario.is_valid():
			horario= Horario()
			horario.nombre 		=   request.POST.get('nombre')
			horario.hora_inicio		=   request.POST.get('hora_inicio')
			horario.hora_fin 	= 	request.POST.get('hora_fin')
			horario.dia 	=  	request.POST.get('dia')
			horario.save()
			return redirect(total)
	else:
		formularioC = FormularioHorario()
		context = {'formularioC':formularioC}
	return render (request,'horario/crear.html',context)

def modificar(request):
	dni = request.GET['id']
	horario = Horario.objects.get(id = dni)
	if request.method == 'POST': 
		formulario = FormularioHorario(request.POST)
		if formulario.is_valid():
			datos = formulario.cleaned_data #obteniendo todos los datos del formulario Horario
			horario.nombre 		=   datos.get('nombre')
			horario.dia 		=   datos.get('dia')
			horario.hora_fin 	= 	datos.get('hora_fin')
			horario.hora_inicio 	=  	datos.get('hora_inicio')
			horario.save()
			return redirect(total)
		#se modifica
	else:
		formulario = FormularioHorario(instance = horario)
	context = {
		'formularioC': formulario}
	return render (request,'horario/modificar.html', context)
 
def eliminar(request):
	idd = request.GET['id']
	horario = Horario.objects.get(id = idd)
	horario.delete()
	return redirect(total)
