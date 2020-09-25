from django.shortcuts import render, redirect
from .models import Empresa, Horario
from .forms import VagasModelForms
from core import dias

# Create your views here.

def index(request): 
    empresa = Empresa.objects.all()
    horarios = Horario.objects.all()
    datas = dias.lista_dias
    if str(request.method) == 'POST':
        form = VagasModelForms(request.POST)
        if form.is_valid():
           
           form.save()
            #return redirect('')

    else:
        form = VagasModelForms()
    
    context = {'emp':empresa,'hor':horarios,'dt': datas,'form':form}
    return render(request,'index.html',context)

