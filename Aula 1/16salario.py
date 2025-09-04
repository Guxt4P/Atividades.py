#Atividade 16

#Crie um programa que leia o número de dias trabalhados em um mês e mostre o salário de um funcionário, sabendo que ele trabalha 8 horas por dia e ganha R$25,00 por hora trabalhada.

day = int(input("Dias trabalhados: "))

horas = 8   
ganha = 25
salario = day * horas * ganha

print(f"O seu salário é de R$ {salario},00")

