from __future__ import unicode_literals
from django.contrib import admin
from apps.cita.models import Citas




# Register your models here.

class CitasAdmin(admin.ModelAdmin):
	list_display = ['nombre','fecha_nacimiento','telefono','tipo_cita','dia', 'inicio_cita', 'finaliza_cita', 'nota']
	


admin.site.register(Citas, CitasAdmin)