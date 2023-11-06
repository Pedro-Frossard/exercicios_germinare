def localizarCliente(clientes, variavel):
    num_variaveis_encontradas = 0
    variaveis_encontradas = []
    for chaves, valores in clientes.items():
        for chave, valor in valores.items():
            if variavel in valor:
                num_variaveis_encontradas+=1
                variaveis_encontradas.append([chaves, chave])
            else:
                continue
    if num_variaveis_encontradas == 0:
        print('Valor não encontrado')
    else:
        print('Valor encontrado:')
        for valores_encontrados in variaveis_encontradas:
            print(f'{valores_encontrados[0]}: {valores_encontrados[1]}\n')



clientes = {
    'Cliente 1': {
        'Nome': 'Alice',
        'Endereço': 'Rua Figueiredo Neto, 153',
        'Nome da Mãe': 'Maria Sophia',
    },
    'Cliente 2': {
        'Nome': 'Marcelo Figueiredo',
        'Endereço': 'Rua Boa Vizinhança, 781',
        'Nome da Mãe': 'Ana Clara Figueiredo',
    },
    'Cliente 3': {
        'Nome': 'Carlos Barbosa',
        'Endereço': 'Av. Guilherme, 593',
        'Nome da Mãe': 'Sofia Barbosa',
    },
    'Cliente 4': {
        'Nome': 'Fernando Campos',
        'Endereço': 'Rua Martins Figueiredo, 1481',
        'Nome da Mãe': 'Deise Campos',
    },
    'Cliente 5': {
        'Nome': 'Eva Dias',
        'Endereço': 'Rua Borges dos Santos, 71',
        'Nome da Mãe': 'Carolina Dias',
    }
}

localizarCliente(clientes,'Rua')