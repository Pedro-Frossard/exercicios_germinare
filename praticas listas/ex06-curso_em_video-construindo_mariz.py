matriz = []

coluna_linha = int(input('Digite quantas colunas e linhas a matriz terá: '))
for coluna in range(coluna_linha):
    matriz.append([0]*coluna_linha)
    for linha in range(coluna_linha):
        numero = int(input(f'Digite um valor para a posição {coluna},{linha}: '))
        matriz[coluna][linha] = numero
for l in range(coluna_linha):
    for c in range(coluna_linha):
        print(f'[{matriz[coluna][linha]}]', end = '')
    print()