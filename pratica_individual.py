codigos = [345,765,100,910,344,642]
precos = [11.36, 13.98, 9.86, 19.98, 13.96, 16.98]
estoques = [2, 4, 1, 25, 0, 12]

def menu():
    print("\x1b[2J")  #print acima é para limpar a tela do terminal
    print(f'\033[1;33mCódigo --|--            Produto            --|-- Preço(R$) --|-- Estoque\033[0;0m')
    print(f'\n{codigos[0]:^7}--|--{"Presunto Fatiado 180g":^31}--|--{precos[0]:^11}--|--{estoques[0]:^6}',
    f'\n{codigos[1]:^7}--|--{"Coxinha da Asa Empanadas 400g":^31}--|--{precos[1]:^11}--|--{estoques[1]:^6}',
    f'\n{codigos[2]:^7}--|--{"Chicken Supreme 300g":^31}--|--{precos[2]:^11}--|--{estoques[2]:^6}',
    f'\n{codigos[3]:^7}--|--{"Hambúrguer Polpetone 320g ":^31}--|--{precos[3]:^11}--|--{estoques[3]:^6}',
    f'\n{codigos[4]:^7}--|--{"Filé de Tilápia 250g":^31}--|--{precos[4]:^11}--|--{estoques[4]:^6}',
    f'\n{codigos[5]:^7}--|--{"Filé de Peito Empanado 400g":^31}--|--{precos[5]:^11}--|--{estoques[5]:^6}'
    f'\n\033[1;31m{999:^7}---->{"FINALIZAR O PROGRAMA":^31}\033[0;0m'
    )

menu()
valor_compra = 0
quantidade_items_comprados = 0
while True:
    codigo = int(input('Digite o código do produto que você quer comprar: '))
    if codigo != 999:
        if codigo in codigos:
            localizacao_codigo = codigos.index(codigo)
            produto_localizado = [codigos[localizacao_codigo], precos[localizacao_codigo], estoques[localizacao_codigo]]
            if produto_localizado[-1] > 0:
                while True:
                    quantidade_produtos = int(input('Quantos produtos você deseja comprar? '))
                    if produto_localizado[-1] - quantidade_produtos < 0:
                        print('Quantidade indisponivel')
                        continue
                    else:
                        estoques[localizacao_codigo] -= quantidade_produtos
                        valor_compra+=precos[localizacao_codigo]*quantidade_produtos
                        quantidade_items_comprados+=quantidade_produtos
                        print('Compra realizada')
                        break
            else:
                print('O produto escolhido não tem estoque')
        else:
            print('Código inexistente')
            continue
    elif codigo == 999:
        print('Compra finalizada')
        print(f'O valor total ficou em R${valor_compra:.2f} e {quantidade_items_comprados} produtos comprados')
        break
