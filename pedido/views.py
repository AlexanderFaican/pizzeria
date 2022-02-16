from django.shortcuts import render, redirect
from .models import Factura,Detalle_factura
def total(request):
	lista = Factura.objects.all()
	return render (request, 'pedido/all.html',{'lista':lista})

def despachar(request):
	dni = request.GET['id']
	
	factura = Factura.objects.get(id = dni)
	detalle = Detalle_factura.objects.filter(factura = factura.id)
	if (detalle.exists()):
		detalle.delete()
		factura.delete()
		return redirect(total)
	else: 
		factura.delete()	

	return redirect(total)
