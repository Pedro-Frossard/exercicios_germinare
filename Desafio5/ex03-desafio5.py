posicao1 = posicao2 = posicao3 = posicao4 = 0 
while True:
    numero = int(input('Digite um número entre 0 --> 100 ou negativo para sair: '))
    if numero > 0:
        if numero > 100:
            print('Digite um número valido')
        else:
            if numero <= 25:
                posicao1+=1
            elif numero > 25 and numero <=50:
                posicao2+=1
            elif numero > 50 and numero <=75:
                posicao3+=1
            elif numero > 75 and numero <=100:
                posicao4+=1
    else:
        print(f'No intervalo de 0-25 --> você digitou {posicao1} vezes\nNo intervalo de 26-50 --> você digitou {posicao2} vezes\nNo intervalo de 51-75 --> você digitou {posicao3} vezes\nNo intervalo de 76-100 --> você digitou {posicao4} vezes')
        break