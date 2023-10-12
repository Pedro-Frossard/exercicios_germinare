'''
Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''
contador = soma = media = maior = menor = numero_anterior= 0
while True:
    numero=int(input('Digite um número inteiro: '))
    sair = input('Quer sair? ').upper().strip()
    soma += numero
    contador += 1
    if contador == 1:
        maior= menor = numero_anterior = numero    
    maior = max(numero, numero_anterior, maior)
    menor = min(numero, numero_anterior, menor)
    numero_anterior = numero
    if sair.startswith('S'):
        media = soma/contador
        print(f'Você digitou {contador} números e a média deles é {media:.2f}')
        print(f'O maior número entre eles foi {maior} e o menor foi {menor}')
        break



