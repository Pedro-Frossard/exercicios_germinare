print("""
        Item             Valor
[1] Pão de Queijo       R$3,50
[2] Coxinha             R$5,00
[3] Esfiha de Carne     R$5,50
[4] Empada de Frango    R$5,50
[5] Refrigerante        R$6,00
[6] Suco de Laranja     R$8,00
[7] Café expresso       R$3,00
[8] Chocolate Quente    R$4,50
[9] Água mineral        R$2,50
[0] Parar
""")

precos = [3.5, 5, 5.5, 5.5, 6, 8, 3, 4.5, 2.5]
produtos = ['Pão de Queijo', 'Coxinha', 'Esfiha de Carne', 'Empada de Frango', 'Refrigerante', 'Suco de Laranja', 'Café expresso', 'Chocolate Quente', 'Água mineral']
pedidos = []
acumulador = 0
while True:
    pedido = int(input('O que voce vai querer? '))
    if 1 <= pedido <= 9:
        while True:
            quantidade = int(input('Quantos você vai querer? '))
            if quantidade < 0:
                print('Quantidade invalida')
                continue
            else:
                pedidos.append((pedido, quantidade, precos[pedido-1]*quantidade))
                acumulador+=precos[pedido-1]*quantidade
                break
    elif pedido == 0:
        for compra in pedidos:
            print(f'{compra[1]} - {produtos[compra[0]-1]}(s) - R${compra[2]:.2f}')
        print(f'TOTAL: R${acumulador:.2f}')
        break
    else:
        print('Produto invalido, por favor digite um numero de 1-9 ou 0 para sair')
        break