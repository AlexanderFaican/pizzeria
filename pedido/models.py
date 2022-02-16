from django.db import models
class Factura(models.Model):

	id = models.AutoField(primary_key = True)#es el auto incrementable
	persona=models.CharField(max_length = 50, null = False)
	estado=models.CharField(max_length = 50, null = False)
	fecha_pedido = models.CharField(max_length = 50, null = False)
	fecha_entrega = models.CharField(max_length = 50, null = False)
	IVA = models.CharField(max_length = 50, null = False)
	subtotal = models.CharField(max_length = 50, null = False)
	total = models.CharField(max_length = 50, null = False)
	pago = models.CharField(max_length = 10)
	descuento = models.CharField(max_length = 10)
class Detalle_factura(models.Model):
	id = models.AutoField(primary_key = True)#es el auto incrementable
	factura  = models.CharField(max_length = 50, null = False)
	articulo = models.CharField(max_length = 50, null = False)
	cantidad = models.CharField(max_length = 50, null = False)
