from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from django.views.generic import CreateView,ListView
from django.core.urlresolvers import reverse_lazy
from apps.paciente.forms import PacienteForm
from apps.paciente.models import Pacientes



def paciente_view(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method=='POST':
		form= PacienteForm(request.POST,instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			form.save()
		return redirect('paciente:paciente', pk=post.pk)
	else:
		form=PacienteForm(instance=post)
	return render(request,'paciente/paciente.html',{'form':form})


# Funcion para crear un paciente
class PacientesCreate(CreateView):
	model = Pacientes
	form_class = PacienteForm
	template_name = 'paciente/paciente.html'
	success_url = reverse_lazy('paciente:paciente_lista')

# Funcion para   en listar los pacientes creados

def paciente_list(request):
	paciente=Pacientes.objects.all()
	contexto={'pacientes':paciente}
	return render(request, 'paciente/paciente_list.html',contexto)

# funcion para editar la informacion de los pacientes

def paciente_edit(request, id_paciente):
	paciente=Pacientes.objects.get(id=id_paciente)
	if request.method == 'GET':
		form = PacienteForm(instance=paciente)
	else:
		form = PacienteForm(request.POST, instance=paciente)
		if form.is_valid():
			form.save()
		return redirect('paciente:paciente_lista')
	return render(request, 'paciente/paciente.html', {'form':form})

# Funcion para borrar un paciente
def paciente_delete(request,id_paciente):
	paciente = Pacientes.objects.get(id=id_paciente)
	if request.method == 'POST':
		paciente.delete()
		return redirect('paciente:paciente_lista')
	return render(request, 'paciente/paciente_deletes.html', {'paciente':paciente})