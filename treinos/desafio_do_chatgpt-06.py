print('Desafio das N rainhas')
tabuleiro = []
for linha in range(8):
    tabuleiro.append(['_']*8)
for l in tabuleiro:
    for c in l:
        print(f'{c} ', end='')
    print()

print('\nOnde você quer colocar a rainha? ')
while True:
    linha_rainha = int(input('Linha: '))
    coluna_rainha = int(input('Coluna: '))
    if linha_rainha > 8 or coluna_rainha > 8 or coluna_rainha < 1 or linha_rainha < 1:
        print('Posição fora do tabuleiro')
        continue
    else:
        break
posicoes_ocupadas = []
conta_linha = linha_rainha-2
conta_coluna = coluna_rainha-2
for i in range(0,8):
    for h in range(8):
        if (linha_rainha-1) - 1 + h >= 0 and (coluna_rainha-1) - 1 + h >= 0:
            posicoes_ocupadas.append([(linha_rainha-1) - 1 + h, (coluna_rainha-1) - 1 + h])

        if (linha_rainha-1) - 1 + h >= 0 and (coluna_rainha-1) + 1 - h < 8:
            posicoes_ocupadas.append([(linha_rainha-1) - 1 + h, (coluna_rainha-1) + 1 - h])
        
        if (linha_rainha-1) + 1 - h < 8 and (coluna_rainha-1) - 1 + h >= 0:
            posicoes_ocupadas.append([(linha_rainha-1) + 1 - h, (coluna_rainha-1) - 1 + h])

        if (linha_rainha-1) + 1 - h < 8 and (coluna_rainha-1) + 1 - h < 8:
            posicoes_ocupadas.append([(linha_rainha-1) + 1 - h, (coluna_rainha-1) + 1 - h])
    posicoes_ocupadas.append([linha_rainha-1, i])
    posicoes_ocupadas.append([i, coluna_rainha-1])
        
for j in posicoes_ocupadas:
    linha, coluna = j[0], j[1]
    if 0 <= linha < 8 and 0 <= coluna < 8:
        tabuleiro[linha][coluna] = '\033[33mN\033[m'

tabuleiro[linha_rainha-1][coluna_rainha-1] = '\033[1;31mN\033[m'

for l in range(8):
    for c in range(8):
        if tabuleiro[l][c] == '_':
            tabuleiro[l][c] = '\033[1;32mN\033[m'

    
for l in tabuleiro:
    for c in l:
        print(f'{c} ', end='')
    print()
