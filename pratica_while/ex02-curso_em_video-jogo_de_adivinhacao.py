'''
Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
'''
from time import sleep
from random import randint

tentativas=0
print('Olá, sou seu computador\nAcabei de pensar em um número de 0 a 10\nConsegue adivinhar qual foi?')
numero_pensado=randint(0,10)
while True:
    numero=int(input('Qual é seu palpite? '))
    if numero == numero_pensado:
        print('Parabéns! Você adivinhou o número')
        tentativas= tentativas + 1
        print('O número de tentativas foi', tentativas)
        break
    elif numero > numero_pensado:
        print('Hmmm, o número que eu pensei é menor')
        tentativas= tentativas + 1
        continue
    elif numero < numero_pensado:
        print('Hmmm, o número é um pouco maior')
        tentativas= tentativas + 1
        continue
    