def Calcular_ano_bissexto(ano):
    if ano % 4 == 0 and ano % 100 != 0:
        return True
    elif ano % 400 == 0:
        return True
    else:
        return False


def dataValida(data):
    if len(data) == 10:
        if data[2] == '/' and data[5] == '/':
            if 1 <= int(data[3:5]) <= 12:
                if int(data[3:5]) == 2:
                    if Calcular_ano_bissexto(ano=int(data[6:])):
                        if 1 <= int(data[:2]) <= 29: 
                            return True
                        else:
                            return False
                    else:
                        if 1 <= int(data[:2]) <= 28: 
                            return True
                        else:
                            return False
                else:
                    if int(data[3:5]) <= 7:
                        if int(data[3:5]) % 2 == 0:
                            if 1 <= int(data[:2]) <= 30:
                                return True
                            else:
                                return False
                        else:
                            if 1 <= int(data[:2]) <= 31:
                                return True
                            else:
                                return False
                    else:
                        if int(data[3:5]) % 2 == 0:
                            if 1 <= int(data[:2]) <= 31:
                                return True
                            else:
                                return False
                        else:
                            if 1 <= int(data[:2]) <= 30:
                                return True
                            else:
                                return False
            else:
                return False
        else:
            return False
    else:
        return False


ano = int(input('Digite um ano: '))
if Calcular_ano_bissexto(ano):
    print('O ano fornecido é bissexto')
else:
    print('O ano fornecido não é bissexto')

while True:
    data = input('Digite uma data no formato (dia/mes/ano): ')

    if dataValida(data):
        print('Data valida!')
        break
    else:
        print('Data invalida, tente novamente')
        continue