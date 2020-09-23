from django.shortcuts import render
from .models import Empresa, Horario
from core import dias

# Create your views here.

def index(request): 
    empresa = Empresa.objects.all()
    horarios = Horario.objects.all()
    datas = dias.lista_dias

    return render(request, 
    'index.html',
    {'emp':empresa,
    'hor':horarios,
    'dt': datas

    })
