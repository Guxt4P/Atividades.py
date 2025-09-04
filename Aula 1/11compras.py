#Atividade 11

#Peça o valor de um produto e aplique um desconto de 10%.

preco = float(input("Digite o valor do produto: R$ "))

desconto = preco * 0.10
preco_final = preco - desconto

print(f"O valor com 10% de desconto é: R$ {preco_final:.2f}")
