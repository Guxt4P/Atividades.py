#Crie uma calculadora simples que permita ao usuário escolher uma operação (adição, subtração, multiplicação ou divisão) e dois números, e então exiba o resultado.

num1 = float(input("Digite um numero: "))
num2 = float(input("Digite outro numero: "))
operador = input("Digite o operador: ")

if operador == "+":
    print(f"A soma do numero {num1} + {num2} = {num1 + num2}")
elif operador == "-":
    print(f"A subtração do numero {num1} - {num2} = {num1 - num2}")
elif operador in ("*", "x", "X"):
    print(f"A multiplicação do numero {num1} * {num2} = {num1 * num2}")
elif operador == "/":
    print(f"A divisão do numero {num1} / {num2} = {num1 / num2}")
else:
    print("Operador invalido")