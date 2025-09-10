import tkinter as tk
from tkinter import messagebox

# =========================
# Dados do cliente
# =========================
saldo = 500.0
limite_saque = 1000.0
limite_diario = 3
saques_realizados = 0

# =========================
# Funções
# =========================
def consultar_saldo():
    messagebox.showinfo("Saldo", f"📌 Seu saldo atual é: R$ {saldo:.2f}\n"
                                 f"📊 Saques restantes hoje: {limite_diario - saques_realizados}")

def sacar():
    global saldo, saques_realizados
    if saques_realizados >= limite_diario:
        messagebox.showerror("Erro", "❌ Você atingiu o limite diário de saques!")
        return

    try:
        valor = float(entry_valor.get())
        if valor <= 0:
            messagebox.showerror("Erro", "❌ Digite um valor positivo!")
        elif valor > limite_saque:
            messagebox.showerror("Erro", f"❌ O limite por saque é R$ {limite_saque:.2f}")
        elif valor > saldo:
            messagebox.showerror("Erro", "❌ Saldo insuficiente!")
        else:
            saldo -= valor
            saques_realizados += 1
            messagebox.showinfo("Saque", f"✅ Saque de R$ {valor:.2f} realizado!\n"
                                         f"Novo saldo: R$ {saldo:.2f}")
    except ValueError:
        messagebox.showerror("Erro", "⚠️ Digite um valor numérico válido.")

def depositar():
    global saldo
    try:
        valor = float(entry_valor.get())
        if valor <= 0:
            messagebox.showerror("Erro", "❌ Digite um valor positivo!")
        else:
            saldo += valor
            messagebox.showinfo("Depósito", f"✅ Depósito de R$ {valor:.2f} realizado!\n"
                                            f"Novo saldo: R$ {saldo:.2f}")
    except ValueError:
        messagebox.showerror("Erro", "⚠️ Digite um valor numérico válido.")

def sair():
    janela.quit()

# =========================
# Interface Tkinter
# =========================
janela = tk.Tk()
janela.title("Caixa Eletrônico")
janela.geometry("300x300")
janela.resizable(False, False)

# Título
label_titulo = tk.Label(janela, text="🏦 Caixa Eletrônico", font=("Arial", 14, "bold"))
label_titulo.pack(pady=10)

# Entrada de valor
label_valor = tk.Label(janela, text="Digite o valor:", font=("Arial", 11))
label_valor.pack()
entry_valor = tk.Entry(janela, font=("Arial", 11))
entry_valor.pack(pady=5)

# Botões
btn_saque = tk.Button(janela, text="Saque", width=15, command=sacar)
btn_saque.pack(pady=5)

btn_deposito = tk.Button(janela, text="Depósito", width=15, command=depositar)
btn_deposito.pack(pady=5)

btn_saldo = tk.Button(janela, text="Consultar Saldo", width=15, command=consultar_saldo)
btn_saldo.pack(pady=5)

btn_sair = tk.Button(janela, text="Sair", width=15, command=sair)
btn_sair.pack(pady=10)

# Iniciar janela
janela.mainloop()
