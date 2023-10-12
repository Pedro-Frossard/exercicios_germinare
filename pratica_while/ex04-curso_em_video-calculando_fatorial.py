'''
Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
'''


numero = int(input('Digite um número que eu vou calcular seu fatorial: '))
acumulador=numero
resultado=0
print(f'{numero}! = {numero}',end='')
while True:
    acumulador= acumulador-1
    if acumulador >= 1:
        print(f' x {acumulador}', end='')
        if acumulador == numero-1:
            resultado = acumulador * numero
            continue
        resultado = acumulador * resultado
        continue
            
    else:
        break
print(f' = {resultado}')