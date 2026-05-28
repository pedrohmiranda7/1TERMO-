# TKINTER

# Componentes Widgets
# tk: Tk() #Janela
# lb: Label() # Rótulo
# bt: Button() # Botão
# et: Entry() # Caixa de texto

import tkinter as tk
from tkinter import messagebox

# 1. Criar a janela principal
janela = tk.Tk()
janela.title("Minha Primeira Janela GUI")
janela.geometry("400x200") #Largura e Altura
janela.configure(bg="#f0f0f0") # Cor do fundo

# 2. Criar a função do botão (evento)
def mostrar_mensagem():
    messagebox.showinfo("Sucesso!", "Você clicou no botão")

# 3. Criar os componentes
lbl_titulo = tk.Label(janela, text="Bem-vindo à nossa aula de Tkinter", font=("Arial", 14, "bold"))
btn_clique = tk.Button(janela, text="Clique Aqui", font =("Arial", 11), bg="#a72ecc", fg="white", command=mostrar_mensagem)
btn_close = tk.Button(janela, text="Fechar", font=("Arial", 14, "bold"), bg="#cce2ee", command=janela.destroy)

# 4. Posicionar os componentes
lbl_titulo.pack(pady=20) #'pady' adiciona um espaçamento vertical
btn_clique.pack(pady=10)
btn_close.pack(pady=5)

# 5. Rodar o loop da interface
janela.mainloop()


import tkinter as tk
from tkinter import messagebox

def saudar_usuario():
    # .get() serve para buscar o texto que vamos digitar

    nome = campo_nome.get()

    if nome == "":
        messagebox.showwarning("Aviso", "Por favor, digite seu nome!")
    else:
        messagebox.showinfo("Saudações Alunos", f"olá, {nome}! Seja bem-vindo ao mundo das interfaces gráficas")

# Configurações da janela 
app = tk.Tk()
app.title = ("Exemplo 1")
app.geometry = ("350x200")

# Componentes
lbl_instrucao = tk.label(app, text="Digite seu nome abaixo:")
lbl_instrucao.pack(pady=10)

campo_nome = tk.Entry(app, font=("Arial", 12))
campo_nome.pack(pady=5)

btn_enviar = tk.Button(app, text ="Enviar", command=saudar_usuario)
btn_enviar.pack(pady=15)

app.mainloop()