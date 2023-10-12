'''
A PICPAY está modificando a exibição de extratos de operações financeiras no seu sistema,
para isso ela precisa que você ajude a pensar em um programa que consiga gerar as seguintes
saídas de dados:
Crie uma função que recebe os dados necessários como parâmetro de entrada e essa função
deve exibir o extrato conforme imagens acima:
EX: na chamada de função, se você digitar:
Algumas regras devem ser seguidas:
1 – O Sistema deve mostrar a data atual no campo Data do extrato.
2 – Se o saldo for maior do que 1500 deve aparecer em AZUL, caso contrário, deve aparecer
de VERMELHO:
2 – A agência deve ser mostrada sempre com 4 dígitos. Se for agencia 1, aparece 0001.
3 – O CPF deve ser apresentado no extrato no formato XXX.XXX.XXX-XX e precisa ser um CPF
válido. Para isso, você pode usar a biblioteca validate_docbr, mas não é obrigatório.
4 – O ID deve ser um número gerado aleatoriamente com 7 casas decimais.
5 – Deverá ter as cores verdes, azul e os títulos em negrito.
6 – O e-mail também precisa ser válido, para isso, use a função que você já fez no desafio 3 da
semana 3.
'''
from datetime import date
from random import randint
from validate_docbr import CPF
from Função_validação_email import validar_email_usuario
def exibirExtrato(nome, cpf, agencia, contaCorrente, destinatario, instituição, email, valor):
    print(f'\033[32mDADOS DO CLIENTE\033[m')
    print(f'\033[1mNome:\033[m {nome}')
    print(f'\033[1mAgência:\033[m {agencia:04d}')
    print(f'\033[1mConta corrente:\033[m {contaCorrente}')
    print('')
    print(f' ','\033[34m-\033[m'*25,' ')
    print(f'\033[32mDADOS DA TRANSFERÊNCIA\033[m')
    print(f'\033[1mPara:\033[m {destinatario}')
    print(f'\033[1mInstituição:\033[m {instituição}')
    
    if validar_email_usuario(email)==True:
        print(f'\033[1mChave:\033[m {email}')
    else:
        print(f'\033[1mChave:\033[m Email invalido')


    cpf_formatado=f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'

    if CPF().validate(cpf_formatado):
        print(f'\033[1mCPF:\033[m {cpf_formatado}')
    else:
        print(f'\033[1mCPF:\033[m CPF INEXISTENTE')

    if valor > 1500:
        print(f'\033[34mValor: R${valor:.2f}\033[m')
    else:
        print(f'\033[31mValor: R${valor:.2f}\033[m')

    print('')
    print(f' ','\033[34m-\033[m'*25,' ')
    print(f'\033[32mID/Transação\033[m')
    print(f'\033[1mID: \033[m{randint(1000000,9999999)}')
    print(f'\033[1mData: \033[m{date.today()}')


exibirExtrato('Viviane','07160128478',1,1234567,'Larissa','Picpay','germinaretech@gmail.com',1000)


