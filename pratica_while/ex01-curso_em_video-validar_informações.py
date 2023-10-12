'''Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

while True:
    sexo = input('Digite o seu sexo (M = masculino, F = feminino, P = prefiro não dizer): ')
    if sexo.upper() == 'M' or sexo.upper() == 'F':
        print(f'Sexo "{sexo.upper()}" registrado com sucesso')
        break
    elif sexo.upper() == 'P':
        print('Sexo desconhecido')
        break
    else:
        print('Por favor digite alguma das opções')
        continue