# 1. Registro de Operador: Peça o nome do operador e o turno (A, B ou C). Exiba:
# "Operador [Nome] registrado no Turno [Turno]. Boa jornada!"

# nome = input("Digite o seu nome")
# turno = input("Digite seu turno")
# print(f"Seu nome é {nome} e o seu turno é {turno}. Boa jornada")



#2. Cálculo de Produção: Peça a quantidade de peças produzidas em 1 hora. Calcule e
# exiba quantas peças serão produzidas em um turno de 8 horas.

# peças = int(input("Digite a quantidade de peças produzidas em 8 horas"))
# resultado = peças*8
# print (f"Serão produzidas {resultado} peças em 8 horas")



# 3. Conversor de Unidade: O sistema lê uma pressão em Bar. Converta para PSI (1 Bar
# ≈ 14.5 PSI) e exiba com duas casas decimais.

# bar = float(input("Digite o valor da pressão de bar"))
# variável = 14.5
# resultado = bar*variável
# print(f"Resultado de bar é {resultado}")



# 4. Média de Qualidade: Peça 3 notas de inspeção de uma peça (0 a 10). Exiba a média
# aritmética simples delas.

# n1 = int(input("Digite a primeira peça de 0 a 10:"))
# n2 = int(input("Digite a segunda peça de 0 a 10:"))
# n3 = int(input("Digite a terceira peça de 0 a 10:"))
# variável = 3
# resultado = (n1+n2+n3)/3
# print(f"A média aritmética é {resultado}!")



# 5. Termostato Inteligente: Peça a temperatura de um motor.
# ● Abaixo de 40°C: "Baixa carga".
# ● Entre 40°C e 70°C: "Normal".
# ● Acima de 70°C: "ALERTA: Resfriamento Ativado!

# print("Bem vindo ao Termostato Inteligente! \n Digite a temperatura do motor:")
# temperatura = int(input("Digite sua temperatura"))

# if temperatura < 40:
#     print("Baixa Carga")
# elif 40 < temperatura < 70:
#     print("Normal")
# elif temperatura > 70:
#     print("ALERTA: Resfriamento ativado!")
# else:
#     print("Sistema Finalizado")
   
    

# 6. Classificador de Lotes: O usuário insere o código do produto. Se começar com "A",
# exiba "Alimentos". Se "E", "Eletrônicos". Para qualquer outro, "Desconhecido"

# print("Bem vindo ao classificador de lotes!")
# lotes = str(input("Digite o que deseja: \n"))

# if lotes == "A":
#     print("Alimento")
# elif lotes == "E":
#     print("Eletrônico")
# else:
#     print("Descohecido")



# 7. Segurança de Operação: A máquina só liga se o sensor_porta == "fechada" E o
# botao_emergencia == "desligado". Peça esses dois inputs e diga se a máquina pode
# iniciar.

# print("Sistema de Segurança de Operação da Máquina!")
# sensorporta = str(input("Digite se a porta está aberta ou fechada \n"))
# botaoemergencia = str(input("Digite se o botão de emergência está ligado ou desligado\n"))

# if sensorporta == "aberta" and botaoemergencia == "ligado":
#     print("A máquina não pode ser inicializada")
# elif sensorporta == "fechada" and botaoemergencia == "desligado":
#     print("A máquina vai ser inicializada!")
# else:
#     print("Sistema finalizado")



# 8. Cálculo de Descarte: Peça o total de peças produzidas e o total de defeituosas. Se
# o descarte for maior que 5% do total, exiba "Revisar Processo", caso contrário,
# "Processo Otimizado".

# total = int(input("Digite o total de peças produzidas: \n"))
# defeito = int(input("Digite o total de peças defeituosas: \n"))
# if defeito>=(total * 0.05):
#     print ("Revisar processo")
# else:
#     print("Processo finalizado")



# 9. Validação de Medida: Uma peça deve ter entre 9.8mm e 10.2mm. Peça a medida e
# diga se está dentro da tolerância, acima ou abaixo

# peça = float(input("Digite a medida da peça"))
# if 9.8 < peça < 10.2:
#     print("Está dentro da tolerância")
# elif peça < 9.8:
#     print("Está abaixo da tolerância")
# else:
#     print("Está acima da tolerância")



#     10. Contagem Regressiva de Setup: Use um for para fazer uma contagem regressiva
# de 10 até 1 para o início de uma prensa, e finalize com "Prensa Ativada!".

# print("Iniciando contagem regressiva: \n")
# for i in range(10,0,-1):
#     print(i)
# print(f"Prensa ativada!")



# 11. .Soma de Produção (Acumulador): Use um while para pedir o peso de várias caixas.
# O loop para quando o usuário digitar 0. No fim, mostre o peso total acumulado.

# totalpeso = 0
# while True:
#     peso = float(input("Digite o peso da caixa: \n"))
#     if peso == 0:
#      break
#     totalpeso += peso
# print(f"Peso total acumulado: {totalpeso}")



# # 12. .Múltiplas Leituras: Use um for para pedir a temperatura de 5 sensores diferentes.
# # Ao final, mostre qual foi a maior temperatura lida.

# mtemp=0
# for i in range(5):
#     temp= float(input(f"Temperatura do sensor:"))
#     if temp > mtemp:
#      total = i+temp
# print(f"Temperatura captada", (total))



# # 13. Painel de Login: Crie um while que peça a senha do supervisor ("admin123").
# # Enquanto ele errar, o programa diz "Acesso Negado". Ele tem apenas 3 tentativas.
# # Se esgotar, exiba "Painel Bloqueado".

# senha = "admin123"
# while True