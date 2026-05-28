# Exercício> Crie uma interface gráfica que calcule a média de três notas digitadas pelo usuário. A interface deve conter campos para o usuário inserir as notas e um botão para calcular a média. Ao clicar no botão, a média deve ser exibida em uma mensagem.

import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Seja bem-vindo à calculadora do Pedro!")
janela.geometry("1000x800") #Largura e Altura
janela.configure(bg="#f0f0f0") # Cor do fundo

def mostrar_mensagem():
    try:
        # messagebox.showinfo("Sucesso!", f"Sua média é {resultado}")

        n1 = float(nota_media1.get())
        n2 = float(nota_media2.get())
        n3 = float(nota_media3.get())
        resultado = (n1 +n2 + n3)/3

        messagebox.showinfo("Média calculada", f"O resultado é {resultado}")
    except ValueError:
        print("Digite valores corretos")
    
    if resultado > 200:
        messagebox.showwarning("Aviso", "Por favor, digite números menores")
    else: 
        messagebox.showinfo("Número válido!")
       


#Componentes
lbl_titulo = tk.Label(janela, text="Calculadora do Pedro", font=("Arial", 14, "bold"))
lbl_titulo.pack(pady=15)

lbl_titulo1 = tk.Label(janela, text="Digite o primeiro valor", font=("Arial", 14, "bold"))
lbl_titulo1.pack(pady=10)
nota_media1 = tk.Entry(janela, font=("Arial", 12))
nota_media1.pack(pady=5)

lbl_titulo2 = tk.Label(janela, text="Digite o segundo valor", font=("Arial", 14, "bold"))
lbl_titulo2.pack(pady=10)
nota_media2 = tk.Entry(janela, font=("Arial", 12))
nota_media2.pack(pady=5)

lbl_titulo3 = tk.Label(janela, text="Digite o terceiro valor", font=("Arial", 14, "bold"))
lbl_titulo3.pack(pady=10)
nota_media3 = tk.Entry(janela, font=("Arial", 12))
nota_media3.pack(pady=5)

btn_enviar = tk.Button(text ="Enviar", command=mostrar_mensagem)
btn_enviar.pack(pady=15)

janela.mainloop()