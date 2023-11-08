'''
Menor que 65Kg Pena
Maior ou igual a 65Kg e menor que 72Kg Leve
Maior ou igual a 72Kg e menor que 79Kg Ligeiro
Maior ou igual a 79Kg e menor que 86Kg Meio-médio
Maior ou igual a 86Kg e menor que 93Kg Médio
Maior ou igual a 93Kg e menor que 100Kg Meio-pesado
Maior ou igual a 100Kg Pesado
'''

nome = input('Qual é o nome do lutador? ')
peso = float(input('Peso: '))

if peso < 65:
    print(f'O lutador {nome.title()} pesa {peso} Kg e se enquadra na categoria Pena!')
elif peso >= 65 and peso < 72:
    print(f'O lutador {nome.title()} pesa {peso} Kg e se enquadra na categoria Leve!')
elif 72 <= peso < 79:
    print(f'O lutador {nome.title()} pesa {peso} Kg e se enquadra na categoria Ligeiro!')
elif peso >= 79 and peso < 86:
    print(f'O lutador {nome.title()} pesa {peso} Kg e se enquadra na categoria Meio-médio!')
elif peso >= 86 and peso < 93:
    print(f'O lutador {nome.title()} pesa {peso} Kg e se enquadra na categoria Médio!')
elif peso >= 93 and peso < 100:
    print(f'O lutador {nome.title()} pesa {peso} Kg e se enquadra na categoria Meio-pesado!')
elif peso > 100:
    print(f'O lutador {nome.title()} pesa {peso} Kg e se enquadra na categoria Pesado!')