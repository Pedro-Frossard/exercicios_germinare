numero = int(input('Digite um número que eu direi a tabuada dele até o 20: '))
if numero > 0:
    for i in range(1,21):
        print(f'{numero} x {i} = {numero*i}')

else:
    print('Digite um número positivo maior que 0')