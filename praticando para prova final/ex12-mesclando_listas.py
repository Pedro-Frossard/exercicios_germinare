from random import randint


numero_elementos_lista1 = int(input('Quantos elementos deve ter a lista 1? '))
numero_elementos_lista2 = int(input('Quantos elementos deve ter a lista 2? '))
lista1= []
lista2 = []
if numero_elementos_lista1 <=0 or numero_elementos_lista2 <= 0:
    print('Numero invalido')
else:
    for i in range(numero_elementos_lista1):
        lista1.append(randint(0,50))
    print(f'Lista 1 = {lista1}')
    for j in range(numero_elementos_lista2):
        lista2.append(randint(0,50))
    print(f'Lista 2 = {lista2}')

    if numero_elementos_lista1 > numero_elementos_lista2:
        maior = lista1

    else:
        maior = lista2
    lista_mesclada = []
    for lista in range(len(maior)):
        if lista >= len(lista1):
            for i in lista2[lista:]:
                lista_mesclada.append(i)
            break
        elif lista >= len(lista2):
            for j in lista1[lista:]:
                lista_mesclada.append(j)
            break
        else:
            lista_mesclada.append(lista1[lista])
            lista_mesclada.append(lista2[lista])

    print(f'lista resultante = {lista_mesclada}')