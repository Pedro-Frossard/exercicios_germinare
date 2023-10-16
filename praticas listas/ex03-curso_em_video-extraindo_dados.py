numeros = []

while True:
    numero = int(input('Digite um número: '))
    numeros.append(numero)
    sair = input('Quer sair? ').lower()
    if sair.startswith('s'):
        numeros.sort()
        numeros.reverse()
        print(f'Os números em ordem decrescente são {numeros}')
        if 5 in numeros:
            print(f'Você digitou o número 5 e ele está na {numeros.index(5)+1}º posição da lista')
        else:
            print('Você não digitou o número 5')
        break