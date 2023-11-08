def converterDecimal(numero_dec):
    numeros_binarios = []
    while True:
        numeros_binarios.append(numero_dec%2)
        numero_dec//=2
        if numero_dec == 0 or numero_dec == 1:
            numeros_binarios.append(numero_dec)
            numeros_binarios.reverse()
            print('O número convertido para binario será ', end='')
            break
    for binario in numeros_binarios:
        print(binario,end='')



while True:
    numero_dec = int(input('\nNumero: '))

    if  numero_dec <= 0 or numero_dec >= 255:
        print('Número invalido para conversão para binario de 8 bits')
        continue
    else:
        converterDecimal(numero_dec)
        break