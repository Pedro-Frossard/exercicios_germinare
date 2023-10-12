from random import randint
print(40*'-')
print('        VAMOS JOGAR PAR E ÍMPAR')
print(40*'-')

numero_vitorias = 0
while True:
    numero_comput = randint(0,10)
    numero = int(input('Digite um valor: '))
    if numero < 0 or numero > 10: 
        print('Por favor digite um número entre 0 e 10')
        continue
    escolha = input('Par ou Ímpar? ').upper()
    if escolha.startswith('P'):
        soma = numero_comput + numero
        if soma % 2 == 0:
            print(f'Você jogou {numero} e eu joguei {numero_comput} a soma dos dois é {soma}')
            print('O número é PAR, você venceu!!')
            print('Vamos jogar novamente...')
            print(40*'-')
            numero_vitorias +=1
            continue
        elif soma % 2 == 1:
            print(f'Você jogou {numero} e eu joguei {numero_comput} a soma dos dois é {soma}')
            print('O número é ÍMPAR, você perdeu')
            print(f'Número de vitorias: {numero_vitorias}')
            print(40*'-')
            break
    elif escolha.startswith('I') or escolha.startswith('Í'):
        soma = numero_comput + numero
        if soma % 2 == 1:
            print(f'Você jogou {numero} e eu joguei {numero_comput} a soma dos dois é {soma}')
            print('O número é Ímpar, você venceu!!')
            print('Vamos jogar novamente...')
            print(40*'-')
            numero_vitorias +=1
            continue
        elif soma % 2 == 0:
            print(f'Você jogou {numero} e eu joguei {numero_comput} a soma dos dois é {soma}')
            print('O número é PAR, você perdeu')
            print(f'Número de vitorias: {numero_vitorias}')
            print(40*'-')
            break
    else:
        print('Digite uma opção valida')
        continue