from django.conf.urls import url, include
from apps.cita.views import  CitasCreate, cita_list,cita_edit,cita_delete 


urlpatterns = [
    url(r'^nuevo$', CitasCreate.as_view(),name='cita'),
    url(r'^listar$', cita_list, name='cita_list'),
    url(r'^editar/(?P<id_cita>\d+)/$', cita_edit,name='cita_edit'),
    url(r'^eliminar/(?P<id_cita>\d+)/$', cita_delete,name='cita_eliminar'),

]