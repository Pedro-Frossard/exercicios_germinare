'''
Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
'''

from datetime import date

ano=int(input('Digite um ano que eu vou falar se é bissexto ou não (digite 0 se quiser ver o ano atual): '))

if ano == 0:
    ano_atual=date.today().year
    if ano_atual % 4 == 0 and ano_atual % 100 != 0 or ano_atual % 400 == 0:
        print(f'O ano atual {ano_atual} é bissexto')
    else:
        print(f'O ano atual {ano_atual} não é bissexto')

elif ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto')