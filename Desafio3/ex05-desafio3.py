entrada_hora = int(input('Digite a hora de sua entrada no estacionamento: '))
entrada_minuto = int(input('Digite os minutos de sua entrada no estacionamento: '))
saida_hora = int(input('Digite a hora da sua saída do estacionamento: '))
saida_minuto = int(input('Digite os minutos da sua saída do estacionamento: '))

def calcular_preco_mesmo_dia(entrada_hora, entrada_minuto, saida_hora, saida_minuto):

    entrada_minuto = ((entrada_hora * 60) + entrada_minuto)
    minutos_saida = ((saida_hora * 60) + saida_minuto)

    diferenca_tempo = minutos_saida - entrada_minuto
    diferenca_horas = diferenca_tempo/ 60
    if diferenca_horas <= 2:
        preco_estacionamento = diferenca_horas * 1.00
        print(f'O valor cobrado pelo estacionamento é R${preco_estacionamento:.2f}')
    elif 3 <= diferenca_horas <= 4:
        preco_estacionamento = 4.80 + (diferenca_horas - 4) * 2.00
        print(f'O valor cobrado pelo estacionamento é R${preco_estacionamento:.2f}')
    else:
        preco_estacionamento = 2.00 + (diferenca_horas - 2) * 1.40
        print(f'O valor cobrado pelo estacionamento é R${preco_estacionamento:.2f}')


def calcular_preco_dia_posterior(entrada_hora, entrada_minuto, saida_hora, saida_minuto):

    minutos_entrada = ((entrada_hora * 60) + entrada_minuto)
    minutos_saida = ((saida_hora * 60) + saida_minuto)

    diferenca_tempo = 1440 - minutos_entrada + minutos_saida
    diferenca_horas = diferenca_tempo/ 60
    if diferenca_horas <= 2:
        preco_estacionamento = diferenca_horas * 1.00
        print(f'O valor cobrado pelo estacionamento é R${preco_estacionamento:.2f}')
    elif 3 <= diferenca_horas <= 4:
        preco_estacionamento = 4.80 + (diferenca_horas - 4) * 2.00
        print(f'O valor cobrado pelo estacionamento é R${preco_estacionamento:.2f}')
    else:
        preco_estacionamento = 2.00 + (diferenca_horas - 2) * 1.40
        print(f'O valor cobrado pelo estacionamento é R${preco_estacionamento:.2f}')
    

if entrada_hora <= saida_hora:
    calcular_preco_mesmo_dia(entrada_hora, entrada_minuto, saida_hora, saida_minuto)
else:
    calcular_preco_dia_posterior(entrada_hora, entrada_minuto, saida_hora, saida_minuto)