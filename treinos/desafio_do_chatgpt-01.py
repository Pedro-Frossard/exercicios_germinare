limite = int(input('Digite um número inteiro positivo: '))
contador = contador2 = 1
if limite >= 0:
    while contador < limite:
        contador += 1
        contador2 = contador
        soma = 0
        while contador2 != 1:
            contador2-=1
            numero_divisivel = contador / contador2
            if numero_divisivel.is_integer():
                soma+=contador2
            if contador2 == 1:
                if soma == contador:
                    print(f'{soma} --> ', end = '')
                    break
                else:
                    continue
else:
    print('Digite um limite valido')

print('Fim')





