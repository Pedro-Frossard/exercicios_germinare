from time import sleep
while True:
    contador = 0
    contagem = 1
    x = int(input('Digite um número inteiro positivo ou um número negativo para sair: '))
    if x > 0:
        while contagem > 0:
            contagem = x-contador
            print(contagem)
            contador+=1
            sleep(1)
    else:
        print('Acabou')
        break