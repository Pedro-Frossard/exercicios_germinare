A = int(input('Digite o lado 1 do triangulo: '))
B = int(input('Digite o lado 2 do triangulo: '))
C = int(input('Digite o lado 3 do triangulo: '))

if A+B > C and B+C > A and A+C > B:
    print('Essas medidas podem formar um triangulo')
else:
    print('Essas medidas não podem formar um triangulo')