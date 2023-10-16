lista = []
pares =[]
impares = []

while True:
    numero = int(input('Digite um número: '))
    lista.append(numero)
    if numero%2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
    sair = input('Deseja sair? ').lower()
    if sair.startswith('s'):
        print(f'Todos os números digitados são {lista}')
        print(f'Os números pares são {pares}')
        print(f'Os números impares são {impares}')
        break