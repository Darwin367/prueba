from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse

# Create your models here.

class Citas(models.Model):
	nombre=models.CharField(max_length=100)
	fecha_nacimiento=models.DateField()
	telefono=models.CharField(max_length=100)
	tipo_cita=models.CharField(max_length=100)
	dia=models.DateField()
	inicio_cita = models.TimeField()
	finaliza_cita = models.TimeField()
	nota = models.TextField(blank=True, null=True)

	class Meta:
			verbose_name = u'Cita'
			verbose_name_plural = u'Cita'


	def mirar_conincidencia(self, inicio_fijo, fin_fijo, inicio, fin):
         conincidencia = False
         if inicio == fin_fijo or fin == inicio_fijo:    # Caso muy extremos
              conincidencia = False
         elif (inicio >= inicio_fijo and inicio <= fin_fijo) or (fin >= inicio_fijo and fin <= fin_fijo): # limites internos
               conincidencia = True
         elif inicio <= inicio_fijo and fin >= fin_fijo: # limite
              conincidencia = True
 
         return conincidencia


	def obteniendo_url(self):
         url = reverse('admin:%s_%s_change' % (self._meta.app_label, self._meta.model_name), args=[self.id])
         return u'<a href="%s">%s</a>' % (url, str(self.inicio_cita))


	def verificar(self):
         if self.finaliza_cita <= self.inicio_cita:
              raise ValidationError('Hora no valida')
 
         cita = Citas.objects.filter(dia=self.dia)
         if  cita.exists():
              for citas in cita:
                 if self.mirar_conincidencia(citas.inicio_cita, citas.finaliza_cita, self.inicio_cita, self.finaliza_cita):
                     raise ValidationError(
                         'Por favor ingrese otra hora: ' + str(citas.dia) + ', ' + str(
                            citas.inicio_cita) + '-' + str(citas.finaliza_cita))
