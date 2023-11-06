from time import sleep
from random import randint

jogadores = dict()

for i in range(4):
    jogadores[f'Jogador {i+1}'] = randint(1,6)

for chave, valor in jogadores.items():
    print(f'O {chave} jogou o dado e caiu {valor}')
    sleep(1)

ranking = sorted(jogadores.items(), key= lambda x: x[1], reverse=True)
for ordem, jogador in enumerate(ranking):
    print(f'{ordem+1}º lugar temos {jogador[0]} com {jogador[1]} pontos')
        