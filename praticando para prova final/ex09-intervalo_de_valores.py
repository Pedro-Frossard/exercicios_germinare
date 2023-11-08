inicio = int(input('Qual deve ser o inicio do intervalo? '))

fim = int(input('Qual deve ser o fim do intervalo? '))

if inicio > fim:
    print('Você digitou um inicio maior que o fim, mesmo assim eu inverterei os valores')
    print(f'Os numeros divisiveis por 5 no intervalo de {fim} a {inicio} são: ')
    for numero in range(fim, inicio+1):
        if numero%5 == 0:
            print(numero, end='  ')

else:
    print(f'Os numeros divisiveis por 5 no intervalo de {inicio} a {fim} são: ')
    for numero in range(inicio, fim+1):
        if numero%5 == 0:
            print(numero, end='  ')