'''
Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
'''

velocidade_carro=int(input('A quantos Km/h você estava dirigindo? '))

if velocidade_carro > 80:
    multa=(velocidade_carro-80)*7
    print(f'MULTADO!! Você excedeu o limite de 80Km/h. Por isso você recebeu uma multa de R${multa:.2f}')

else:
    print('Tenha um bom dia! Dirija com segurança.')