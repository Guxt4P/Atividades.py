#Solicite a idade do usuário e informe se ele é menor de idade, maior de idade ou idoso (considerando 18 e 65 anos como limites).

idade = int(input("Sua idade: "))

if idade >= 18 and idade <= 64:
    print("Você é maior de idade")
elif idade >= 65:
    print("Você é idoso")
else:
    print("Você é menor de idade")
