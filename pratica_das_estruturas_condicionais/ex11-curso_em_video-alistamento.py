'''
Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
from datetime import date

nascimento= int(input('Em que ano você nasceu? '))
idade = date.today().year-nascimento

if idade == 18:
    print(f'A pessoa que nasceu em {nascimento} tem {idade} anos deve se alistar ainda este ano.')
elif idade < 18:
    print(f'A pessoa que nasceu em {nascimento} possuí {idade} anos se alistará em {18-idade} anos no ano de {(18-idade)+ date.today().year}')
else:
    print(f'A pessoa que nasceu em {nascimento} possuí {idade} anos e se alistou a {idade-18} anos no ano de {date.today().year-(idade-18)}')