import math
import random

def calcular_fatorial(numero):
    return math.factorial(numero)

a = random.randint(0, 20)
b = random.randint(0, 20)

fatorial_a = calcular_fatorial(a)
fatorial_b = calcular_fatorial(b)

soma_fatoriais = fatorial_a + fatorial_b

print(f'Valor de A: {a}')
print(f'Fatorial de A ({a}!): {fatorial_a}')
print(f'Valor de B: {b}')
print(f'Fatorial de B ({b}!): {fatorial_b}')
print(f'Soma dos fatoriais: {soma_fatoriais}')
