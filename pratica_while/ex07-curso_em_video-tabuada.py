while True:
    contador = 0
    valor1 = int(input('Digite um valor: '))
    valor2 = int(input('Digite outro valor ou um número negativo para sair: '))
    if valor2 < 0:
        print('Fim!')
        break
    print(40*'-')
    
    while True:
        contador+=1
        print(f'{valor1} x {contador} = {valor1*contador}')
        if contador >= valor2:
            print(40*'-')
            break