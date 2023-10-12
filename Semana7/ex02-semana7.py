bebe = crianca = pre_adolecente = adolecente = jovem = adulto = idoso = 0
maior_idade = menor_idade = soma = 0

for i in range(1,11):
    idade  = int(input(f'Digite a idade da {i}º pessoa: '))
    soma += idade
    if idade < 2:
        bebe+=1
    elif idade >= 2 and idade < 10:
        crianca+=1
    elif idade >= 10 and idade < 14:
        pre_adolecente+=1
    elif idade >= 14 and idade < 18:
        adolecente+=1
    elif idade >= 18 and idade < 21:
        jovem+=1
    elif idade >= 21 and idade < 60:
        adulto+=1
    else:
        idoso+=1
    if i == 1:
        maior_idade = menor_idade = media = idade
    elif i > 1:
        maior_idade = max(maior_idade, idade)
        menor_idade = min(menor_idade, idade)

media = soma/10
print(f'A média das idades foi {media} anos\nA maior idade registrada foi {maior_idade} anos\nA menor idade registrada foi {menor_idade} anos\nEntre essas pessoas {bebe} são bebes\n{crianca} são crianças\n{pre_adolecente} são pré-adolecentes\n{adolecente} são adolecentes\n{jovem} são jovens\n{adulto} são adultos\n{idoso} são idosos\n')