numero = int(input('Digite um número para ver se ele é primo ou não: '))
contador = 0

for i in range(1,numero+1):
    if numero%i == 0:
        print(f'\033[33m{i}\033[m', end = ' ')
        contador+=1
    else:
        print(f'\033[31m{i}\033[m', end = ' ')

print()
print(f'O número {numero} foi divisível {contador} vezes')
if contador == 2:
    print('Por isso ele é um número PRIMO')
else:
    print('Por isso ele NÂO é um número PRIMO')