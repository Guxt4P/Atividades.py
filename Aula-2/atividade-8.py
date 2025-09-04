#Peça ao usuário seu peso e altura, calcule o Índice de Massa Corporal (IMC) e classifique-o como "Abaixo do peso", "Peso normal", "Sobrepeso" ou "Obesidade".

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura ** 2)

if imc < 20:
    print(f"Você está abaixo do peso com um IMC de {imc:.2f}")
elif imc < 25:   # de 20 até 24.9
    print(f"Você está com o peso normal com um IMC de {imc:.2f}")
elif imc < 30:   # de 25 até 29.9
    print(f"Você está com sobrepeso com um IMC de {imc:.2f}")
elif imc < 35:   # de 30 até 34.9
    print(f"Você está com obesidade com um IMC de {imc:.2f}")
else:            # 35 ou mais
    print(f"Você está com obesidade grave com um IMC de {imc:.2f}")
