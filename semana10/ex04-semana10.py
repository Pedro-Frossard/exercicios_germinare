def incluirNovoTel(telefones, nome):
    agenda[nome] = telefones


def incluirTelefone(outro_telefone, nome_agenda):
    for chave, valor in agenda.items():
        if chave == nome_agenda:
            valor.append(outro_telefone)
    


def excluirTelefone():
    while True:
        telefone_para_excluir = input('Qual é o número de telefone que você deseja exc0luir? ')
        telefone_encontrado = False
        if len(telefone) == 13 or len(telefone) == 12:
            for chave, valor in agenda.items():
                if telefone_para_excluir in valor:
                    valor.remove(telefone_para_excluir)
                    telefone_encontrado = True
                    if valor == []:
                        agenda.pop(chave)
                    break
            if telefone_encontrado == False:
                print('Telefone não encontrado, tente novamente.')
                continue
            else:
                break
        else:
            print('Telefone invalido')
            continue



def excluirNome():
    while True:
        if agenda == {}:
            print('Você não tem contatos para excluir')
            break
        else:
            nome_para_excluir = input('Quem você deseja excluir de sua agenda? ')
            if nome_para_excluir in agenda.keys():
                agenda.pop(nome_para_excluir)
                break
            else:
                print('Nome não encontrado')
                continue



def mostrarAgenda(agenda):
    for chave, valor in agenda.items():
        print(f'{chave}: ', end='')
        for tel in valor:
            print(tel,end='  ')
        print()
    


agenda = dict()

while True:
    telefones = []
    print('1 - Adicionar novo nome e telefone\n2 - Incluir telefone em um nome já existente\n3 - Excluir telefone de uma pessoa\n4 - Excluir pessoa e telefone\n5 - Mostrar Agenda\nOutro - Parar')
    escolha = int(input('Escolha: '))
    if escolha > 5 or escolha < 1:
        print('Encerrando')
        break
    else:
        if escolha == 1:
            nome = input('Nome: ')
            num_telefones = int(input('Quantos telefones essa pessoa tem? '))
            contador = 0
            while contador < num_telefones:
                contador+=1
                telefone = input('\nExemplo telefone: 5511958278542\nTelefone: ')
                if len(telefone) == 13 or len(telefone) == 12:
                    telefones.append(telefone)
                else:
                    print('Telefone invalido')
                    contador-=1
                    continue
            incluirNovoTel(telefones,nome)

        elif escolha == 2:
            nome_agenda = input('Nome: ')
            while True:
                outro_telefone = input('\nExemplo telefone: 5511958278542\nTelefone: ')
                if len(str(outro_telefone)) == 13 or len(str(outro_telefone)) == 12:
                    break
                else:
                    print('Telefone invalido')
                    continue
                
            if nome_agenda not in agenda.keys():
                incluirNovoTel(telefones=[outro_telefone], nome=nome_agenda)
            else:
                incluirTelefone(outro_telefone, nome_agenda)
        elif escolha == 3:
            excluirTelefone()
        elif escolha == 4:
            excluirNome()
        elif escolha == 5:
            mostrarAgenda(agenda)