from django import template
from random import choice
from core import dias
from ..models import Empresa, Horario, Vagas

register = template.Library()

@register.filter()
def filter_teste(value):
    return "{} +  QUalquer coisa".format(value)
listacor=["primary","secondary","success","danger","warning"]

@register.simple_tag
def corBotao():
    return choice(listacor)


@register.simple_tag
def idBotao(i,lista,j):
    
    idbtn = str(lista[8]) + str(lista[j]) + str(i)
    idbtn=idbtn.replace(":","")
    return idbtn.replace("/","")



vg=Vagas.objects.filter(statusVaga='Reservado').values('idVaga')
#vg=Vagas.objects.values('idVag.values('idVagas')
listaIdvagas=[]
for i in vg:
    listaIdvagas.append(i['idVaga'])
#print(vg[0:len(vg)])
li=['202003101700', '1202006100800', '202007100800', '202008100800', '202009100800', '202010100800', '202011100800', '202005100900', '202006100900', '202007100900', '202008100900', '202009100900', '202010100900', '202011100900', '202005101000', '202006101000', '202007101000', '202008101000', '202009101000', '202010101000', '202011101000', '202005101100', '202006101100', '202007101100', '202008101100', '202009101100', '202010101100', '202011101100', '202005101200', '202006101200', '202007101200', '202008101200', '202009101200', '202010101200', '202011101200', '202005101400', '202006101400', '202007101400', '202008101400', '202009101400', '202010101400', '202011101400', '202005101500', '202006101500', '202007101500', '202008101500', '202009101500', '202010101500', '202011101500', '202005101600', '202006101600', '202007101600', '202008101600', '202009101600', '202010101600', '202011101600', '202005101700', '202006101700', '202007101700', '202008101700', '202009101700', '202010101700', '202011101700', '202005101800', '202006101800', '202007101800', '202008101800', '202009101800', '202010101800', '202011101800']
@register.simple_tag
def ativaBotao(i,lista,j):
    
    x=idBotao(i,lista,j)
    bt=''
    if x in listaIdvagas:
         return "disabled"
       #tex= 'type=\"button\" class=\"btn btn-danger btn-sm btn-block\" data-toggle=\"modal\" data-target=\"#exampleModal\" onclick=\"setaDadosModal(\'{%idBotao i semana1 j%}\')\" >Indisponível'
    else:
        pass
        #tex='type=\"button\" class=\"btn btn-danger btn-sm btn-block\" data-toggle=\"modal\" data-target=\"#exampleModal\" onclick=\"setaDadosModal(\'{%idBotao i semana1 j%}\')\" >Disponível' 
    #print("true")
    #print(str(x))
    #return x
@register.simple_tag
def mudaTexto(i,lista,j):
    
    x=idBotao(i,lista,j)
    if x in listaIdvagas:
         return 'Indisponível'
    else:
        return 'Disponível' 


@register.simple_tag
def mudaCor(i,lista,j):
    
    x=idBotao(i,lista,j)
    if x in listaIdvagas:
         return 'danger'
    else:
        return 'success' 
