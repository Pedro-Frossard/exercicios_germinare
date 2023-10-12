
SALARIO_POR_HORA = 25
VALOR_POR_DEPENDENTE = 500
SEMANAS_POR_MES = 4


nome_funcionario = input("Qual o nome do funcionário? ")
horas_por_semana = float(input(f"Quantas horas por semana {nome_funcionario} trabalha? "))
numero_dependentes = int(input("Digite o número de dependentes: "))


salario_base = horas_por_semana * SALARIO_POR_HORA * SEMANAS_POR_MES
bonus_dependentes = numero_dependentes * VALOR_POR_DEPENDENTE
salario_mensal = salario_base + bonus_dependentes


print(f"{nome_funcionario} terá um salario mensal de R${salario_mensal:.2f}")
