from random import randint


def numero_que_mais_apareceu(numeros):
    numeros_que_apareceram = [0 for i in range(10)]
    for indice, numero in enumerate(numeros_que_apareceram):
        numeros_que_apareceram[indice] = numeros.count(indice)
    return print(f'O maior número que mais apareceu foi o número {numeros_que_apareceram.index(max(numeros_que_apareceram))} que apareceu {numeros_que_apareceram[numeros_que_apareceram.index(max(numeros_que_apareceram))]} vezes')
    

def numero_que_menos_apareceu(numeros):
    numeros_que_menos_apareceram = [0 for i in range(10)]
    for indice, numero in enumerate(numeros_que_menos_apareceram):
        numeros_que_menos_apareceram[indice] = numeros.count(indice)
    return print(f'O maior número que menos apareceu foi o número {numeros_que_menos_apareceram.index(min(numeros_que_menos_apareceram))} que apareceu {numeros_que_menos_apareceram[numeros_que_menos_apareceram.index(min(numeros_que_menos_apareceram))]} vezes')


def maiorNumero(numeros):
    return print(f'\nO maior número sorteado foi o número {max(numeros)}')


def menorNumero(numeros):
    return print(f'O menor número sorteado foi o {min(numeros)}')


numeros = [randint(0,9) for i in range(1000)]



numero_que_mais_apareceu(numeros)
numero_que_menos_apareceu(numeros)
maiorNumero(numeros)
menorNumero(numeros)