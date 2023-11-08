n = int(input('Digite um número "n" de 1 a 50: '))

if n < 1 or n > 50:
    print('ERRO: n deve ser um inteiro entre 1 e 50')

else:
    for i in range(1,n+1):
        print(' '*(i-1)+str(i))
