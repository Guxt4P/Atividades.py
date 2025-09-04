#Receba a nota de um aluno e classifique-a como A (90-100), B (80-89), C (70-79), D (60-69), ou F (menos de 60).

nota = float(input("Digite sua nota: "))

if 90 <= nota <= 100:
    print("Você tirou A")
elif 80 <= nota <= 89:
    print("Você tirou B")
elif 70 <= nota <= 79:
    print("Você tirou C")
elif 60 <= nota <= 69:
    print("Você tirou D")
elif 0 <= nota < 60:
    print("Você tirou F")
else:
    print("Erro: nota inválida")
