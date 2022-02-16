from django.db import models

class Cliente(models.Model):

	id = models.AutoField(primary_key = True)#es el auto incrementable
	cedula = models.CharField(max_length = 10, null = False)
	nombre = models.CharField(max_length = 50, null = False)
	apellido = models.CharField(max_length = 50, null = False)
	direccion = models.CharField(max_length = 50, null = False)
	telefono = models.CharField(max_length = 10, null = False)
	celular = models.CharField(max_length = 10, null = False)
	correo = models.CharField(max_length = 50, null = False)
	estado = models.CharField(max_length = 10)

class Cuenta(models.Model):
	id = models.AutoField(primary_key = True)#es el auto incrementable
	cliente = models.CharField(max_length = 10, null = False)
	username = models.CharField(max_length = 10, null = False)
	password = models.CharField(max_length = 10, null = False)
