import datetime

def calcular_tempo_do_dia(hora, minutos):
    agora = datetime.datetime.now()

    hora_fornecida = hora_fornecida = datetime.datetime(agora.year, agora.month, agora.day, hora, minutos)

    diferenca = hora_fornecida-datetime.datetime(agora.year, agora.month, agora.day)

    minutos_decorridos = diferenca.total_seconds() / 60
    minutos_faltando = 24 * 60 - minutos_decorridos

    return minutos_decorridos, minutos_faltando

hora_atual = int(input('Qual a hora agora? '))
minutos_atuais = int(input('Quais são os minutos agora? ')) 

tempo_decorrido, minutos_faltando = calcular_tempo_do_dia(hora_atual, minutos_atuais)
print(f"Minutos decorridos desde o início do dia: {tempo_decorrido} minutos")
print(f"Minutos faltando para o dia acabar: {minutos_faltando} minutos")
