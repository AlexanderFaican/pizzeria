from django.shortcuts import render, redirect
from .forms import FormularioMenu
from .models import Menu
def total(request): 
	

	lista = Menu.objects.all()#elemnto del orm objetss.all oltengo los elementos y los almaceno en lista

	return render (request,'Menu/all.html',{'lista':lista})

def crear(request):
	print('totalllllllllllllllllllll-------------22222222')
	if request.method =='POST':
		formulario = FormularioMenu(request.POST)
		if formulario.is_valid():
			menu= Menu()
			menu.nombre 		=   request.POST.get('nombre')
			menu.cantidad		=   request.POST.get('cantidad')
			menu.codigo 	= 	request.POST.get('codigo')
			menu.precio 	=  	request.POST.get('precio')
			menu.ingredientes 	=   request.POST.get('ingredientes')
			menu.descripcion = request.POST.get('descripcion')
			menu.save()
			return redirect(total)
	else:
		formularioC = FormularioMenu()
		context = {'formularioC':formularioC}
	return render (request,'menu/crear.html',context)

def modificar(request):
	dni = request.GET['id']
	menu = Menu.objects.get(id = dni)
	if request.method == 'POST': 
		formulario = FormularioMenu(request.POST)
		if formulario.is_valid():
			datos = formulario.cleaned_data #obteniendo todos los datos del formulario Menu
			menu.nombre 		=   datos.get('nombre')
			menu.precio 		=   datos.get('precio')
			menu.codigo 	= 	datos.get('codigo')
			menu.cantidad 	=  	datos.get('cantidad')
			menu.ingredientes 	=   datos.get('ingredientes')
			menu.descripcion = datos.get('descripcion')
			menu.save()
			return redirect(total)
		#se modifica
	else:
		formulario = FormularioMenu(instance = menu)
	context = {
		'formularioC': formulario}
	return render (request,'Menu/modificar.html', context)

def eliminar(request):
	idd = request.GET['id']
	menu = Menu.objects.get(id = idd)
	menu.delete()
	return redirect(total)
