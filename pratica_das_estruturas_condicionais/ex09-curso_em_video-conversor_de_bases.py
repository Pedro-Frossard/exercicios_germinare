'''
Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
'''

numero = int(input('Digite um número inteiro: '))
print('Escolha ua das bases para a conversão\n[ 1 ] BINÁRIO\n[ 2 ] HEXADECIMAL\n[ 3 ] OCTAL')
escolha = int(input('Digite o número da sua opção: '))
if escolha == 1:
    print(f'O número {numero} em binário é igual a {bin(numero)[2:]}')
elif escolha == 2:
    print(f'O número {numero} em hexadecimal é igual a {hex(numero)[2:]}')
elif escolha == 3:
    print(f'O número {numero} em octal é igual a {oct(numero)[2:]}')
else:
    print('Digite uma escolha valida')
