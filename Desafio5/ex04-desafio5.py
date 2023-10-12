# Pedir o valor e a quantidade de meses da aplicação
contador = 0
valor_aplicacao = float(input('Qual é o valor total da aplicação? R$'))
meses = int(input('Digite o número de meses da aplicação: '))
valor_inicial = valor_aplicacao
while True:
# Validar a entrada de dados
    contador+=1
    if valor_aplicacao < 0:
        print('Valor inválido')
        break
    if meses < 1:
        print('Número de meses inválido')
        break

# Verificar a porcentagem de juros que se deve pagar e calcular os juros usando a atribuição
    if valor_aplicacao < 2000:
        valor_aplicacao*=1.005
    elif valor_aplicacao >= 2000 and valor_aplicacao < 10000:
        valor_aplicacao*=1.01
    elif valor_aplicacao >= 10000:
        valor_aplicacao*=1.015
        print(valor_aplicacao)
    if contador >= meses:
        print(f'Depois de {meses} meses de aplicação, com o valor inicial de R${valor_inicial} o valor total aplicado será de R$ {valor_aplicacao:.2f}')
        break


    