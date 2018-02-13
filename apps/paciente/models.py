from django.db import models

# Create your models here.

class Pacientes(models.Model):
	nombre=models.CharField(max_length=100)
	fecha_nacimiento=models.DateField()
	telefono=models.CharField(max_length=100)
	nota = models.TextField(blank=True, null=True)


	class Meta:
			verbose_name = u'Paciente'
			verbose_name_plural = u'Paciente'

