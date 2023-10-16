numeros = []

while True:
    numero = int(input('Digite um número: '))
    if numero in numeros:
        print('Este valor ja tem na lista')
        continue
    else:
        numeros.append(numero)
        print('Valor guardado com sucesso')
    
    sair = input('Deseja sair? [S/N] ').lower()
    if sair.startswith('s'):
        numeros.sort()
        print('Os números digitados foram', numeros)
        break
    else:
        continue