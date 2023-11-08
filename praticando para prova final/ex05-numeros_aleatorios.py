import random

n = int(input('Informe a quantidade de números desejados: '))

soma_numeros_positivos = 0
soma_numeros_negativos = 0
print('\nNUMEROS GERADOS AUTOMATICAMENTE:')

for i in range(n):
    numero_aleatorio = random.randint(-40, 40)
    print(numero_aleatorio, end=' ')
    if numero_aleatorio < 0:
        soma_numeros_negativos+=numero_aleatorio
    elif numero_aleatorio > 0:
        soma_numeros_positivos+=numero_aleatorio

print(f'\n\nSOMA DOS NÚMEROS POSITIVOS: {soma_numeros_positivos}\nSOMA DOS NÚMERO NEGATIVOS: {soma_numeros_negativos}')