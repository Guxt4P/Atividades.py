#Atividade 8 

#Faça um algoritmo que leia a largura e altura de uma parede, calcule e mostre a área a ser pintada e a quantidade de tinta necessária para o serviço, sabendo que cada litro de tinta pinta uma área de 2metros quadrados.

width = float(input("Qual é a largura da sua parede: "))
height = float(input("Qual é a altura: "))

area = (width*height)
litros = area /2

print(f"A área da sua parede é de: {area:.2f} m²")
print(f"Será necessário {litros:.2f} litros de tinta para pintá-la.")

