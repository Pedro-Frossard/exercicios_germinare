from random import randint 
from time import sleep

print('JOGO DOS DADOS')
print('REGRAS:')
print('- Você começa com 100 pontos')
print('- Se a soma dos dados jogados for 7 ou 11 os pontos apostados dobram, caso contrario você perde 20 pontos')
print('- O jogo acaba quando você digitar um número negativo ou 0 na aposta ou se você não tiver mais pontos\n')
vezes_perdidas = vezes_ganhas = 0
pontos = 100
while True:
    aposta = int(input('Quantos pontos voce quer apostar nesta rodada (digite 0 ou um número negativo para parar)? '))
    if aposta > 0 and pontos > 0:
        if aposta > pontos:
            print('Aposte pontos que voce tem')
            continue
        dado1 = randint(1,6)
        dado2 = randint(1,6)
        soma = dado1 + dado2
        print('Jogando dados...')
        sleep(1.5)
        print(f'Os valores dos dados foram {dado1} e {dado2}')
        if soma == 7 or soma == 11:
            pontos+= aposta * 2
            print(f'A soma deles deu {soma}, agora você tem {pontos}')
            vezes_ganhas+=1
        elif soma != 7 and soma != 11:
            pontos-=20
            print(f'A soma deles deu {soma}, agora você tem {pontos}')
            vezes_perdidas+=1
    else:
        print(f'No final do jogo você ficou com {pontos} pontos\nNúmero de vitórias --> {vezes_ganhas}\nNúmero de derrotas --> {vezes_perdidas}')
        break