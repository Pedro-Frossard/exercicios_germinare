print('SUPER LOJA')
print('')
contador = menor_preco = maior_preco = acumulador = 0
while True:
    nome_produto = input('Qual foi o produto que você comprou? ')
    preco = float(input('Qual foi o preço dele? R$'))
    continuar = input('Deseja continuar? [S/N] ').upper()
    contador +=1
    acumulador+=preco
    if contador == 1:
        menor_preco = maior_preco = preco
        nome_produto_menor = nome_produto
        nome_produto_maior = nome_produto
    elif contador > 1:
        if preco < menor_preco:
            nome_produto_menor = nome_produto
        elif preco > maior_preco:
            nome_produto_maior = nome_produto
        menor_preco = min(preco, menor_preco)
        maior_preco = max(preco , maior_preco)
        

    if continuar.startswith('N'):
        print('FIM DO PROGRAMA')
        print('')
        print(f'O total de compra foi de R${acumulador:.2f}\nO produto de maior preço foi {nome_produto_maior} e custou R${maior_preco:.2f}\nO produto de menor preço foi {nome_produto_menor} e custou R${menor_preco:.2f}')
        break