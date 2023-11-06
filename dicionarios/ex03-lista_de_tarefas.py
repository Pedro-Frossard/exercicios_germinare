import datetime

tarefas_atribuidas = dict()
tarefas_pendentes = dict()
tarefas_concluidas = dict()

def adicionarTarefa(tarefa, data):
    data_hoje = datetime.date.today()
    if data_hoje.year > int(data[6:]) or data_hoje.month > int(data[3:5]) or data_hoje.day > int(data[:2]):
        tarefas_pendentes[tarefa] = data
    elif data_hoje.year < int(data[6:]) or data_hoje.month < int(data[3:5]) or data_hoje.day < int(data[:2]):
        tarefas_atribuidas[tarefa] = data
    else:
        tarefas_atribuidas[tarefa] = data



def marcarConcluida(tarefa_concluida):
    if tarefa_concluida in tarefas_atribuidas:
        tarefas_atribuidas.pop(tarefa_concluida)
        tarefas_concluidas[tarefa_concluida] = 'No prazo'
    elif tarefa_concluida in tarefas_pendentes:
        tarefas_pendentes.pop(tarefa_concluida)
        tarefas_concluidas[tarefa_concluida] = 'Concluida com atraso'
    else:
        print('Tarefa não encontrada')



def mudarPrazo():
    while True:
        tarefa_para_mudar = input('Digite a tarefa que você quer mudar: ')
        if tarefa_para_mudar in tarefas_atribuidas:
            data_tarefa = input('Qual é a data da tarefa (DD/MM/AAAA)? ')
            if data_tarefa in tarefas_atribuidas.values():
                
        elif tarefa_para_mudar in tarefas_pendentes:

        else:
            print('Essa tarefa não existe ou ja foi concluida')
            continue



while True:
    print('1 - Adicionar nova tarefa\n2 - Marcar como colcluida\n3 - Mudar prazo\n4 - Excluir tarefa\n5 - Mostrar Tarefas\nOutro - Parar')
    escolha = int(input('Escolha: '))

    if escolha >= 1 and escolha <=5:
        if escolha == 1:
            tarefa = input('Tarefa: ')
            data = input('Data (DD/MM/AAAA): ')
            if len(data)!=10:
                print('Data invalida')
            else:
                adicionarTarefa(tarefa, data)
        elif escolha == 2:
            tarefa_concluida = input('Nome da tarefa concluida: ')
            marcarConcluida(tarefa_concluida)
            print(tarefas_concluidas)
        elif escolha == 3:
            