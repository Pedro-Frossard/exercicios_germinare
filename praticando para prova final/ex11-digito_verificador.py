numero = input('Digite um número inteiro positivo de 10 digitos: ')

if len(numero) == 10 and numero.isdigit() and int(numero) >= 0:
    acumulador = 0
    for num in numero:
        acumulador+=int(num)
    media = acumulador / 10 
    digito_verificador = media//1
    print(f'A média dos digitos do número somados é igual a {media} e seu digito verificador é {int(digito_verificador)}')

else:
    print('Número invalido')

