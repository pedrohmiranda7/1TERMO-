# # Exercício 1: Registro de Operador: Peça o nome do operador e o turno (A, B ou C). Exiba:  "Operador [Nome] registrado no Turno [Turno]. Boa jornada!"

# import tkinter as tk
# from tkinter import messagebox, ttk

# def operador():
#     nome = ent_nome.get()
#     turno = ent_turno.get()

#     if nome == "" or turno == "":
#         messagebox.showwarning("Cadastro", f"Erro", "Por favor, preencha os campos corretamente.")
#     else:
#         messagebox.showinfo("Cadastro", f"Operador {nome} registrado no turno {turno}. Boa jornada!")

# # Criação da janela 
# janela = tk.Tk()
# janela.title("Registro de operador")
# janela.geometry("800x600")

# # Labels e Entries
# lbl_nome = tk.Label(janela, text="Nome:", font=("Arial", 14))
# lbl_nome.grid(row=0, column=0, pady=10, padx=10)

# ent_nome = tk.Entry(janela, font=("Arial", 14), width=30)
# ent_nome.grid(row=0, column=1, pady=10, padx=10)

# lbl_turno = tk.Label(janela, text="Turno (A, B ou C):", font=("Arial", 14))
# lbl_turno.grid(row=1, column=0, pady=10, padx=10)

# ent_turno = tk.Entry(janela, font=("Arial", 14), width=30)
# ent_turno.grid(row=1, column=1, pady=10, padx=10)

# # Botão para registrar operador
# btn_registrar = tk.Button(janela, text="Registro de operador", font=("Arial", 14), bg="blue", fg="white", command=operador)
# btn_registrar.grid(row=2, column=0, columnspan=2, pady=20, padx=20)
# btn_fechar_janela = tk.Button(janela, text="Fechar", font=("Arial", 14), bg="red", fg="white", command=janela.destroy)
# btn_fechar_janela.grid(row=6, column=0, columnspan=2, pady=20, padx=20)


# # Loop principal
# janela.mainloop()

# # Exercício 2: Cálculo de Produção: Peça a quantidade de peças produzidas em 1 hora. Calcule e exiba quantas peças serão produzidas em um turno de 8 horas.

# import tkinter as tk
# from tkinter import messagebox

# def calcular_producao():
#     quantidade = ent_quantidade.get()

#     if quantidade == "":
#         messagebox.showwarning("Cálculo de produção", f"Erro", "Por favor, preencha o campo corretamente.")
#     else:
#         producao_turno = int(quantidade) * 8
#         messagebox.showinfo("Cálculo de produção", f"Serão produzidas {producao_turno} peças em um turno de 8 horas.")


#  # Criação da janela 
# janela = tk.Tk()
# janela.title("Cálculo de Produção")
# janela.geometry("800x600")

# # Labels e Entries
# lbl_quantidade = tk.Label(janela, text="Digite a quantidade de peças produzidas em 1 hora:", font=("Arial", 14))
# lbl_quantidade.grid(row=0, column=0, pady=10, padx=10)

# ent_quantidade = tk.Entry(janela, font=("Arial", 14), width=30)
# ent_quantidade.grid(row=0, column=1, pady=10, padx=10)

# # Botão para calcular produção
# btn_calcular_producao = tk.Button(janela, text="Calcular Produção", font=("Arial", 14), bg="blue", fg="white", command=calcular_producao)
# btn_calcular_producao.grid(row=2, column=0, columnspan=2, pady=20, padx=20)
# btn_fechar_janela = tk.Button(janela, text="Fechar", font=("Arial", 14), bg="red", fg="white", command=janela.destroy)
# btn_fechar_janela.grid(row=6, column=0, columnspan=2, pady=20, padx=20)


# # # Loop principal
# janela.mainloop()

# Exercício 3: Conversor de Unidade: O sistema lê uma pressão em Bar. Converta para PSI (1 Bar ≈ 14.5 PSI) e exiba com duas casas decimais.

# import tkinter as tk
# from tkinter import messagebox

# def converter_pressao():
#     pressao_bar = ent_pressao_bar.get()

#     if pressao_bar == "":
#         messagebox.showwarning("Conversor de unidade", f"Erro", "Por favor, preencha o campo corretamente.")
#     else:
#         pressao_psi = float(pressao_bar) * 14.5
#         messagebox.showinfo("Conversor de unidade", f"{pressao_bar} Bar é equivalente a {pressao_psi:.2f} PSI.")

# # Criação da janela
# janela = tk.Tk()        
# janela.title("Conversor de Unidade")
# janela.geometry("800x600")

# # Labels e Entries
# lbl_pressao_bar = tk.Label(janela, text="Digite a pressão em Bar:", font=("Arial", 14))
# lbl_pressao_bar.grid(row=0, column=0, pady=10, padx=10)

# ent_pressao_bar = tk.Entry(janela, font=("Arial", 14), width=30)
# ent_pressao_bar.grid(row=0, column=1, pady=10, padx=10) 

# # Botão para converter pressão
# btn_converter_pressao = tk.Button(janela, text="Converter Pressão", font=("Arial", 14), bg="blue", fg="white", command=converter_pressao)
# btn_converter_pressao.grid(row=2, column=0, columnspan=2, pady  =20, padx=20)
# btn_fechar_janela = tk.Button(janela, text="Fechar", font=("Arial", 14), bg="red", fg="white", command=janela.destroy)
# btn_fechar_janela.grid(row=6, column=0, columnspan=2, pady=20, padx=20)


# # Loop principal
# janela.mainloop()

# # Exercício 4: Média de Qualidade: Peça 3 notas de inspeção de uma peça (0 a 10). Exiba a média aritmética simples delas.

# import tkinter as tk
# from tkinter import messagebox  

# def calcular_media():
#     nota1 = ent_nota1.get()
#     nota2 = ent_nota2.get()
#     nota3 = ent_nota3.get()

#     if nota1 == "" or nota2 == "" or nota3 == "":
#         messagebox.showwarning("Cálculo da Média", f"Erro", "Por favor, preencha todos os campos corretamente.")
#     else:
#         media = (float(nota1) + float(nota2) + float(nota3)) / 3
#         messagebox.showinfo("Cálculo da Média", f"A média aritmética é: {media:.2f}")

# # Criação da janela
# janela = tk.Tk()
# janela.title("Média de Qualidade")
# janela.geometry("800x600")  

# # Labels e Entries
# lbl_nota1 = tk.Label(janela, text="Digite a primeira nota de inspeção (0 a 10):", font=("Arial", 14))
# lbl_nota1.grid(row=0, column=0, pady=10, padx=10)

# ent_nota1 = tk.Entry(janela, font=("Arial", 14), width=30)
# ent_nota1.grid(row=0, column=1, pady=10, padx=10)   

# lbl_nota2 = tk.Label(janela, text="Digite a segunda nota de inspeção (0 a 10):", font=("Arial", 14))
# lbl_nota2.grid(row=1, column=0, pady=10, padx=10)

# ent_nota2 = tk.Entry(janela, font=("Arial", 14), width=30)
# ent_nota2.grid(row=1, column=1, pady=10, padx=10)

# lbl_nota3 = tk.Label(janela, text="Digite a terceira nota de inspeção (0 a 10):", font=("Arial", 14))
# lbl_nota3.grid(row=2, column=0, pady=10, padx=  10)

# ent_nota3 = tk.Entry(janela, font=("Arial", 14), width=30)
# ent_nota3.grid(row=2, column=1, pady=10, padx=10)

# # Botão para calcular média
# btn_calcular_media = tk.Button(janela, text="Calcular Média", font=("Arial", 14), bg="blue", fg="white", command=calcular_media)
# btn_calcular_media.grid(row=3, column=0, columnspan=2, pady=20, padx=20)
# btn_fechar_janela = tk.Button(janela, text="Fechar", font=("Arial", 14), bg="red", fg="white", command=janela.destroy)
# btn_fechar_janela.grid(row=6, column=0, columnspan=2, pady=20, padx=20)

# # Loop principal
# janela.mainloop()

# # Exercício 5: Termostato Inteligente: Peça a temperatura de um motor.
# # ● Abaixo de 40°C: "Baixa carga".
# # ● Entre 40°C e 70°C: "Normal".
# # ● Acima de 70°C: "ALERTA: Resfriamento Ativado!".

# import tkinter as tk
# from tkinter import messagebox

# def verificar_temperatura():
#     temperatura = ent_temperatura.get()

#     if temperatura == "":
#         messagebox.showwarning("Termostato Inteligente", f"Erro", "Por favor, preencha o campo corretamente.")
#     else:
#         temp = float(temperatura)
#         if temp < 40:
#             messagebox.showinfo("Termostato Inteligente", "Baixa carga.")
#         elif 40 <= temp <= 70:
#             messagebox.showinfo("Termostato Inteligente", "Normal.")
#         else:
#             messagebox.showinfo("Termostato Inteligente", "ALERTA: Resfriamento Ativado!")
        
# # Criação da janela
# janela = tk.Tk()
# janela.title("Termostato Inteligente")
# janela.geometry("800x600")

# # Labels e Entries
# lbl_temperatura = tk.Label(janela, text="Digite a temperatura do motor (°C):", font=("Arial", 14))
# lbl_temperatura.grid(row=0, column=0, pady=10, padx=10)

# ent_temperatura = tk.Entry(janela, font=("Arial", 14), width=30)
# ent_temperatura.grid(row=0, column=1, pady=10, padx=10)

# # Botão para verificar temperatura
# btn_verificar_temperatura = tk.Button(janela, text="Verificar Temperatura do Motor", font=("Arial", 14), bg="blue", fg="white", command=verificar_temperatura)
# btn_verificar_temperatura.grid(row=2, column=0, columnspan=2, pady=20, padx=20)
# btn_fechar_janela = tk.Button(janela, text="Fechar", font=("Arial", 14), bg="red", fg="white", command=janela.destroy)
# btn_fechar_janela.grid(row=6, column=0, columnspan=2, pady=20, padx=20)

# # Loop principal   
# janela.mainloop()

# # Exercício 6: Classificador de Lotes: O usuário insere o código do produto. Se começar com "A", exiba "Alimentos". Se "E", "Eletrônicos". Para qualquer outro, "Desconhecido".

# import tkinter as tk
# from tkinter import messagebox

# def classificar_lote():
#     codigo_produto = ent_codigo_produto.get()

#     if codigo_produto == "":
#         messagebox.showwarning("Classificador de Lotes", f"Erro", "Por favor, preencha o campo corretamente.")
#     else:
#         if codigo_produto.startswith("A"):
#             messagebox.showinfo("Classificador de Lotes", "Alimentos.")
#         elif codigo_produto.startswith("E"):
#             messagebox.showinfo("Classificador de Lotes", "Eletrônicos.")
#         else:
#             messagebox.showinfo("Classificador de Lotes", "Desconhecido.")

# # Criação da janela
# janela = tk.Tk()
# janela.title("Classificador de Lotes")
# janela.geometry("800x600")

# # Labels e Entries
# lbl_codigo_produto = tk.Label(janela, text="Digite o código do produto (A ou E):", font=("Arial", 14))
# lbl_codigo_produto.grid(row=0, column=0, pady=10, padx=10)

# ent_codigo_produto = tk.Entry(janela, font=("Arial", 14), width=30)
# ent_codigo_produto.grid(row=0, column=1, pady=10, padx=10)

# # Botão para classificar lote
# btn_classificar_lote = tk.Button(janela, text="Classificar Lote", font=("Arial", 14), bg="blue", fg="white", command=classificar_lote)
# btn_classificar_lote.grid(row=2, column=0, columnspan=2, pady=20, padx=20)
# btn_fechar_janela = tk.Button(janela, text="Fechar", font=("Arial", 14), bg="red", fg="white", command=janela.destroy)
# btn_fechar_janela.grid(row=6, column=0, columnspan=2, pady=20, padx=20)

# # Loop principal   
# janela.mainloop()

# Exercício 7: Segurança de operação: A máquina só liga se o sensor_porta == "fechada" E o botao_emergencia == "desligado". Peça esses dois inputs e diga se a máquina pode iniciar.

# import tkinter as tk
# from tkinter import messagebox

# def verificar_seguranca():
#     sensor_porta = ent_sensor_porta.get()
#     botao_emergencia = ent_botao_emergencia.get()

#     if sensor_porta == "" or botao_emergencia == "":
#         messagebox.showwarning("Segurança de Operação", f"Erro", "Por favor, preencha todos os campos corretamente.")
#     else:
#         if sensor_porta.lower() == "fechada" and botao_emergencia.lower() == "desligado":
#             messagebox.showinfo("Segurança de Operação", "A máquina pode iniciar.")
#         else:
#             messagebox.showinfo("Segurança de Operação", "A máquina não pode iniciar. Verifique os sensores e o botão de emergência.")

# # Criação da janela
# janela = tk.Tk()   
# janela.title("Segurança de Operação")
# janela.geometry("800x600")

# # Labels e Entries
# lbl_sensor_porta = tk.Label(janela, text="Estado do sensor da porta (fechada/aberta):", font=("Arial", 14))
# lbl_sensor_porta.grid(row=0, column=0, pady=10, padx=10)

# ent_sensor_porta = tk.Entry(janela, font=("Arial", 14), width=30)
# ent_sensor_porta.grid(row=0, column=1, pady=10, padx=10)

# lbl_botao_emergencia = tk.Label(janela, text="Estado do botão de emergência (ligado/desligado):", font=("Arial", 14))
# lbl_botao_emergencia.grid(row=1, column=0, pady=10, padx=10)
# ent_botao_emergencia = tk.Entry(janela, font=("Arial", 14), width=30)
# ent_botao_emergencia.grid(row=1, column=1, pady=10, padx=10)

# # Botão para verificar segurança
# btn_verificar_seguranca = tk.Button(janela, text="Verificar Segurança de Operação", font=("Arial", 14), bg="blue", fg="white", command=verificar_seguranca)
# btn_verificar_seguranca.grid(row=2, column=0, columnspan=2, pady=20, padx=20)
# btn_fechar_janela = tk.Button(janela, text="Fechar", font=("Arial", 14), bg="red", fg="white", command=janela.destroy)
# btn_fechar_janela.grid(row=6, column=0, columnspan=2, pady=20, padx=20)

# # Loop principal
# janela.mainloop()

# # Exercício 8: Cálculo de descarte: Peça o total de peças produzidas e o total de defeituosas. Se o descarte for maior que 5%, exiba "Revisar Processo", caso contrário, Processo Otimizado".

# import tkinter as tk
# from tkinter import messagebox

# def calcular_descarte():
#     total_pecas = ent_total_pecas.get()
#     total_defeituosas = ent_total_defeituosas.get()

#     if total_pecas == "" or total_defeituosas == "":
#         messagebox.showwarning("Cálculo de Descarte", f"Erro", "Por favor, preencha todos os campos corretamente.")
#     else:
#         descarte = (int(total_defeituosas) / int(total_pecas)) * 100
#         if descarte > 5:
#             messagebox.showinfo("Cálculo de Descarte", f"Descarte: {descarte:.2f}%. Revisar Processo.")
#         else:
#             messagebox.showinfo("Cálculo de Descarte", f"Descarte: {descarte:.2f}%. Processo Otimizado.")

# # Criação da janela
# janela = tk.Tk()
# janela.title("Cálculo de Descarte")
# janela.geometry("800x600")

# # Labels e Entries
# lbl_total_pecas = tk.Label(janela, text ="Digite o total de peças produzidas:", font = ("Arial", 14))
# lbl_total_pecas.grid(row=0, column=0, pady=10, padx=10)

# ent_total_pecas = tk.Entry(janela, font = ("Arial", 14), width=30)
# ent_total_pecas.grid(row=0, column=1, pady=10, padx=10)

# lbl_total_defeituosas = tk.Label(janela, text ="Digite o total de peças defeituosas:", font = ("Arial", 14))
# lbl_total_defeituosas.grid(row=1, column=0, pady=10, padx=10)

# ent_total_defeituosas = tk.Entry(janela, font = ("Arial", 14), width=30)
# ent_total_defeituosas.grid(row=1, column=1, pady=10, padx=10)

# # Botão para calcular descarte
# btn_calcular_descarte = tk.Button(janela, text="Calcular Descarte", font=("Arial", 14), bg="blue", fg="white", command=calcular_descarte)
# btn_calcular_descarte.grid(row=2, column=0, columnspan=2, pady=20, padx=20)
# btn_fechar_janela = tk.Button(janela, text="Fechar", font=("Arial", 14), bg="red", fg="white", command=janela.destroy)
# btn_fechar_janela.grid(row=6, column=0, columnspan=2, pady=20, padx=20)

# # Loop principal
# janela.mainloop()

# # Exercício 9: Validação de Medida: Uma peça deve ter entre 9.8mm e 10.2mm. Peça a medida e diga se está dentro da tolerância, acima ou abaixo.

# import tkinter as tk
# from tkinter import messagebox


# def validacao_medida():
#     medida = ent_medida.get() 
#     if medida == "":
#         messagebox.showwarning("Validação de medida", f"Erro", "Por favor, preencha o campo de medida.")
#     else:
#         medida_float = float(medida)
#         if 9.8 <= medida_float <= 10.2:
#             messagebox.showinfo("Validação de medida", "A medida está dentro da tolerância.")
#         elif medida_float < 9.8:
#             messagebox.showinfo("Validação de medida", "A medida está abaixo da tolerância.")
#         else:
#             messagebox.showinfo("Validação de medida", "A medida está acima da tolerância.")

# # Criação da janela
# janela = tk.Tk()
# janela.title("Validação de Medida")
# janela.geometry("800x600")

# # Labels e Entries
# lbl_medida = tk.Label(janela, text="Digite a medida da peça em mm:", font=("Arial", 14))
# lbl_medida.grid(row=0, column=0, pady=10, padx=10)

# ent_medida = tk.Entry(janela, font=("Arial", 14), width=30)
# ent_medida.grid(row=0, column=1, pady=10, padx=10)

# # Botão para validar medida
# btn_confirmar_medida = tk.Button(janela, text = "Validar Medida", font = ("Arial", 14), bg = "blue", fg = "white", command=validacao_medida)
# btn_confirmar_medida.grid(row=1, column=0, columnspan=2, pady=20, padx=20)

# # Loop principal
# janela.mainloop()

# # Exercício 10: Contagem Regressiva de Setup: Use um for para fazer uma contagem regressiva de 10 até 1 para o início de uma prensa, e finalize com "Prensa Ativada".

# import tkinter as tk
# from tkinter import messagebox

# def contagem_regressiva():
#     for i in range(10, 0, -1):
#         messagebox.showinfo("Contagem Regressiva", f"Contagem Regressiva {i}")
#     messagebox.showinfo("Contagem Regressiva", "Prensa Ativada!")

# # Criação da janela
# janela = tk.Tk()
# janela.title("Contagem Regressiva")
# janela.geometry("800x600")

# # Botão para iniciar contagem regressiva
# btn_iniciar_contagem_regressiva = tk.Button(janela, text="Iniciar Contagem Regressiva", font=("Arial", 14), bg="blue", fg="white", command=contagem_regressiva)
# btn_iniciar_contagem_regressiva.grid(row=0, column=0, pady=20, padx=20)
# btn_fechar_janela = tk.Button(janela, text="Fechar", font=("Arial", 14), bg="red", fg="white", command=janela.destroy)
# btn_fechar_janela.grid(row=6, column=0, pady=20, padx=20)

# # Loop principal
# janela.mainloop()

# # Exercício 11: Soma de Produção (Acumulador): Use um while para pedir o peso de várias caixas. O loop para quando o usuário digitar 0. No fim, mostre o peso total acumulado.

# from tkinter import *

# janela = Tk()
# janela.title("Soma de Produção")

# largura = 800
# altura = 600

# largura_tela = janela.winfo_screenwidth()
# altura_tela = janela.winfo_screenheight()

# x = (largura_tela // 2) - (largura // 2)
# y = (altura_tela // 2) - (altura // 2)

# janela.geometry(f"{largura}x{altura}+{x}+{y}")

# total = 0

# def adicionar():
#     global total

#     peso = float(entry_peso.get())

#     if peso == 0:
#         lbl_resultado.config(text=f"Peso total acumulado: {total:.2f} kg")
#     else:
#         total += peso
#         lbl_resultado.config(text=f"Total atual: {total:.2f} kg")

#     entry_peso.delete(0, END)

# Label(janela, text="Peso da caixa:", font=("Arial", 14)).pack(pady=10)

# entry_peso = Entry(janela, font=("Arial", 14))
# entry_peso.pack()

# Button(janela, text="Adicionar", command=adicionar).pack(pady=10)

# lbl_resultado = Label(janela, text="", font=("Arial", 14))
# lbl_resultado.pack(pady=20)

# janela.mainloop()


# # Exercício 12: Múltiplas Leituras: Use um for para pedir a temperatura de 5 sensores diferentes. Ao final, mostre qual foi a maior temperatura lida.

# from tkinter import *

# janela = Tk()
# janela.title("Exercício 12")

# largura = 800
# altura = 600

# largura_tela = janela.winfo_screenwidth()
# altura_tela = janela.winfo_screenheight()

# x = (largura_tela // 2) - (largura // 2)
# y = (altura_tela // 2) - (altura // 2)

# janela.geometry(f"{largura}x{altura}+{x}+{y}")

# contador = 0
# maior = float("-inf")

# def registrar():
#     global contador, maior

#     temp = float(entry_temp.get())

#     contador += 1

#     if temp > maior:
#         maior = temp

#     if contador == 5:
#         lbl_resultado.config(text=f"Maior temperatura: {maior:.2f} °C")
#     else:
#         lbl_resultado.config(text=f"Leitura {contador}/5 registrada")

#     entry_temp.delete(0, END)

# Label(janela, text="Temperatura:", font=("Arial", 14)).pack(pady=10)

# entry_temp = Entry(janela, font=("Arial", 14))
# entry_temp.pack()

# Button(janela, text="Registrar", command=registrar).pack(pady=10)

# lbl_resultado = Label(janela, text="", font=("Arial", 14))
# lbl_resultado.pack(pady=20)

# janela.mainloop()

# # Exercício 13: 13.Painel de Login: Crie um while que peça a senha do supervisor ("admin123"). Enquanto ele errar, o programa diz "Acesso Negado". Ele tem apenas 3 tentativas. Se esgotar, exiba "Painel Bloqueado".

# from tkinter import *

# janela = Tk()
# janela.title("Exercício 13")

# largura = 800
# altura = 600

# largura_tela = janela.winfo_screenwidth()
# altura_tela = janela.winfo_screenheight()

# x = (largura_tela // 2) - (largura // 2)
# y = (altura_tela // 2) - (altura // 2)

# janela.geometry(f"{largura}x{altura}+{x}+{y}")

# tentativas = 3

# def verificar():
#     global tentativas

#     senha = entry_senha.get()

#     if senha == "admin123":
#         lbl_resultado.config(text="Acesso Permitido")
#     else:
#         tentativas -= 1

#         if tentativas > 0:
#             lbl_resultado.config(
#                 text=f"Acesso Negado\nTentativas restantes: {tentativas}"
#             )
#         else:
#             lbl_resultado.config(text="Painel Bloqueado")

#     entry_senha.delete(0, END)

# Label(janela, text="Digite a senha:", font=("Arial", 14)).pack(pady=10)

# entry_senha = Entry(janela, show="*", font=("Arial", 14))
# entry_senha.pack()

# Button(janela, text="Entrar", command=verificar).pack(pady=10)

# lbl_resultado = Label(janela, text="", font=("Arial", 14))
# lbl_resultado.pack(pady=20)

# janela.mainloop()

# # Exercício 14:Simulador de Estoque: Comece com estoque = 100. Crie um menu (while) onde o usuário pode: (1) Adicionar itens, (2) Remover itens ou (3) Sair. Se o estoque ficar abaixo de 10, avise: "Estoque Crítico!".

# from tkinter import *

# janela = Tk()
# janela.title("Exercício 14")

# largura = 800
# altura = 600

# largura_tela = janela.winfo_screenwidth()
# altura_tela = janela.winfo_screenheight()

# x = (largura_tela // 2) - (largura // 2)
# y = (altura_tela // 2) - (altura // 2)

# janela.geometry(f"{largura}x{altura}+{x}+{y}")

# estoque = 100

# def adicionar():
#     global estoque

#     estoque += int(entry_qtd.get())

#     lbl_resultado.config(text=f"Estoque atual: {estoque}")

#     entry_qtd.delete(0, END)

# def remover():
#     global estoque

#     estoque -= int(entry_qtd.get())

#     if estoque < 10:
#         lbl_resultado.config(
#             text=f"Estoque atual: {estoque}\nESTOQUE CRÍTICO!"
#         )
#     else:
#         lbl_resultado.config(text=f"Estoque atual: {estoque}")

#     entry_qtd.delete(0, END)

# Label(janela, text="Quantidade:", font=("Arial", 14)).pack(pady=10)

# entry_qtd = Entry(janela, font=("Arial", 14))
# entry_qtd.pack()

# Button(janela, text="Adicionar", command=adicionar).pack(pady=5)

# Button(janela, text="Remover", command=remover).pack(pady=5)

# lbl_resultado = Label(janela, text="Estoque inicial: 100", font=("Arial", 14))
# lbl_resultado.pack(pady=20)

# janela.mainloop()

# # Exercício 15: Relatório de Turno Completo: Use um for para processar 5 peças. Para cada peça, peça o diâmetro. Se a peça for aprovada (entre 19.9 e 20.1), conte-a. No final do loop, exiba o total de peças aprovadas e a porcentagem de eficiência do lote.

# from tkinter import *

# janela = Tk()
# janela.title("Exercício 15")

# largura = 800
# altura = 600

# largura_tela = janela.winfo_screenwidth()
# altura_tela = janela.winfo_screenheight()

# x = (largura_tela // 2) - (largura // 2)
# y = (altura_tela // 2) - (altura // 2)

# janela.geometry(f"{largura}x{altura}+{x}+{y}")

# contador = 0
# aprovadas = 0

# def verificar():
#     global contador, aprovadas

#     diametro = float(entry_diametro.get())

#     contador += 1

#     if 19.9 <= diametro <= 20.1:
#         aprovadas += 1

#     if contador == 5:
#         eficiencia = (aprovadas / 5) * 100

#         lbl_resultado.config(
#             text=f"Peças aprovadas: {aprovadas}\nEficiência: {eficiencia:.1f}%"
#         )
#     else:
#         lbl_resultado.config(text=f"Peça {contador}/5 registrada")

#     entry_diametro.delete(0, END)

# Label(janela, text="Diâmetro da peça:", font=("Arial", 14)).pack(pady=10)

# entry_diametro = Entry(janela, font=("Arial", 14))
# entry_diametro.pack()

# Button(janela, text="Registrar", command=verificar).pack(pady=10)

# lbl_resultado = Label(janela, text="", font=("Arial", 14))
# lbl_resultado.pack(pady=20)

# janela.mainloop()