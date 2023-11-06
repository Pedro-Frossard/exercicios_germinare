def inverterEstoque(estoque):
    estoque_invertido = dict()
    for codigo, produto in estoque.items():
        if produto in estoque_invertido.keys():
            if type(estoque_invertido[produto]) == list:
                estoque_invertido[produto].append(codigo)
            else:
                estoque_invertido[produto] = [estoque_invertido[produto],codigo]

        else:
            estoque_invertido[produto] = codigo
        
    return estoque_invertido


estoque = {
    405 : 'chinelo',
    159 : 'boné',
    981 : 'camiseta',
    309 : 'celular',
    582 : 'bala',
    603 : 'camiseta',
    875 : 'camiseta',
    333 : 'boné'
}

print(inverterEstoque(estoque))