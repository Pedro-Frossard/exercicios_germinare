def verificar_matriz_simetrica(matriz):
    linha_coluna_iguais = 0
    for l in range(3):
        for c in range(3):
            coluna = [matriz[0][c+linha_coluna_iguais], matriz[1][c+linha_coluna_iguais], matriz[2][c+linha_coluna_iguais]]
            if matriz[l] == coluna:
                linha_coluna_iguais+=1
                break
    if linha_coluna_iguais == 3:
        return True
    else:
        return False

        




matriz = [[0,0,0],
          [0,0,0],
          [0,0,0]
    ]   

for linha in range(3):
    for coluna in range(3):
        valor = int(input(f'Digite um valor para a posição [{linha}, {coluna}]: '))
        matriz[linha][coluna] = valor

if verificar_matriz_simetrica(matriz):
    print('A matriz é simétrica')
else:
    print('A matriz não é simetrica')

