def eh_par_impar(numero):
    if numero%2 == 1:
        print(f'O número {numero} \033[1mé impar\033[m')
    elif numero%2 == 0:
        print(f'O número {numero} \033[1mé par\033[m')

def eh_primo(numero,contador):
    numero_de_divisores=0
    while numero>contador:
            contador+=1
            if numero%contador == 0:
                numero_de_divisores+=1
    if numero_de_divisores == 2:
        print(f'O número {numero} \033[1mé primo\033[m')
    else:
        print(f'O número {numero} \033[1mnão é primo\033[m')

def eh_armstrong(numero, contador, acumulador):
    numero_str = str(numero)
    numero_len = len(numero_str)
    while contador < numero_len:
        acumulador += int(numero_str[contador])**3
        contador+=1
    if acumulador == numero:
        print(f'O número {numero} \033[1mé armstrong\033[m')
    else:
        print(f'O número {numero} \033[1mnão é armstrong\033[m')

def eh_quadradoPerfeito(numero):
    raiz_numero=numero**(1/2)
    
    if raiz_numero.is_integer():
        print(f'O número {numero} \033[1mé um quadrado perfeito\033[m')
    else:
        print(f'O número {numero} \033[1mnão é um quadrado perfeito\033[m')

def eh_palindromo(numero):
    numero_str = str(numero)
    if numero_str[::-1] == numero_str:
        print(f'O número {numero} \033[1mé um palindromo\033[m')
    else:
        print(f'O número {numero} \033[1mnão é um palindromo\033[m')

def tem_fibonacci(numero, contador):
    termo1 = termo2 = 0
    termo3 = 1
    contador = 0
    fibonacci = False

    while termo1 < numero:
        termo1 = termo2
        termo2 = termo3
        termo3 = termo1 + termo2
        contador += 1

        if termo1 == numero:
            fibonacci = True
            break

    if fibonacci == True:
        print(f'O número {numero} \033[1mestá na sequência de Fibonacci\033[m')
    else:
        print(f'O número {numero} \033[1mnão está na sequência de Fibonacci\033[m')
            

contador = acumulador = 0 
numero = int(input('\033[1mDigite um número inteiro positivo: \033[m'))
if numero<0:
    print('\033[31mDigite um número positivo\033[m')
else:
    eh_par_impar(numero)
    eh_primo(numero, contador)
    eh_armstrong(numero, contador, acumulador)
    eh_quadradoPerfeito(numero)
    eh_palindromo(numero)
    tem_fibonacci(numero,contador)
