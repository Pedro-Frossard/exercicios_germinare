# Criar uma função para autenticar o e-mail
def validar_email_usuario(email):
    email.lower()

    validacao= email.find('@') != -1 and email.find('.com') != -1
    return validacao

