#Solicite o preço de um produto e aplique um desconto de 10% se o preço for maior que R$ 100. Exiba o valor final.

preco = float(input("Digite o preço do produto: R$ "))

if preco > 100:
    desconto = preco * 0.10
    preco_final = preco - desconto
    print(f"O produto tinha preço de R$ {preco:.2f}, recebeu 10% de desconto e saiu por R$ {preco_final:.2f}")
else:
    print(f"O produto custa R$ {preco:.2f} (sem desconto)")


