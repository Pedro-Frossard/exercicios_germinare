numeros_por_extenso = ('um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete','oito','nove','dez')

while True:
    numero_inteiro = int(input('Digite um número de 1-10: '))
    if 1 <= numero_inteiro <= 10:
        print(f'Você digitou o número {numeros_por_extenso[numero_inteiro-1]}')

    else:
        print('FIM!!')
        break

