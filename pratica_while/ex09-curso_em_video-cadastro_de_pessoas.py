maior_idade = menor_idade = num_homens = num_mulheres = 0
while True:
    print('CADASTRE UMA PESSOA')
    print('')
    idade = int(input('Qual é a idade da pessoa cadastrada? '))
    sexo = input('Qual é o sexo da pessoa [M/F]: ').upper()
    sair = input('Deseja continuar? ').upper()
    if idade < 0 or idade > 150:
            print('Digite uma idade real')
            continue
    if sexo.startswith('M') == False and sexo.startswith('F') == False:
            print('Digite uma das opções')
            continue
    if idade >= 18:
            maior_idade += 1
    elif idade < 18:
            menor_idade += 1
    if sexo.startswith('M'):
            num_homens+=1
    elif sexo.startswith('F'):
            num_mulheres+=1

    if sair.startswith('N'):
        print(f'Total de pessoas maiores de idade: {maior_idade}\nTotal de pessoas menores de idade: {menor_idade}\nTotal de homens: {num_homens}\nTotal de mulheres: {num_mulheres}')
        break
