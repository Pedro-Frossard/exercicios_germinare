def mostrarTabela(produtos,precos):
    print('Produtos'+'.'*42+'Preços')
    
    for produto, preco in zip(produtos, precos):
        print(f'{produto}{(50-len(produto))*"."}R$ {preco:.2f}')


def principaisPrecos(produtos,precos):
    print()
    valor_maior = max(precos)
    valor_menor = min(precos)
    posicao_maior = precos.index(valor_maior)
    posicao_menor = precos.index(valor_menor)
    print(f'Produto mais caro\n{produtos[posicao_maior]} --> R${valor_maior:.2f}\n\nProduto mais barato\n{produtos[posicao_menor]} --> R${valor_menor:.2f}')


def somarIndicesPares(precos):
    acumulador = 0
    for index , valor in enumerate(precos):
        if index == 0 or index % 2 == 0:
            acumulador+= valor
    print()
    print(f'A soma de todos os produtos que estão em indices pares é R${acumulador:.2f}')


produtos = ('Pão de queijo 400g','Salsicha Hot-dog 500g','Pão de alho baguete 400g','Filé de Peito de Frango 1Kg','Isca de Frango 300g','Linguiça toscana 700g','Pedaço de Filé de Salmão 500g','Filé de Tilápia 250g','Bife de Filé Mignon MAIS 900g','Carne moída patinho 900g')
precos = (10.76,9.96,10.96,19.96,13.96,17.96,54.96,13.96,89.96,39.97)


mostrarTabela(produtos, precos)
principaisPrecos(produtos,precos)
somarIndicesPares(precos)