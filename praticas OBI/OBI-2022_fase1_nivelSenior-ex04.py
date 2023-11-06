linhas_colunas = int(input())
quadrado = []
for numero in range(linhas_colunas):
    numeros = input().split()
    quadrado.append(numeros)

for i in range(linhas_colunas):
    for j in range(linhas_colunas):
        quadrado[i][j] = int(quadrado[i][j])

for ordem, linha in enumerate(quadrado):
    if 0 in linha:
        soma_linha_0 = sum(linha)
        posicao_0 = [ordem, linha.index(0)]
        continue
    else:
        soma = sum(linha)
print(soma-soma_linha_0)
print(posicao_0[0]+1)
print(posicao_0[1]+1)