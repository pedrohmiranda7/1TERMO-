def cadastro ():
    nome = input("Digite seu nome: \n")
    setor = input("Digite seu setor: (E = Elétrica / TA = Trabalho em Altura): \n")
    status = input("Digite seu status de treinamento: (1 = NR- 10 / 2 = NR-35 / 3 = BRIGADA:) \n")
    
    # E = "Elétrica"
    # TA = "Trabalho em Altura"

    # 1 = NR-10
    # 2 = NR-35
    # 3 = BRIGADA

    if setor == "E":
        print(f"É obrigatório o uso de luvas de alta tensão e botas dielétricas!")
    elif setor == "TA":
        print(f"É obrigatório o uso de cinturão de segurança e talabarte")    
    else:
        print(f"Bom trabalho")

def alerta_de_reciclagem():
    tempo = int(input("Qual foi o ano em que ocorreu o último treinamento?: \n"))
    ano_atual = int(input("Qual é o ano em que estamos?: \n"))
    resultado_total = ano_atual - tempo 

    while resultado_total > 2:
        print(f"Treinamento vencido, mandar para reciclagem...")
    
    while resultado_total < 2:
        print("Treinamento válido") 

print(cadastro())
print(alerta_de_reciclagem())


# total_funcionarios = 5
# treinamentos_em_dia = 3

# # Mostrar resumo na tela
# print("RESUMO")
# print("Total de funcionários:", total_funcionarios)
# print("Treinamentos em dia:", treinamentos_em_dia)