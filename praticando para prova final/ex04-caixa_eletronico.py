dinheiro = float(input('Quanto você deseja sacar? R$'))


saque = dinheiro
notas_100 = saque // 100
saque %= 100
notas_50 = saque // 50
saque %= 50
notas_10 = saque // 10
saque %= 10
notas_5 = saque // 5
saque %= 5
notas_2 = saque

print(f"Notas de 100: {notas_100}")
print(f"Notas de 50: {notas_50}")
print(f"Notas de 10: {notas_10}")
print(f"Notas de 5: {notas_5}")
print(f"Notas de 2: {notas_2}")