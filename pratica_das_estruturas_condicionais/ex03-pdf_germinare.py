'''
Crie um programa que gere um número inteiro aleatório entre 1-10 e você deve adivinhar que número foi
escolhido pelo computador. O seu programa deve ser capaz de dizer se o seu “chute” foi certeiro (acertou o
número), se foi maior ou menor.
'''
from random import randint

numero_aleatorio= randint(1,10)
numero_escolhido= int(input('Escolha um número de 1 a 10: '))

if numero_aleatorio == numero_escolhido:
    print('Parabéns, você acertou o número!!!!')

elif numero_aleatorio < numero_escolhido:
    print(f'Você não acertou, o número {numero_escolhido} foi maior.')

else:
    print(f'Você não acertou, o número {numero_escolhido} foi menor.')
    