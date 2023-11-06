from random import randint

biblioteca = dict()
def cadastrarLivro(biblioteca):
    while True:
        titulo = input('Qual é o titulo do livro? ')
        autor =  input('Qual é o autor do livro? ')
        biblioteca[f'livro {len(biblioteca)+1}'] = {
                                                'titulo': titulo,
                                                'autor': autor                                            
                                                }
        while True:
            codigo = randint(1000,9999)
            adicionar_codigo = 0
            for i in biblioteca:
                if len(biblioteca) > 1:
                    if i != f'livro {len(biblioteca)}':
                        if biblioteca[i]['codigo'] == codigo:
                            adicionar_codigo+=1
                        else:
                            continue
            if adicionar_codigo == 0:
                biblioteca[f'livro {len(biblioteca)}']['codigo'] = codigo
                print(f'\nTitulo: {biblioteca[f"livro {len(biblioteca)}"]["titulo"]}\nAutor: {biblioteca[f"livro {len(biblioteca)}"]["autor"]}\nCódigo: {biblioteca[f"livro {len(biblioteca)}"]["codigo"]}')
                break
            else:
                continue
        if 'codigo' in biblioteca[f'livro {len(biblioteca)}']:
            break
def removerLivro(biblioteca):
    while True:
        remover_livro = int(input('Qual é o código do livro que voce deseja remover? '))
        livro_nao_encontrado=0
        for livro in biblioteca:
            if biblioteca[livro]['codigo'] == remover_livro:
                remover = input(f'Você realmente deseja remover este livro? ').upper()
                if remover.startswith('S'):
                    del(biblioteca[livro])
                    print('Livro removido')
                    break
                else:
                    break
            else:
                livro_nao_encontrado+=1
                continue
        if livro_nao_encontrado == len(biblioteca):
            print('Livro não encontrado')
            continue
        elif livro_nao_encontrado == len(biblioteca)-1:
            break 

def buscarLivro(biblioteca):
    while True:
        pesquisa_codigo = int(input('Qual é o código do livro que você deseja buscar? '))
        livro_desconhecido = 0
        for livro in biblioteca:
            if biblioteca[livro]['codigo'] == pesquisa_codigo:
                print(f'\nTitulo: {biblioteca[livro]["titulo"]}\nAutor: {biblioteca[livro]["autor"]}')
            else:
                livro_desconhecido+=1
        if livro_desconhecido == len(biblioteca):
            print('Livro não encontrado, tente novamente')
            continue
        elif livro_desconhecido == len(biblioteca)-1:
            break


                  


while True:
    print('[1] Cadastrar novo livro\n[2] Remover livro\n[3] Buscar livro por código\n[4] Ver quantidade de registros\n[5] Ver livros\n[Outro] Sair')
    escolha = int(input('Escolha: '))
    if escolha == 1:
        cadastrarLivro(biblioteca)
    elif escolha == 2:
        removerLivro(biblioteca)
    elif escolha == 3:
        buscarLivro(biblioteca)
    elif escolha == 4:
        print(f'Registros na biblioteca: {len(biblioteca)}')
    elif escolha == 5:
        print('Opção 1 – Mostrar os livros por ordem de cadastro.\nOpção 2 – Mostrar os livros em ordem alfabética pelo título.\nOpção 3 – Mostrar os livros em ordem alfabética pelo autor.\nOpção 4 – Mostrar os livros em ordem crescente do código.\nOutro número - Voltar ao menu principal')
        opcao = int(input('Opção: '))
        if opcao == 1:
            for numero, livro in enumerate(biblioteca):
                print(f'\nLivro: {numero+1}\nTitulo: {biblioteca[livro]["titulo"]}\nAutor: {biblioteca[livro]["autor"]}')
        elif opcao == 2:
            biblioteca_ordenada = dict(sorted(biblioteca.items(), key=lambda item: item[1]['titulo']))
            for livro_ordenado in biblioteca_ordenada:
                print(f'\n{livro_ordenado}\nTitulo: {biblioteca_ordenada[livro_ordenado]["titulo"]}\nAutor: {biblioteca_ordenada[livro_ordenado]["autor"]}\nCódigo: {biblioteca[livro_ordenado]["codigo"]}')
        elif opcao == 3:
            biblioteca_ordenada_autores = sorted(biblioteca.items(), key=lambda x:x[1]['autor'])
            for livro_ordenado_autores in biblioteca_ordenada_autores:
                print(f'\n{livro_ordenado_autores[0]}\nTitulo: {livro_ordenado_autores[1]["titulo"]}\nAutor: {livro_ordenado_autores[1]["autor"]}\nCódigo: {livro_ordenado_autores[1]["codigo"]}')
        elif opcao == 4:
            biblioteca_ordenada_codigo = sorted(biblioteca.items(), key= lambda x:x[1]['codigo'])
            for livro_ordenado_codigo in biblioteca_ordenada_codigo:
                print(f'\n{livro_ordenado_codigo[0]}\nTitulo: {livro_ordenado_codigo[1]["titulo"]}\nAutor: {livro_ordenado_codigo[1]["autor"]}\nCódigo: {livro_ordenado_codigo[1]["codigo"]}')
        else:
            print('\nVoltando ao menu principal...\n')
            continue
            
    if escolha > 5 or escolha < 1:
        break


