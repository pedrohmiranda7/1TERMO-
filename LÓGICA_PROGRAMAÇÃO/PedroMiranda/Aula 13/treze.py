# Revisão Tkinter

import tkinter as tk
from tkinter import messagebox, ttk

# DEF funções em bloco
def realizar_cadastro():
    #.get
    nome_usuario = ent_nome_usuario.get()
    curso_usuario = ent_curso_usuario.get()
    nome_escola = cmb_nome_escola.get()

    if nome_usuario == "" and curso_usuario == "" and nome_escola == "":
        messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")
    else:
        messagebox.showinfo("Cadastro Realizado", f"Nome: {nome_usuario}\nCurso: {curso_usuario}\nEscola: {nome_escola}")
        

# 0 - Etapa
janela = tk.Tk()
janela.title("Revisão Tkinter")
janela.geometry("800x800")
janela.configure(bg="white")

# 1 - Etapa Componentes
# Labels = Rótulos ou os nossos antigos prints
lbl_nome_usuario = tk.Label(janela, text= "Digite seu nome:", font=("Arial", 14), fg="black")
lbl_nome_usuario.grid(row=0, column=0, pady=10, padx=10)

lbl_curso_usuario = tk.Label(janela, text= "Digite seu curso:", font =("Arial", 14), fg="black")
lbl_curso_usuario.grid(row=1, column=0, pady=20, padx=20)

lbl_nome_escola = tk.Label(janela, text= "Digite sua escola:", font =("Arial", 14), fg="black")
lbl_nome_escola.grid(row=2, column=0, pady=10, padx=10)

# Entrys = Caixa de texto ou antigos input
ent_nome_usuario = tk.Entry(janela, font=("Arial", 14), width=30)
ent_nome_usuario.grid(row=0, column=1, pady=10, padx=10)
ent_curso_usuario = tk.Entry(janela, font=("Arial", 14), width=30)
ent_curso_usuario.grid(row=1, column=1, pady=10, padx=10)

# ComboBox = Caixa de seleção
cmb_nome_escola = ttk.Combobox(janela, values =["SESI408","SESI5"], width=30, font=("Arial", 14), state="readonly")
cmb_nome_escola.grid(row=2, column=1, pady=10, padx=10)

# Botões = Botões de clique
btn_realizar_cadastro = tk.Button(janela, text="Realizar Cadastro", font=("Arial", 14), bg="blue", fg="white", command=realizar_cadastro)
btn_realizar_cadastro.grid(row=5, column=0, columnspan=2, pady=20, padx=20)
btn_fechar_janela = tk.Button(janela, text="Fechar", font=("Arial", 14), bg="red", fg="white", command=janela.destroy)
btn_fechar_janela.grid(row=6, column=0, columnspan=2, pady=20, padx=20)

# 4 - Etapa Loop
janela.mainloop()
