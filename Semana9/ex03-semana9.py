def selecionarClientes(clientes, idade_min, idade_max, cidade, valor_min):
    clientes_selecionados = set()
    for cliente in clientes:
        if cliente[1] >= idade_min and cliente[1] <= idade_max and cliente[2].title() == cidade and cliente[-1] >= valor_min:
            clientes_selecionados.add(cliente[0])
    print('Os clientes selecionados foram:')
    for cliente_selecionado in clientes_selecionados:
        print(cliente_selecionado)

clientes = [
        ('Ana clara', 27, 'Rio de Janeiro', 800),
        ('Pedro', 22, 'São Paulo', 1000),
        ('Carlos', 45, 'São Paulo', 400),
        ('Marcelo', 36, 'São Paulo', 800),
        ('Maria', 28,'São Bernardo', 550)
]

selecionarClientes(clientes, idade_min=18,idade_max=40,cidade='São Paulo',valor_min=600)