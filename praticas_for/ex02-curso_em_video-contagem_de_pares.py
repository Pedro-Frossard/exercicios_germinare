limite = int(input('Digite um número que eu direi todos os pares até ele: '))
if limite < 0:
    print('Não pode haver um limite negativo')

else:
    for i in range(0,limite+1,2):
        if i == limite - 1 or i == limite:
            print(i)
        else:
            print(f'{i} --> ', end = '')
        
        