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
print(lista_dias)
