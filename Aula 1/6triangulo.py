#Atividade 6

#Área = (base × altura) / 2

base = float(input("Qual é o valor da base: "))
altura = float(input("Valos da altura: "))

print("A area do triângulo",(base*altura/2))
print(f"Área = {base} * {altura} / 2 =",(base*altura/2))

#Ou pode ser feito assim:

b = float(input("Qual é o valor da base: "))
h = float(input("Valos da altura: "))
cal = (b*h/2)

print(f"A area do triângulo {cal}")
print(f"Área = {b} * {h} / 2 = {cal}")