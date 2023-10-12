from time import sleep

minutos = int(input('Qual o minuto inicial? '))
if minutos  >= 0:
    if minutos > 0:
        for i in range(minutos-1,-1,-1):
            for j in range(60,-1,-1):
                if j <= 10 and i == 0:
                    print(f'\033[31m{i:02}:{j:02}\033[m')
                    sleep(1)
                    if j == 0:
                        print('Fim!')
                else:
                    if j == 60:
                        j = 0
                        print(f'{i+1:02}:{j:02}')
                        sleep(1)
                    else:
                        print(f'{i:02}:{j:02}')
                        sleep(1)
                
    elif minutos == 0:
        segundos = int(input('Quantos segundos então? '))
        if segundos > 0:
            for k in range(segundos,-1,-1):
                    if k <= 10:
                        print(f'\033[31m00:{k:02}\033[m')
                        sleep(1)
                    else:
                        print(f'00:{k:02}')
                        sleep(1)
                    if k == 0:
                        print('Fim!')
        else:
            print('Segundos inválidos')        

else:
    print('Digite minutos válidos')