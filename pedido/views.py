from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Factura,Detalle_factura
@login_required
def total(request):
	lista = Factura.objects.all()
	return render (request, 'pedido/all.html',{'lista':lista})
@login_required
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
