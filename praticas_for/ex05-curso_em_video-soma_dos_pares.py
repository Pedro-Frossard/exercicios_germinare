soma_par = soma_impar = 0

for i in range(0,6):
    numero = int(input('Digie um número positivo: '))
    if numero % 2 == 0:
        soma_par+=numero
    else:
        soma_impar+=numero

print(f'A soma dos números pares digitados é igual a {soma_par}\nA soma dos número ímpares digitados é igual a {soma_impar}')
