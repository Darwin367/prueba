from django.contrib import admin

# Register your models here.
from apps.paciente.models import Pacientes
import datetime
import calendar
from calendar import HTMLCalendar

class PacientesAdmin(admin.ModelAdmin):
	 list_display = ['nombre','fecha_nacimiento','telefono','nota']

admin.site.register(Pacientes, PacientesAdmin)