from random import randint

print('\033[31m> Cassino <\033[m'.center(30, '-'))
dinheiro_total = float(input('Com quantos reais você quer jogar? R$'))
numeros = []
vezes_aparecidas = total_ganho = total_perdido = vitorias = derrotas = 0

if dinheiro_total >= 0:
       while True:
        numeros.clear()
        aposta = float(input('Digite quanto que você quer apostar ou um número negativo para parar: R$'))
        if aposta <= 0 or dinheiro_total <=0:
            print(f'Saldo total final: R${dinheiro_total:.2f}\nVezes ganhas: {vitorias}\nVezes perdidas: {derrotas}\nDinheiro ganho: R${total_ganho:.2f}\nDinheiro perdido: R${total_perdido:.2f}')
            break
        else:
            if aposta > dinheiro_total:
                print('Não é possível apostar mais do que você tem')
                print()
                continue
            else:
                numero_escolhido = int(input('Digite um número de 0 a 100: '))
                if numero_escolhido < 0 or numero_escolhido > 100:
                    print('Escolha um número válido')
                    continue
                else:
                    for i in range(0,15):
                        numeros.append(randint(0,100))
                        if numero_escolhido == numeros[len(numeros)-1]:
                            vezes_aparecidas +=1
                    print('Os números selecionados foram: ', end='')
                    for j in range(0,15):
                        print(numeros[j],end=' - ')
                    print('Fim')
                    print()
                    if vezes_aparecidas == 1:
                        dinheiro_total+=aposta*5
                        print(f'O numero {numero_escolhido} apareceu {vezes_aparecidas} vezes, por isso agora você tem R${dinheiro_total:.2f}')
                        print()
                        total_ganho+= aposta*5
                        vitorias+=1
                    elif vezes_aparecidas == 2:
                        dinheiro_total+=aposta*10
                        print(f'O numero {numero_escolhido} apareceu {vezes_aparecidas} vezes, por isso agora você tem R${dinheiro_total:.2f}')
                        print()
                        total_ganho+= aposta*10
                        vitorias+=1
                    elif vezes_aparecidas >= 3:
                        dinheiro_total+=aposta*20
                        print(f'O numero {numero_escolhido} apareceu {vezes_aparecidas} vezes, por isso agora você tem R${dinheiro_total:.2f}')
                        print()
                        total_ganho+= aposta*20
                        vitorias+=1
                    else:
                        dinheiro_total-= aposta 
                        print(f'O numero {numero_escolhido} não apareceu nenhuma vez, por isso você perdeu R${aposta:.2f} e agora você tem R${dinheiro_total:.2f}')
                        print()
                        total_perdido+= aposta
                        derrotas+=1
else:
    print('Número inválido')

