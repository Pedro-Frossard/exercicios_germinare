LITROS_POR_LATA = 5
METROS_POR_LITRO = 3


largura = float(input("Digite a largura do quintal (metros): "))
comprimento = float(input("Digite o comprimento do quintal (metros): "))


area_quintal = largura * comprimento


litros_necessarios = area_quintal / METROS_POR_LITRO


latas_necessarias = litros_necessarios // LITROS_POR_LATA



custo_por_lata = float(input("Digite o custo de cada lata de tinta (R$): "))
custo_total = latas_necessarias * custo_por_lata


print(f"Para pintar um quintal de {largura}m x {comprimento}m:")
print(f"Você precisará de {latas_necessarias} latas de tinta.")
print(f"O custo total será de R${custo_total:.2f}.")
