# Exercício 1: Crie uma aplicação que faça o cálculo de idade de pessoas.
# Deve perguntar o nome da pessoa e o ano de nascimento.

import tkinter as tk
from tkinter import messagebox

def calcular_idade():
    nome = ent_nome.get()
    ano_nascimento = ent_ano_nascimento.get()

    if nome == "" or ano_nascimento == "":
        messagebox.showwarning("Cálculo de idade", "Erro", "Por favor, preencha todos os campos.")
    else:
        idade = 2026 - int(ano_nascimento)
        messagebox.showinfo("Cálculo de idade", f"Sua idade é {idade} anos.")

# Criação da janela 
janela = tk.Tk()
janela.title("Cálculo de Idade")
janela.geometry("800x800")

# Labels e Entries
lbl_nome = tk.Label(janela, text="Nome:", font=("Arial", 14))
lbl_nome.grid(row=0, column=0, pady=10, padx=10)

ent_nome = tk.Entry(janela, font=("Arial", 14), width=30)
ent_nome.grid(row=0, column=1, pady=10, padx=10)

lbl_ano_nascimento = tk.Label(janela, text="Ano de Nascimento:", font=("Arial", 14))
lbl_ano_nascimento.grid(row=1, column=0, pady=10, padx=10)

ent_ano_nascimento = tk.Entry(janela, font=("Arial", 14), width=30)
ent_ano_nascimento.grid(row=1, column=1, pady=10, padx=10)

# Botão para calcular idade
btn_calcular_idade = tk.Button(janela, text="Calcular Idade", font=("Arial", 14), bg="blue", fg="white", command=calcular_idade)
btn_calcular_idade.grid(row=2, column=0, columnspan=2, pady=20, padx=20)

# Loop principal
janela.mainloop()