'''
Suponha que queremos descobrir se três números (A, B e C) podem ser usados como lados de um
triângulo. Obviamente os três valores têm que ser positivos e não nulos mas, além disso, em um triângulo
vale a propriedade de que cada um dos seus lados é menor do que a soma dos outros dois lados.
A < (B+C) e B < (A+C) e C < (B+A)
'''

# Saber os lados do triangulo

A=float(input('Digite uma medida: '))
B=float(input('Digite outra medida: '))
C=float(input('Digite mais uma medida: '))

# Ver se os números estão de acordo com as restrições
if A>0 and B>0 and C>0:
    if A < B+C and B < A+C and C < B+A: # Validar se auilo é ou não um triângulo
        print(f'O poligono de medidas {A}, {B} e {C} é um triângulo!!!!')

    else:
        print(f'O poligono de medidas {A}, {B} e {C} não é um triângulo.')
else:
    print('Digite medidas validas')
