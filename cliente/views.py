import cliente
from django.shortcuts import render, redirect
from .forms import FormularioCliente,FormularioCuenta
from .models import Cliente,Cuenta
 
def total(request): 

	lista = Cliente.objects.all()#elemnto del orm objetss.all oltengo los elementos y los almaceno en lista

	return render (request,'cliente/all.html',{'lista':lista})
 
def crear(request):
	print('entramosss a crearrrrr')
	if request.method =='POST':
		formulario = FormularioCliente(request.POST)
		if formulario.is_valid():
			cliente= Cliente()
			cliente.nombre 		=   request.POST.get('nombre')
			cliente.cedula 		=   request.POST.get('cedula')
			cliente.direccion 	= 	request.POST.get('direccion')
			cliente.telefono 	=  	request.POST.get('telefono')
			cliente.celular 	=   request.POST.get('celular')
			cliente.correo 		= 	request.POST.get('correo')
			cliente.apellido 	= 	request.POST.get('apellido')
			cliente.save()
			cuenta = Cuenta()
			cuenta.username = request.POST.get('username')
			cuenta.password = request.POST.get('password')
			cuenta.cliente = cliente.id
			cuenta.estado = True
			cuenta.save()
			return redirect(total)
	else:
		formularioC = FormularioCliente()
		formularioCu = FormularioCuenta()
		context = {'formularioC':formularioC,'formularioCu':formularioCu}
	return render (request,'cliente/crear.html',context)

def modificar(request):
	dni = request.GET['id']
	cliente = Cliente.objects.get(id = dni)
	if request.method == 'POST': 
		formulario = FormularioCliente(request.POST)
		if formulario.is_valid():
			datos = formulario.cleaned_data #obteniendo todos los datos del formulario cliente
			cliente.nombre 		=   datos.get('nombre')
			cliente.cedula 		=   datos.get('cedula')
			cliente.direccion 	= 	datos.get('direccion')
			cliente.telefono 	=  	datos.get('telefono')
			cliente.celular 	=   datos.get('celular')
			cliente.correo 		= 	datos.get('correo')
			cliente.apellido 	= 	datos.get('apellido')
			cliente.save()
			return redirect(total)
		#se modifica
	else:
		formulario = FormularioCliente(instance = cliente)
	context = {
		'formularioC': formulario}
	return render (request,'cliente/modificar.html', context)
 
def eliminar(request):
	idd = request.GET['id']
	cliente = Cliente.objects.get(id = idd)
	#cuenta = Cuenta.objects.get(persona = persona.id)
	#cuenta.delete()
	cliente.delete()
	return redirect(total)
