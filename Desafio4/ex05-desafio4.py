divida = float(input('Qual é o valor da divida? R$'))
pagamento_mensal = float(input('Quanto você pagará por mês até a divida ser paga? R$'))
contador = 0
mes_pago=divida
while mes_pago > 0:
    mes_pago-=pagamento_mensal
    contador+=1
    
    if mes_pago < 0:
        ultima_divida = pagamento_mensal+mes_pago
        print(f'{contador}º)Mês. Total pago R${(pagamento_mensal*(contador-1))+(ultima_divida):.2f} Divida --> R${ultima_divida-ultima_divida:.2f}')
        print('\033[1;32mDIVIDA PAGA!\033[m')
    else:
        print(f'{contador}º)Mês. Total pago R${pagamento_mensal*contador:.2f} Divida --> R${mes_pago:.2f}')