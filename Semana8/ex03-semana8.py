assinantes = (10000, 10500, 11000, 11200, 11500, 11800)
cancelamentos = (500, 450, 500, 200, 300, 200)
acessos_canal_rural = (2000, 2200, 2500, 2600, 2700, 2800)

for mes_assinantes, mes_cancelamentos in zip(assinantes, cancelamentos):
    taxa_retenção = (mes_assinantes - mes_cancelamentos)*100/mes_assinantes
    print(f'{taxa_retenção:.2f}%')
print()
for assinantes_mes, canal_rural in zip(assinantes, acessos_canal_rural):
    if assinantes.index(assinantes_mes) == 0:
        taxa_retenção_canal_rural = 0.0
        print(f'{taxa_retenção_canal_rural:.2f}%')
        continue
    else:
        posicao_atual_canal_rural = acessos_canal_rural.index(canal_rural)
        posicao_atual_assinantes = assinantes.index(assinantes_mes)
        taxa_retenção_canal_rural = (acessos_canal_rural[posicao_atual_canal_rural]-acessos_canal_rural[posicao_atual_canal_rural-1])*100/(assinantes[posicao_atual_assinantes] - assinantes[posicao_atual_assinantes-1])
        if taxa_retenção+taxa_retenção_canal_rural >= 150:
            print(assinantes_mes)