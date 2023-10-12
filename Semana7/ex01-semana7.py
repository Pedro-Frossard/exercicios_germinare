'''
ENUNCIADO: Faça um programa que ajude as pessoas a saberem o tempo necessário para comprar sua casa
própria fazendo um investimento fixo mensal. 

ENTRADA: O programa deve ler o valor do imóvel, o valor do investimento mensal e a taxa mensal de juros.

CONDIÇOÊS: Caso o valor do investimento mensal seja menor do que 1% do valor do imóvel deve ser mostrada uma mensagem informando não ser viável o investimento. 

SAÍDA: O tempo necessário para compra deve ser calculado em meses utilizando juros compostos
'''

valor_imovel = float(input('Qual é o valor da casa? R$'))
valor_mensal = float(input('Qual será o investimento fixo mensal? R$'))
taxa_de_juros = float(input('Qual é a taxa mensal de juros? '))
total_pago = desconto_mensal = 0

if valor_imovel*0.01 > valor_mensal:
    print('\033[31mInvestimento fixo não viável\033[m')

else:
    for i in range(1,10000):
        if valor_imovel - desconto_mensal <=0:
            total_pago+=valor_imovel
            print(f'Depois de {i} meses e pagar R${total_pago:.2f} no total, você possuirá o imóvel')
            break
        juros_mes = valor_imovel*(taxa_de_juros/100)
        desconto_mensal = valor_mensal - juros_mes
        if desconto_mensal <=0:
            print('Digite uma porcentagem de juros que quando aplicada ao valor do imovel seja menor que o valor fixo mensal')
            break
        valor_imovel-= desconto_mensal
        total_pago+=valor_mensal
       
