from django.shortcuts import render, redirect
from .models import Empresa, Horario
from .forms import VagasModelForms
from core import dias

# Create your views here.

def index(request): 
    empresa = Empresa.objects.all()
    horarios = Horario.objects.all()
    primeiraSemana = dias.primeira_semana
    segundaSemana = dias.segunda_semana
    terceiraSemana = dias.terceira_semana
    quartaSemana = dias.quarta_semana
    if str(request.method) == 'POST':
        form = VagasModelForms(request.POST)
        if form.is_valid():
            form.save()


    else:
        form = VagasModelForms()
    
    context = {'emp':empresa,
    'hor':horarios,
    'semana1': primeiraSemana,
    'semana2': segundaSemana,
    'semana3': terceiraSemana,
    'semana4': quartaSemana,
    'form':form}
    return render(request,'index.html',context)

