import datetime

def calcular_diferenca_idade(data1, data2):
    ano1 = int(data1[:4])
    mes1 = int(data1[5:7])
    dia1 = int(data1[8:])

    ano2 = int(data2[:4])
    mes2 = int(data2[5:7])
    dia2 = int(data2[8:])

    data_nascimento1 = datetime.datetime(ano1, mes1, dia1)
    data_nascimento2 = datetime.datetime(ano2, mes2, dia2)

    diferenca = data_nascimento1 - data_nascimento2
    anos = diferenca.days // 365
    meses = (diferenca.days % 365) // 30
    dias = (diferenca.days % 365) % 30
    return anos, meses, dias

pessoa1 = input('Digite a data de nascimento da primeira pessoa (yyyy-mm-dd): ')
pessoa2 = input('Digite a data de nascimento da segunda pessoa (yyyy-mm-dd): ')

resultado = calcular_diferenca_idade(pessoa1, pessoa2)
print(f'Diferença de idade: {resultado[0]} anos, {resultado[1]} meses, {resultado[2]} dias')

