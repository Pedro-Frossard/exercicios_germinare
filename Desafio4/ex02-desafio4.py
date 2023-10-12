from random import randint

contador=0

print(29*'\033[1;31m-\033[m')
print('\033[1;34m    Jogo da adivinhação\033[m ')
print(29*'\033[1;31m-\033[m')
print('')

print('Qual é o nivel que você deseja jogar?\nF --> Fácil\nM --> Médio\nD --> Difícil')

nivel = input('Sua escolha: ').upper()

if nivel == 'F' or nivel == 'M' or nivel == 'D':
    if nivel == 'F':
        numero_escolhido=randint(1,10)
        print('')
        print('\033[1;32mNÍVEL FÁCIL / 1 --> 10\033[m')
    elif nivel == 'M':
        numero_escolhido = randint(1,50)
        print('')
        print('\033[1;33mNÍVEL MÉDIO / 1 --> 50\033[m')
    elif nivel == 'D':
        numero_escolhido = randint(1,100)
        print('')
        print('\033[1;31mNÍVEL DIFÍCIL / 1 --> 100\033[m')
    while True:
        numero_digitado= int(input('Tentativa: '))
        if numero_escolhido < numero_digitado:
            print('O número que eu pensei é menor!')
            contador+=1
            continue
        elif numero_escolhido > numero_digitado:
            print('O número que eu pensei é maior!')
            contador+=1
            continue
        elif numero_digitado == numero_escolhido:
            contador+=1
            print(f'Parabéns! O número que eu estava pensando era {numero_escolhido}, você conseguiu adivinha-lo em  {contador} tentativas')
            break
else:
    print('\033[31mNível invalido!\033[m')