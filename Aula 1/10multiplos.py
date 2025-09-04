#Atividade 10 

#Elaborar um algoritmo que lê 2 valores a e b e os escreve com a mensagem: "São múltiplos" ou "Não são múltiplos".

a = int(input("Digite um valo pro (a): "))
b= int(input("Digite um valor pro (b) "))
 
if a % b == 0 or b % a == 0:
 print("São multiplos")

else:
 print("Não são multiplos")
