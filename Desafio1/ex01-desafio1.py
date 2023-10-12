tempo = int(input("Digite o tempo em segundos: "))

horas = tempo // 3600
tempo = tempo % 3600
minutos = tempo // 60
segundos = tempo % 60
print(f"O tempo convertido é: {horas}h {minutos}min {segundos}s")
