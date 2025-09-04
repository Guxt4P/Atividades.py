#Atividade 12

#Peça o salário de um funcionário e aumente em 15%.

salario = float(input("Seu salário: R$ "))

aumento = salario * 0.15
novo_salario = salario + aumento

print(f"O seu aumento foi de R$ {aumento:.2f}")
print(f"O seu novo salário é de R$ {novo_salario:.2f}")
