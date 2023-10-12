acumulador = contador = 0

while True:
    numero = int(input('Digite um número inteiro ou um número negativo para parar: '))
    numeros_impares = numero
    if numeros_impares > 0:
        if numeros_impares%2==0:
            numeros_impares-=1
            acumulador+=numeros_impares
            contador+=1
            print(f'{numeros_impares} --> ', end = '') 
        while numeros_impares > 1:
            numeros_impares-=2
            acumulador+=numeros_impares
            contador+=1
            print(f'{numeros_impares} --> ', end = '')
        print('Fim')
        print(f'A soma de todos estes {contador} números ímpares menores que {numero} é igual a {acumulador}')
    else:
       print('Acabou!')  
       break 