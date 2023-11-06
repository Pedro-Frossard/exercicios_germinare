numero_max =  int(input('Digite um número que eu direi qual é o maior palindromo até ele e a maior multiplicação com o valor de um palindromo: '))

for numero in range(numero_max,-1,-1):
    if str(numero) == str(numero)[::-1]:
        print(f'O maior palindromo encontrado foi {numero}')
        break


for i in range(1,numero_max+1):
    if i*i == numero_max:
        num_max_multiplicado = i
        break
    elif i*i > numero_max:
        num_max_multiplicado = i-1
        break


for j in range(num_max_multiplicado,-1,-1):
    multi = j*j
    if str(multi) == str(multi)[::-1]:
        print(f'O número maximo multiplicado é {j} x {j} = {multi}')
        break