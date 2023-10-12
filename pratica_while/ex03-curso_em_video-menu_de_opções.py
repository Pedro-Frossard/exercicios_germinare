'''
Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''
from time import sleep as sl

num1=int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro numero inteiro: '))

while True:
    print('[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa')
    escolha=int(input('Qual é a sua opção? '))
    if escolha ==1:
        print(f'{num1} + {num2} = {num1+num2}')
        print(f'='+10*'-=='+'-=')
        continue
    elif escolha == 2:
        print(f'{num1} x {num2} = {num1*num2}')
        print(f'='+10*'-=='+'-=')
        continue
    elif escolha == 3:
        print(f'O maior número entre {num1} e {num2} é o número {max(num2, num1)}')
        print(f'='+10*'-=='+'-=')
        continue
    elif escolha == 4:
        print('Informe outros números')
        num1=int(input('Digite um número inteiro: '))
        num2 = int(input('Digite outro numero inteiro: '))
        continue
    elif escolha == 5:
        print('Finalizando...')
        sl(2)
        print('Programa finalizado tenha um ótimo dia')
        print(f'='+20*'-=='+'-=')
        break
    else:
        print('Opção invalida tente novamente')
        continue