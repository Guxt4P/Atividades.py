#Atividade 14
# Cálculo da conta de energia elétrica

kwh = float(input("Quantidade de kWh consumidos: "))
valor_kwh = float(input("Valor de 1 kWh (em R$): "))

valor_total = kwh * valor_kwh

print(f"O valor da conta de energia é: R$ {valor_total:.2f}")