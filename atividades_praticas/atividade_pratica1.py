def verificar_numero_armstrong(numero):
    tamanho= len(numero)
    numero_int=int(numero)
    if tamanho == 1:
        caractere1=int(numero[0])
        armstrong=bool(caractere1**tamanho==numero)
    elif tamanho == 2:
        caractere1=int(numero[0])
        caractere2=int(numero[1])
        armstrong=bool(caractere1**tamanho+caractere2**tamanho==numero)
    elif tamanho == 3:
        caractere1=int(numero[0])
        caractere2=int(numero[1])
        caractere3=int(numero[2])
        armstrong=bool(caractere1**tamanho+caractere2**tamanho+caractere3**tamanho==numero)
    elif tamanho == 4:
        caractere1=int(numero[0])
        caractere2=int(numero[1])
        caractere3=int(numero[2])
        caractere4=int(numero[3])
        armstrong=bool(caractere1**tamanho+caractere2**tamanho+caractere3**tamanho+caractere4**tamanho==numero)

    return armstrong

def verificar_palindromo(numero):
    palindromo= (numero[::-1]==numero)
    return palindromo
    

numero=input('Digite um número inteiro: ')
verificar_numero_armstrong(numero)
verificar_palindromo(numero)
if verificar_numero_armstrong == True:
    print(f'O número {numero} é Armstrong')
elif verificar_palindromo == True:
    print(f'O número não é armstrong, mas é um palindromo')
else:
    print('O número não é nenhum dos dois')