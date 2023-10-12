from datetime import date

data_hoje = date.today().year
maior_idade = menor_idade = maior_18 = menor_18 = 0
for i in range(0,7):
    nascimento = int(input(f'Digite a data de nascimento da {i+1}º pessoa: '))
    if nascimento > data_hoje or nascimento < 0:
        print('Digite um ano de nascimento valido')
        break
    idade = data_hoje - nascimento
    posicao = i+1
    if idade >= 18:
        maior_18 +=1
    else:
        menor_18 += 1
    if i == 0:
        maior_idade = menor_idade = idade
        posicao_maior_idade = posicao_menor_idade = posicao
    elif i > 0:
        maior_idade = max(maior_idade,idade)
        menor_idade = min(menor_idade,idade)
        if maior_idade == idade:
            posicao_maior_idade = posicao
        elif menor_idade == idade:
            posicao_menor_idade = posicao

print(f'Ao todo tivemos {maior_18} pessoas maiores de idade\n{menor_18} pessoas menores de idade\nA pessoa com mais idade entre as 7 registradas foi a {posicao_maior_idade}º pessoa com {maior_idade} anos\nA pessoa mais nova entre as 7 registradas foi a {posicao_menor_idade}º pessoa com {menor_idade} anos')

