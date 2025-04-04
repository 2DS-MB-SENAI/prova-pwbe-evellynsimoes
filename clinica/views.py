from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import ConsultaForm

def listar_medicos(request):
    medicos = Medico.objects.all()
    especialidade = request.GET.get('especialidade', None)
    if especialidade:
        medicos = medicos.filter(especialidade__icontains=especialidade)
    return render(request, 'listar_medicos.html', {'listas': medicos})

def criar_consulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_medicos')
        else:
            return render(request,'erro.html')
            
    else:
        form = ConsultaForm() 
    return render(request, 'form_consulta.html', {'form': form})

def detalhes_consulta(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk)
    return render(request, 'crud_detalhes.html', {'detalhe': consulta})