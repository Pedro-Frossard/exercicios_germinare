populacao_inicial = float(input("Digite a população inicial: "))
taxa_crescimento = float(input("Digite a taxa de crescimento anual (em decimal): "))
anos = int(input("Digite o número de anos: "))

populacao_final = populacao_inicial * (1 + taxa_crescimento) ** anos

print(f"A população após {anos} anos será de {populacao_final:.0f}.")

