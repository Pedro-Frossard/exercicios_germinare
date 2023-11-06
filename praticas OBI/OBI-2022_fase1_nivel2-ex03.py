N = int(input())
M =  int(input())
S = int(input())
maior_numero = 0
for numero in range(N,M+1):
    soma = 0
    numero_str = str(numero)
    for i in numero_str:
        soma += int(i)
    if soma == S:
        maior_numero = numero
        
if maior_numero == 0:
    print(-1)
else:
    print(maior_numero)