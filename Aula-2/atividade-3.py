#Peça ao usuário para inserir a idade de uma pessoa e classifique-a como "Criança" (0-12 anos), "Adolescente" (13-17 anos), "Adulto" (18-64 anos) ou "Idoso" (65+ anos).

idade = int(input("Idade: "))

if idade >= 0 and idade <= 12:
    print(f"Sua idade é {idade} então você é uma criança")
elif idade >= 13 and idade <= 17:
    print(f"Sua idade é {idade} então você é adolescente")
elif idade >= 18 and idade <= 64:
    print(f"Sua idade é {idade} então você é um adulto")
else:
    print(f"Sua idade é {idade} então você é idoso")