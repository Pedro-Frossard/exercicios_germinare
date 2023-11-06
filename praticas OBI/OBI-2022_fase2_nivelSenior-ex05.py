linhas_colunas = int(input())
piramide = [[0] * linhas_colunas for h in range(linhas_colunas)]
for i in range(linhas_colunas // 2 + 1):
    for j in range(i, linhas_colunas - i):
        piramide[i][j] = i
        piramide[linhas_colunas - 1 - i][j] = i
        piramide[j][i] = i
        piramide[j][linhas_colunas - 1 - i] = i

for l in piramide:
    for c in l:
        print(f'{c:^3}',end=' ')
    print()
