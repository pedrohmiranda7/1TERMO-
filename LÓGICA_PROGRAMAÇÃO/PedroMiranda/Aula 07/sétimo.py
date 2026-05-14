# Correção

# Exercício 1
# print("Registro de operador")
# operador = input("Digite seu nome")
# turno = input("Digite seu turno")
# print(f"Operador {operador} registrado no turno {turno}. Boa jornada!")


# Exercício 2
# print("Cálculo de Produção")
# produção_hora =int(input("Digite a quantidade de peças produzidas em 1 hora"))
# produção_turno = produção_hora *8
# print(f"Quantidade de peças produzidas em um turno de 8 horas: {produção_turno}")


# Exercício 3
# print("Conversor de Unidade")
# pressão_bar = float(input("Digite a pressão em Bar"))
# pressão_psi = pressão_bar * 14.5
# print(f"Pressão em PSI: {pressão_psi:.2f}")
# print(f"Pressão em PSI: {pressão_psi}",round(pressão_psi,2))


# Exercício 4
# print("Inspeção de Peças")
# nota1 =float(input("Digite a nota da inspeção 1 (0 a 10)"))
# nota2 =float(input("Digite a nota da inspeção 2 (0 a 10)"))
# nota3 =float(input("Digite a nota da inspeção 3 (0 a 10)"))
# média = (nota1 + nota2 + nota3) / 3
# print(f"Média de qualidade de peça: {média:.2f}")
# print("Média de qualidade de peça:", round(média,2))


# Eercício 5
# print("Termostato Inteligente")
# temperatura = float(input("Digite a temperatura do motor em °C"))
# if temperatura < 40:
#     print("Baixa carga")
# elif 40 <= temperatura <= 70:
#     print("Normal")
# else:
#     print("ALERTA: Resfriamento Ativado!")

# print("Termostato Inteligente - Versão 2")
# temperatura = float(input("Digite a temperatura do motor em °C"))
# if temperatura < 40:
#     print("Baixa carga")
# elif temperatura > 70:
#     print("ALERTA: Resfriamento Ativado!")
# else:
#     print("Normal")


# Exercício 6
# print("Classificador de Lotes")
# código_produto = input("Digite o código do produto")
# if código_produto == "A":
#     print("Alimentos")
# elif código_produto == "E":
#     print("Eletrônicos")
# else:
#     print("Desconhecido")

# print("Classificador de Lotes - Versão 2")
# código_produto = input("Digite o código do produto")
# if código_produto.startswith("A")
#     print("Alimentos")
# elif código_produto.startswith("E")
#     print("Eletrônicos")
# else:
#     print("Desconhecido")


# Exercício 7
# print("Segurança de Operação)
      

# Exercício 8 
# print("Cálculo de Descarte") 
# total_peças = int(input("Digite o total de peças produzidas"))
# total_defeituosas = int(input("Digite o total de peças defeituosas") 
# descarte_percentual = (total_defeituosas / total_peças) * 100
# if descarte_percentual > 5:
#     print("Revisar Processo")
# else:
#     print("Processo Otimizado")
# print(f"Descarte percentual: {descarte_percentual:.2f}%")


# Exercício 9 
# print("Validação de Medida")
# medida = float(input("Digite a medida da peça em MM"))
# if medida <9.8:
#     print("A peça está abaixo da tolerância")
# elif medida > 10.2:
#     print("A peça está acima da tolerância")
# else:
#     print("A peça está dentro da tolerância")


# Exercício 10 
# print("Contagem Regressiva de Setup")
# for contagem in range(10, 0, -1):
#     print(contagem)
# print("Prensa ativada!")


# Exercício 11
# print("Soma de Produção (Acumulador)")
# peso_total = 0
# while True:
#     peso_caixa =float(input("Digite o peso da caixa(0 para parar)"))
#     if peso_caixa == 0:
#         break
#     peso_total += peso_caixa
# print(f"peso total acumulado: {peso_total:.2f}kg")


# Exercício 12
# print("Múltiplas Leituras")
# temperaturas = []
# for i in range(1,6):
#     temp = float(input(f"Digite a temperatura no sensor {i} em °C"))
#     temperaturas.append(temp)

# print(f"Maior temperatura lida: {max(temperaturas):.2f} °C")
# print(f"Menor temperatura lida: {min(temperaturas):.2f} °C")
# print(f"Soma temperatura lida: {sum(temperaturas):.2f} °C")


# Exercício 13
# print("Painel de Login")
# senha_correta = "admin123"
# tentativas = 3
# while tentativas > 0:
#     senha = input("Digite a senha do supervisor")
#     if senha == senha_correta:
#         print("Acesso Permitido")
#         break
#     else:
#         tentativas -= 1
#         print(f"Acesso negado. Tentativas restantes: {tentativas}")
# if tentativas ==0:
#     print("Painel Bloqueado")


# Exercício 14
# print("Simulador de estoque")
# estoque = 100
# while True:
#     print("\nMenu:")
#     print("1. Adicionar itens")
#     print("2. Remover itens")
#     print("3. Sair")
#     escolha = input("Escolha uma opção (1, 2 ou 3)")

#     if escolha ==1:
#         quantidade =int(input("Digite a quantidade de itens a adicionar"))
#         estoque += quantidade
#         print(f"Estoque atualizado: {estoque} itens")
#     elif escolha == "2":
#         quantidade = int(input("Digite a quantidade d itens a remover"))
#         estoque -= quantidade  
#         print(f"Estoque Atualizado: {estoque} itens")
#         if estoque <10:
#             print("Estoque Crítico!")
#     elif escolha == "3":
#         print("Saindo do simulador de estoque")
#         break
#     else:
#         print("Opção inválida. Tente novamente")


# Exercício 15
# print("Relatório de Turno Completo")
# total_peças = 5
# peças_aprovadas = 0
# for i in range(1, total_peças + 1):
#     diâmetro = float(input(f"Digite o diâmetro de peça {i} em MM"))
#     if 19.9 <= diâmetro <= 20.1:
#         peças_aprovadas += 1
# eficiência = (peças_aprovadas / total_peças) * 100
# print(f"Total de peças aprovadas: {peças_aprovadas}")
# print(f"Eficiência do lote: {eficiência:.2f}%")

