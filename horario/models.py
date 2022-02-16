from django.db import models
class Horario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, null=False)
    hora_inicio = models.CharField(max_length=20, null=False)
    hora_fin = models.CharField(max_length=20,null=False)
    dia = models.CharField(max_length=20,null=False)
    def _str_(self):
        return self.id
