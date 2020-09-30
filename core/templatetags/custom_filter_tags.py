from django import template
from random import choice
from core import dias


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

@register.simple_tag
def mudaCor(st):
    #st=str(st)
    if st == 'v':
        return 'success'
    else:
        return 'danger'