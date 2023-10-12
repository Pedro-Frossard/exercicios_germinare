'''
O professor de matemática da Germinare Business pediu sua ajudar para criar um programa
para crianças que estão aprendendo multiplicação de números inteiros (mas vamos começar
com algo simples, com números menores do que 20).
O programa deve escolher números aleatórios entre 1 e 20, e mostre na tela a pergunta: “qual é
o resultado de a x b”, onde a e b são os números aleatórios. Peça a resposta do usuário. Faça
cinco perguntas ao aluno, e mostre para ele as perguntas e as respostas corretas, além de
quantas vezes o aluno acertou.
'''

from random import randint

a=randint(1,20)
b=randint(1,20)
acertos=0
resposta = int(input(f'Pergunta: {a} x {b} = '))
if resposta == a*b:
    print('Acertou!')
    acertos+=1
    print(f'Acertos atuais: {acertos}')
elif resposta != a*b:
    print(f'Errou\nA resposta correta era {a*b}')
    print(f'Acertos atuais: {acertos}')

a=randint(1,20)
b=randint(1,20)
resposta = int(input(f'Pergunta: {a} x {b} = '))
if resposta == a*b:
    print('Acertou!')
    acertos+=1
    print(f'Acertos atuais: {acertos}')
elif resposta != a*b:
    print(f'Errou\nA resposta correta era {a*b}')
    print(f'Acertos atuais: {acertos}')

a=randint(1,20)
b=randint(1,20)
resposta = int(input(f'Pergunta: {a} x {b} = '))
if resposta == a*b:
    print('Acertou!')
    acertos+=1
    print(f'Acertos atuais: {acertos}')
elif resposta != a*b:
    print(f'Errou\nA resposta correta era {a*b}')
    print(f'Acertos atuais: {acertos}')

a=randint(1,20)
b=randint(1,20)
resposta = int(input(f'Pergunta: {a} x {b} = '))
if resposta == a*b:
    print('Acertou!')
    acertos+=1
    print(f'Acertos atuais: {acertos}')
elif resposta != a*b:
    print(f'Errou\nA resposta correta era {a*b}')
    print(f'Acertos atuais: {acertos}')

a=randint(1,20)
b=randint(1,20)
resposta = int(input(f'Pergunta: {a} x {b} = '))
if resposta == a*b:
    print('Acertou!')
    acertos+=1
    print(f'Acertos atuais: {acertos}')
elif resposta != a*b:
    print(f'Errou\nA resposta correta era {a*b}')
    print(f'Acertos atuais: {acertos}')
