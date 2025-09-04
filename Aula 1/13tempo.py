# Atividade 13 - Cálculo do tempo de viagem (em horas e minutos)

distancia = float(input("Qual vai ser a distância percorrida (em km): "))
velocidade = float(input("Qual vai ser a velocidade média (em km/h): "))

tempo_horas = distancia / velocidade

horas = int(tempo_horas)
minutos = int((tempo_horas - horas) * 60)

print(f"O tempo da viagem será de {horas} horas e {minutos} minutos.")
