from django.conf.urls import url, include
from apps.paciente.views import  PacientesCreate, paciente_list,paciente_edit,paciente_delete 


urlpatterns = [
    url(r'^nuevo$', PacientesCreate.as_view(),name='paciente'),
    url(r'^listar$', paciente_list, name='paciente_lista'),
    url(r'^editar/(?P<id_paciente>\d+)/$', paciente_edit,name='paciente_editar'),
    url(r'^eliminar/(?P<id_paciente>\d+)/$', paciente_delete,name='paciente_eliminar'),

]