from django.db import models
class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, null=False)
    codigo = models.CharField(max_length=10, null=False)
    cantidad = models.IntegerField( null=False, default=0)
    precio = models.IntegerField( null=False, default=0)
    ingredientes = models.CharField(max_length=50, null=False)
    descripcion = models.CharField(max_length=50,default='')
