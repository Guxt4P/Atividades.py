#Peça um número ao usuário e informe se ele é par ou ímpar.

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print(f"O número {numero} é PAR.")
else:
    print(f"O número {numero} é ÍMPAR.")
