from random import randint

def verificarNumerosIguais(numeros):
    numeros_iguais = 0
    numero_repetido = 0
    for i, j in enumerate(numeros):
        if j in numeros[i+1:]:
            for h in numeros:
                if h == j:
                    numeros_iguais+=1
            numero_repetido=j
            break
    print(f'O número repetido foi o {numero_repetido}, existem {numeros_iguais}')

def verificarNumeroAleatorio(numeros,numero_aleatorio):
    quantidade_repetida = 0
    for i in numeros:
        if i == numero_aleatorio:
            quantidade_repetida+=1

    print(f'Existem {quantidade_repetida} numeros {numero_aleatorio} na tupla')
       
    
numeros = (5,10,6,7,5)
numero_aleatorio = randint(1,10)
verificarNumerosIguais(numeros)
verificarNumeroAleatorio(numeros, numero_aleatorio)
