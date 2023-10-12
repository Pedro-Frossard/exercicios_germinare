termo1 = termo3 = contador = 0
termo2 = 1
termo = int(input('Digite um número inteiro positivo: '))

while contador < termo:
    contador+=1
    if termo3 == termo:
        print(f'O número {termo} está na sequencia de Fibonacci e está no indice {contador}')
        break
    termo1 = termo2
    termo2 = termo3
    termo3 = termo1 + termo2

if termo3 != termo:
    print(f'O número {termo} não está na sequencia de Fibonacci')
