contador = 0
vendedores = []
posicoes_vendedores = []

trabalhadores = int(input('De quantas pessoas eu devo calcular o salario? '))
while contador < trabalhadores:
    nome_vendedor = input(f'Qual é o nome do {contador+1}º vendedor? ')
    vendas = float(input('Quanto você vendeu essa semana, em reais: R$'))

    salario = 200+vendas*0.09
    posicoes = [299,399,499,599,699,799,899,999]
    contador+=1
    for i, j in enumerate(posicoes):
        if salario <= j:
            vendedores.append(nome_vendedor)
            posicoes_vendedores.append(i+1)
            break
    if len(vendedores) < contador:
        vendedores.append(nome_vendedor)
        posicoes_vendedores.append(9)
        
contador = 0
for vendedor in zip(vendedores,posicoes_vendedores):
    contador+=1
    print(f'O {contador}º vendedor se chama {vendedor[0]} e ficou na {vendedor[1]}º posição com um salario de R${salario:.2f}')