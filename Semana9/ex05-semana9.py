jogo_da_velha = [['_','_','_'],['_','_','_'],['_','_','_']]
contador = 1
jogador1_ganhador = jogador2_ganhador = 0
while True:
    if contador%2 == 1:
        print('\033[31mJogador 1\033[m')
        jogador_atual = 'Jogador 1'
    else:
        print('\033[32mJogador 2\033[m')
        jogador_atual = 'Jogador 2'
    for l in jogo_da_velha:
        for c in l:
            print(f'{c}  ', end='')
        print()
    print()
    while True:    
        linha = int(input('Linha: '))
        coluna = int(input('Coluna: '))
        if linha > 3 or coluna > 3:
            print(f'Opção invalida. O jogo tem apenas 3 linhas e 3 colunas\nJogue novamente {jogador_atual}')
            continue
        if jogo_da_velha[linha-1][coluna-1]!='_':
            print(f'A casa selecionada esta ocupada. Jogue novamente {jogador_atual}')
            break
        else:
            contador+=1
            if jogador_atual == 'Jogador 1':
                jogo_da_velha[linha-1][coluna-1] = 'X'
            elif jogador_atual == 'Jogador 2':
                jogo_da_velha[linha-1][coluna-1] = 'O'
            for l in jogo_da_velha:
                if l == ['X', 'X', 'X']:
                    jogador1_ganhador+=3
                    break
                elif l == ['O', 'O', 'O']:
                    jogador2_ganhador+=3
                    break
            if jogador1_ganhador == 3 or jogador2_ganhador == 3:
                break
            for l in range(0,3):
                jogador1_ganhador = 0
                jogador2_ganhador = 0
                for c in range(0,3):
                    if jogo_da_velha[l][c] == 'X':
                        jogador1_ganhador +=1
                    elif jogo_da_velha[l][c] == 'O':
                        jogador2_ganhador+=1
            if jogador2_ganhador < 3 and jogador1_ganhador < 3:
                jogador2_ganhador = 0
                jogador1_ganhador = 0
                if (jogo_da_velha[0][0] == 'X' and jogo_da_velha[1][1] == 'X' and jogo_da_velha[2][2] == 'X') or (jogo_da_velha[0][2] == 'X' and jogo_da_velha[1][1] == 'X' and jogo_da_velha[2][0] == 'X'):
                    jogador1_ganhador+=3
                    break
                elif (jogo_da_velha[0][0] == 'O' and jogo_da_velha[1][1] == 'O' and jogo_da_velha[2][2] == 'O') or (jogo_da_velha[0][2] == 'O' and jogo_da_velha[1][1] == 'O' and jogo_da_velha[2][0] == 'O'):
                    jogador2_ganhador+=3
                    break
                else:
                    break
    if jogador1_ganhador == 3:
        print(f'Jogador 1 venceu após {contador-1} rodadas')
        break
    elif jogador2_ganhador == 3:
        print(f'Jogador 2 venceu após {contador-1} rodadas')
        break
    if '_' not in jogo_da_velha[0] and '_' not in jogo_da_velha[1] and '_' not in jogo_da_velha[2]:
        print('Empate!!')
        break
    else:
        jogador1_ganhador = 0
        jogador2_ganhador = 0
        continue

