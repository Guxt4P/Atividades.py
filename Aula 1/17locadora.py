#Atividade 17

#A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar, sabendo que o carro custa 90,00 pordiae R 0,20 por Km rodado.
carro = str(input("Digite o nome do carro alugado: "))
km = float(input("Quantidade de km percorrido: "))
dias = int(input("Quantidade de dias alugados: "))  

preco_dia = 90.00
preco_km = 0.20 

total = (dias * preco_dia) + (km * preco_km)   

print(f"O total a pagar pelo aluguel do carro {carro} é: R$ {total:.2f}")
print("Obrigado por alugar conosco!")