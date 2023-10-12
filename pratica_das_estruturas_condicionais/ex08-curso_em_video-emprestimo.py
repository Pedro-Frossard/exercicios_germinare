'''
Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''

valor_casa= float(input('Qual é o valor da casa? R$ '))
salario= float(input('Quanto você ganha por mês? R$ '))
anos = int(input('Por quantos anos será o financiamento? '))

prestacao= valor_casa/(anos*12)
porcentagem_salario = salario*30/100
if porcentagem_salario <= prestacao:
    print(f'Para comprar uma casa de R${valor_casa:.2f} em um financiamento de {anos} anos. A prestacao será de R${prestacao:.2f}\nEMPRÉSTIMO NEGADO')
elif porcentagem_salario>prestacao:
    print(f'Para comprar uma casa de R${valor_casa:.2f} em um financiamento de {anos} anos. A prestacao será de R${prestacao:.2f}\nEMPRÉSTIMO APROVADO')

