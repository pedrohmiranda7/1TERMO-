import tkinter as tk
from tkinter import messagebox


# função principal
def cadastrar():

    nome = entrada_nome.get()

    curso = entrada_curso.get().lower()

    nr10 = entrada_nr10.get().lower()

    nr35 = entrada_nr35.get().lower()

    ano = int(entrada_ano.get())


    mensagem = "Nome: " + nome + "\n\n"


    # verificar curso
    if curso == "elétrica" or curso == "eletrica":

        mensagem += "Curso: Elétrica\n\n"

        mensagem += "EPIs obrigatórios:\n"

        mensagem += "Luvas\n"

        mensagem += "Botas dielétricas\n\n"


    elif curso == "trabalho em altura":

        mensagem += "Curso: Trabalho em Altura\n\n"

        mensagem += "EPIs obrigatórios:\n"

        mensagem += "Cinturão de segurança\n"

        mensagem += "Talabarte\n\n"


    else:

        mensagem += "Curso não encontrado\n\n"


    # status
    mensagem += "NR-10: " + nr10 + "\n"

    mensagem += "NR-35: " + nr35 + "\n\n"


    # verificar treinamento
    if nr10 == "pendente" or nr35 == "pendente":

        mensagem += "Status: Treinamento vencido\n\n"

    else:

        mensagem += "Status: Treinamento OK\n\n"


    # verificar ano
    if ano == 2026:

        mensagem += "Ano do treinamento válido"

    else:

        mensagem += "Ano do treinamento vencido"


    messagebox.showinfo("Cadastro do Cliente", mensagem)



# ENTER vai para próximo campo
def enter(evento):

    evento.widget.tk_focusNext().focus()

    return "break"



# último ENTER envia tudo
def enter_final(evento):

    cadastrar()



# sair
def sair():

    janela.destroy()



# janela
janela = tk.Tk()

janela.title("Controle de Treinamentos")

janela.geometry("1000x850")

janela.configure(bg="plum")



# título
titulo = tk.Label(

    janela,

    text="Controle de Treinamentos",

    bg="purple",

    fg="white",

    font=("Arial", 28)

)

titulo.pack(pady=40)



# nome
tk.Label(janela, text="Nome", bg="purple", fg="white", font=("Arial", 18)).pack(pady=10)

entrada_nome = tk.Entry(janela, font=("Arial", 18), width=30)
entrada_nome.pack(pady=10)
entrada_nome.bind("<Return>", enter)



# curso
tk.Label(janela, text="Curso: Elétrica ou Trabalho em Altura", bg="purple", fg="white", font=("Arial", 18)).pack(pady=10)

entrada_curso = tk.Entry(janela, font=("Arial", 18), width=30)
entrada_curso.pack(pady=10)
entrada_curso.bind("<Return>", enter)



# nr10
tk.Label(janela, text="NR-10: OK ou Pendente", bg="purple", fg="white", font=("Arial", 18)).pack(pady=10)

entrada_nr10 = tk.Entry(janela, font=("Arial", 18), width=30)
entrada_nr10.pack(pady=10)
entrada_nr10.bind("<Return>", enter)



# nr35
tk.Label(janela, text="NR-35: OK ou Pendente", bg="purple", fg="white", font=("Arial", 18)).pack(pady=10)

entrada_nr35 = tk.Entry(janela, font=("Arial", 18), width=30)
entrada_nr35.pack(pady=10)
entrada_nr35.bind("<Return>", enter)



# ano
tk.Label(janela, text="Ano do treinamento", bg="purple", fg="white", font=("Arial", 18)).pack(pady=10)

entrada_ano = tk.Entry(janela, font=("Arial", 18), width=30)
entrada_ano.pack(pady=10)

# ENTER final envia tudo
entrada_ano.bind("<Return>", enter_final)



# botão cadastrar
botao_cadastrar = tk.Button(

    janela,

    text="Cadastrar Cliente",

    command=cadastrar,

    font=("Arial", 18),

    width=20,

    bg="white"

)

botao_cadastrar.pack(pady=30)



# botão sair
botao_sair = tk.Button(

    janela,

    text="Sair",

    command=sair,

    font=("Arial", 18),

    width=20,

    bg="white"

)

botao_sair.pack(pady=10)



janela.mainloop()