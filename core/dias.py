
import pendulum as pl

def dataInicioSemana(dt): #retorna o inicio da semana basedo no dia atual
    return dt.start_of('week')
def dataFimSemana(dt):  #retorna o fim da semana basedo no dia atual
    return dt.end_of('week')

def invertDias(dia): #coloca a data na ordem pt-br (01/10)
    data_str=str(dia)
    return data_str[8:10]+'/'+ data_str[5:7]
def ListarDias(data):#cria a lista com a datas da semana

    lista_dias=[invertDias(data)]
    dias_semana=pl.period(dataInicioSemana(data), dataFimSemana(data)) #calcula os dia da semana
    for d in dias_semana.range('days'):
        lista_dias.append(invertDias(d)) #preenche a lista com as datas
    lista_dias.append(str(data)[0:4]) #acrescenta o ano na lista
    return lista_dias


data_de_hoje = pl.now().in_timezone('America/Fortaleza')
primeira_semana = ListarDias(data_de_hoje)
segunda_semana = ListarDias(dataInicioSemana(data_de_hoje).add(days=7))
terceira_semana = ListarDias(dataInicioSemana(data_de_hoje).add(days=14))
quarta_semana = ListarDias(dataInicioSemana(data_de_hoje).add(days=21))

#print(primeira_semana,segunda_semana,terceira_semana,quarta_semana)














"""

import pendulum as pl


data_de_hoje = pl.now().in_timezone('America/Fortaleza')
inicio_semana = data_de_hoje.start_of('week')
fim_semana = data_de_hoje.end_of('week')
dias_semana= pl.period(inicio_semana,fim_semana)
def invertDias(dia):
    data_str=str(dia)
    return data_str[8:10]+'/'+ data_str[5:7]

lista_dias=[invertDias(data_de_hoje)]

for d in dias_semana.range('days'):
    lista_dias.append(invertDias(d))

#print(lista_dias)

"""