'''
Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
'''

salario_inicial=float(input('Qual é o salario do funcionario? R$ '))

if salario_inicial<1250:
    aumento=(salario_inicial*115)/100
    print(f'O aumento deste funcionario foi de R${aumento:.2f}')
    
else:
    aumento=salario_inicial*110/100
    print(f'O aumento deste funcionario foi de R${aumento:.2f}')