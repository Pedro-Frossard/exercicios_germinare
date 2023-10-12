horario = input("Digite o horário no formato HH:MM:SS: ")

horas = int(horario[:2])
minutos = int(horario[3:5])
segundos = int(horario[6:8])

total_segundos = horas * 3600 + minutos * 60 + segundos

print(f"O horário {horario} equivale a {total_segundos} segundos.")
