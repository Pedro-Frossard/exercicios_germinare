'''
Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 

Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8'''

termos_mostrados = sequencia_anterior = sequencia_posterior = 0
sequencia = 1
print(20*'-')
print('Sequencia de Fibonacci')
print(20*'-')

termos = int(input('Quantos termos você quer mostrar? '))
print(50*'~')

while termos > termos_mostrados:
    print(f'{sequencia_posterior} - ', end='')
    sequencia_anterior=sequencia
    sequencia = sequencia_posterior
    sequencia_posterior = sequencia_anterior+ sequencia
    termos_mostrados+=1 

print('Fim')
print(50*'~')