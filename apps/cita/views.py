from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from django.views.generic import CreateView,ListView
from django.core.urlresolvers import reverse_lazy
from apps.cita.forms import CitaForm
from apps.cita.models import Citas



def cita_view(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method=='POST':
		form= CitaForm(request.POST,instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			form.save()
		return redirect('cita:cita', pk=post.pk)
	else:
		form=CitaForm(instance=post)
	return render(request,'cita/cita.html',{'form':form})



class CitasCreate(CreateView):
	model = Citas
	form_class = CitaForm
	template_name = 'cita/cita.html'
	success_url = reverse_lazy('cita:cita_list')

def cita_list(request):
	cita=Citas.objects.all()
	contexto={'citas':cita}
	return render(request, 'cita/cita_list.html',contexto)

def cita_edit(request, id_cita):
	cita=Citas.objects.get(id=id_cita)
	if request.method == 'GET':
		form = CitaForm(instance=cita)
	else:
		form = CitaForm(request.POST, instance=cita)
		if form.is_valid():
			form.save()
		return redirect('cita:cita_list')
	return render(request, 'cita/cita.html', {'form':form})

def cita_delete(request,id_cita):
	cita = Citas.objects.get(id=id_cita)
	if request.method == 'POST':
		cita.delete()
		return redirect('cita:cita_list')
	return render(request, 'cita/cita_delete.html', {'cita':cita})
	


	