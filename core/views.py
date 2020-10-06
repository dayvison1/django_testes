from django.shortcuts import render, redirect
from django.contrib import messages
from django.template.base import VARIABLE_ATTRIBUTE_SEPARATOR
from .models import Empresa, Horario, Vagas
from .forms import VagasModelForms
from core import dias

# Create your views here.

def index(request): 
    empresa = Empresa.objects.all()
    horarios = Horario.objects.all()
    #teste = Vagas.objects.all()
    primeiraSemana = dias.primeira_semana
    segundaSemana = dias.segunda_semana
    terceiraSemana = dias.terceira_semana
    quartaSemana = dias.quarta_semana
    listaux = [1,2,3,4,5,6,7]
    system = request.POST.get('campo',None)
    #print(teste)  
    form = VagasModelForms()
    context = {'emp':empresa,
    'hor':horarios,
    'semana1': primeiraSemana,
    'semana2': segundaSemana,
    'semana3': terceiraSemana,
    'semana4': quartaSemana,
    'form':form,
    'listaux':listaux,
    'teste':Vagas.objects.filter(idVaga='sub')
    }
  
    if str(request.method) == 'POST':
        form = VagasModelForms(request.POST)
        if form.is_valid():
            form = form.save(commit=False)#usei o nome task so pra testa
            form.statusVaga="Reservado"
            form.idVaga=system
            form.save()
            messages.success(request, 'Agendamento realizado com sucesso.')
            #form=VagasModelForms(request.POST)
            
            return render(request,'index.html',context)
            
            

    else:
        form = VagasModelForms()
    
    

   
    return render(request,'index.html',context)
 

