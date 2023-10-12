'''
Na semana passada, você criou uma função para validar um e-mail de um usuário (desafio 3 da
semana 3). Agora você precisar criar um gerador de senhas para o mesmo sistema. O seu
programa deverá pedir para o usuário criar uma senha. A senha deve seguir as seguintes regras:
• Deve ter pelo menos 8 caracteres.
• Deve conter pelo menos uma letra maiúscula e uma letra minúscula.
• Deve conter pelo menos um caractere especial (considere apenas esses: ! @ # $ %).
O programa deve validar se a senha atende a esses critérios e informar ao usuário se a senha
é válida ou não. Para isso crie uma função chamada validar_senha onde todas as regras sejam
verificadas e validadas.
'''
senha_usuario = input('Digite sua senha: ')

def validar_senha(senha):

    caractere1 = senha.find('!')
    caractere2 = senha.find('@')
    caractere3 = senha.find('#')
    caractere4 = senha.find('$')
    caractere5 = senha.find('%')

    if caractere1 != -1 or caractere2 != -1 or caractere3 != -1 or caractere4 != -1 or caractere5 != -1:
        caractere_valido = True
    else:
         caractere_valido = False

    tamanho = len(senha)
    if tamanho >= 8:
        tamanho = True
    else:
        tamanho = False

    if senha.isupper():
        letra_valida = False
    elif senha.islower():
        letra_valida = False
    else:
        letra_valida = True

    
    
    

    if tamanho == True and caractere_valido == True and letra_valida == True:
            print('Parabéns, sua senha é valida.')
    else: 
            print('Sua senha não é valida.')
        

validar_senha(senha_usuario)