#Atividade 18   

#O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que a percentagem do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo que leia o custo de fábrica de um carro e escreva o custo ao consumidor.

custo_fabrica = float(input("Digite o custo de fábrica do carro: R$ "))
percentual_distribuidor = 0.28  
imposto = 0.45

custo_distribuidor = custo_fabrica * percentual_distribuidor
custo_imposto = custo_fabrica * imposto 
custo_consumidor = custo_fabrica + custo_distribuidor + custo_imposto   

print(f"\nCusto de fábrica: R$ {custo_fabrica:.2f}")
print(f"Percentual do distribuidor (28%): R$ {custo_distribuidor:.2f}")
print(f"Impostos (45%): R$ {custo_imposto:.2f}")
print(f"=> Custo ao consumidor: R$ {custo_consumidor:.2f}")