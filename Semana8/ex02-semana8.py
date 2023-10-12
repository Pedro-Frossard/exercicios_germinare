def atualizarEstoque(estoque,pedidos,estoque_minimo):
    novo_estoque = set()
    produtos_pouco_estoque = set()
    for i, j in enumerate(estoque):
        produto_em_estoque, preco, quantidade_estoque = j
        for h, y in enumerate(pedidos):
                produto, quantidade = y
                if produto_em_estoque == produto:
                    produto_novo = (produto_em_estoque, preco, quantidade_estoque - quantidade)
                    novo_estoque.add(produto_novo)
                    if quantidade_estoque - quantidade < estoque_minimo:
                         produtos_pouco_estoque.add(produto_novo)
    return print(f'Os produtos com o estoque menor que o limite mínimo foram \n{produtos_pouco_estoque}')



estoque = {
    ('Camiseta',20.0,40),
    ('Sapato', 80.0,15),
    ('Moletom',60.0,20),
    ('Óculos escuro', 30.0, 30),
    ('Meia', 15.0, 50)
}

pedidos = {
    ('Sapato', 2),
    ('Moletom', 4),
    ('Óculos escuro', 2),
    ('Meia', 10)
}

estoque_minimo = int(input('Qual é a quantidade mínima que cada produto deve ter no estoque? '))

atualizarEstoque(estoque,pedidos,estoque_minimo)