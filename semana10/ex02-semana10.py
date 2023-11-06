total_gasto = 0 
saldo_insuficiente = False
def compra(conta, preco):
    global total_gasto
    global saldo_insuficiente
    if conta["saldo"] - preco >=0:
        conta["transações"]+=1
        conta["saldo"]-= preco
        total_gasto += preco
        conta["media"] = total_gasto/conta["transações"]
        return conta
    else:
        saldo_insuficiente = True
        print('Saldo insuficiente')



conta = {'transações':0, 
        'saldo': 1000,
        'media': 0
}

compra(conta, 100)
compra(conta, 200)

