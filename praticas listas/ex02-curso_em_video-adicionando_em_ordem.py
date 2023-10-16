lista = []

for i in range(5):
    numero = int(input('Digite um número: '))
    if i == 0 or numero > max(lista):
        lista.append(numero)
        print(lista)
    else:
        for posicao, numeros in enumerate(lista):
            if numero <= numeros:
                lista.insert(posicao, numero)
                print(lista)
                break
            