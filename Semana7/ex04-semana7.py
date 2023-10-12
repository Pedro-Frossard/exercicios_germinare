print('---------- PROMOÇÃO SWIFT ----------')
print()
quantidade_produtos = int(input('Quantos produtos você comprou na loja? '))
preco_total = 0
if quantidade_produtos > 0:
    for i in range(1,quantidade_produtos+1):
        preco_produto = float(input(f'Quanto custou o {i}º produto? R$'))
        if preco_produto <= 0:
            print('O produto preço do produto não pode ser 0 ou menor')
            break
        else:
            preco_total+=preco_produto
           
    
    if preco_total > 100:
        if quantidade_produtos == 4:
            print()
            print(f'\033[1mNúmero de produtos:\033[m {quantidade_produtos}\n\033[1mValor sem desconto:\033[m R${preco_total:.2f}\n\033[1mValor com desconto de 4%:\033[m R${preco_total - preco_total*0.04:.2f}')
            
        elif quantidade_produtos == 5:
            print()
            print(f'\033[1mNúmero de produtos:\033[m {quantidade_produtos}\n\033[1mValor sem desconto:\033[m R${preco_total:.2f}\n\033[1mValor com desconto de 8%:\033[m R${preco_total - preco_total*0.08:.2f}')
            
        elif quantidade_produtos >= 6:
            print()
            print(f'\033[1mNúmero de produtos:\033[m {quantidade_produtos}\n\033[1mValor sem desconto:\033[m R${preco_total:.2f}\n\033[1mValor com desconto de 12%:\033[m R${preco_total - preco_total*0.12:.2f}')
                
        else:
            print()
            print(f'Você comprou apenas {quantidade_produtos} produtos, a promoção coemça a partir do 4º produto')
            

    else:
        print()
        print('Para a promoção ser aplicada você deve comprar mais de R$100.00 em produtos')

elif quantidade_produtos <= 0:
    print('Voce não comprou nenhum produto')