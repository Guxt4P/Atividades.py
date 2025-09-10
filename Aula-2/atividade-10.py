#Desenvolva um programa que permita ao usuário escolher uma operação (saque, depósito) e simule o comportamento de um caixa eletrônico com validações básicas (ex.: saldo insuficiente para saque).

saldo = 500.0  # saldo inicial

while True:
    print("\n=== Caixa Eletrônico ===")
    print("1 - Saque")
    print("2 - Depósito")
    print("3 - Consultar saldo")
    print("4 - Sair")

    opcao = input("Escolha a operação (1/2/3/4): ")

    if opcao == "1":
        valor = float(input("Digite o valor do saque: R$ "))
        if valor <= saldo:
            saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("❌ Saldo insuficiente!")
    elif opcao == "2":
        valor = float(input("Digite o valor do depósito: R$ "))
        saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    elif opcao == "3":
        print(f"📌 Seu saldo atual é: R$ {saldo:.2f}")
    elif opcao == "4":
        print("Encerrando... 👋")
        break
    else:
        print("⚠️ Opção inválida! Tente novamente.")

