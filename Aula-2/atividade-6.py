#Crie um programa que simule um sistema de login. Solicite um nome de usuário e senha e verifique se as credenciais estão corretas.

usuario_correto = "admin"
senha_correta = "1234"

usuario = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")

if usuario == usuario_correto and senha == senha_correta:
    print("✅ Login realizado com sucesso! Bem-vindo,", usuario)
else:
    print("❌ Usuário ou senha incorretos. Tente novamente.")
