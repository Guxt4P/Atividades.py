#Atividade 9

peso = float(input("Adiciona o seu peso: "))
altura = float(input("Adiciona a sua altura: "))

IMC = peso / (altura ** 2)

print(f"O seu IMC é: {IMC:.2f} kg/m²")