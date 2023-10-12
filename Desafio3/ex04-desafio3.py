'''
O Mercado J&F está com uma promoção de carnes da Friboi, que é imperdível. Confira a tabela
de divulgação de preços abaixo:
Para atender a todos os clientes, o mercado já estabeleceu as regras, mas você precisa criar
um sistema para aplicar as seguintes condições:
• Cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há
limites para a quantidade de carne por cliente.
• Se compra for feita no cartão de débito, o cliente receberá ainda um desconto de 5%
sobre o total da compra.
Escreva um programa que primeiro mostre um menu com as opções disponíveis, depois peça o
tipo e a quantidade de carne comprada pelo usuário. Seu programa deve gerar um relatório
contendo as informações da compra com as informações do tipo de carne comprada, a
quantidade de carne (em Kg), preço total, o meio/tipo de pagamento e valor total a pagar.
Observe um possível fluxo de código!
'''

print('Mercado J&F - Promoção FRIBOI\n1- File Duplo\n2- Alcatra\n3- Picanha\n')
tipo=int(input('Digite o tipo que deseja levar (número): '))

quantidade=float(input('Digite a quantidade comprada (em Kg): '))
print('A compra será realizada com cartão de débito?\n1 - SIM\n2 - NÃO')
debito= int(input('Sua escolha: '))
print('')

print(15 * '*' + 'CUPOM FISCAL' + 15 * '*')
if tipo <= 3 and tipo > 0:
    if tipo == 1:
        print('* Carne: File Duplo')
        print(f'* Quantidade: {quantidade}Kg')
        if quantidade >=5:
            preco=quantidade*5.8
            print(f'* Preço: R${preco:.2f}')
        elif quantidade < 5:
            preco= quantidade*4.90
            print(f'* Preço: R${preco:.2f}')
        if debito==1:
            print('* Cartão de débito: SIM')
            print(f'* Total: R${preco*95/100:.2f}')
        elif debito == 2:
            print('* Cartão de débito: NÃO')
            print(f'* Total: R${preco:.2f}')

    elif tipo == 2:
        print('* Carne: Alcatra')
        print(f'* Quantidade: {quantidade}Kg')
        if quantidade >=5:
            preco=quantidade*6.8
            print(f'* Preço: R${preco:.2f}')
        elif quantidade < 5:
            preco= quantidade*4.90
            print(f'* Preço: R${preco:.2f}')
        if debito==1:
            print('* Cartão de débito: SIM')
            print(f'* Total: R${preco*95/100:.2f}')
        elif debito == 2:
            print('* Cartão de débito: NÃO')
            print(f'* Total: R${preco:.2f}')

    elif tipo == 3:
        print('* Carne: Picanha')
        print(f'* Quantidade: {quantidade}Kg')
        if quantidade >=5:
            preco=quantidade*7.8
            print(f'* Preço: R${preco:.2f}')
        elif quantidade < 5:
            preco= quantidade*4.90
            print(f'* Preço: R${preco:.2f}')
        if debito==1:
            print('* Cartão de débito: SIM')
            print(f'* Total: R${preco*95/100:.2f}')
        elif debito == 2:
            print('* Cartão de débito: NÃO')
            print(f'* Total: R${preco:.2f}')

else: 
    print('Tipo invalido!')