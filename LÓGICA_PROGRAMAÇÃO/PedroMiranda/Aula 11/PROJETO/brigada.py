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

    if resultado_total > 2:
        print(f"Treinamento vencido, mandar para reciclagem...")
    
    elif resultado_total < 2:
        print("Treinamento válido") 

    else:
        print("O treinamento vai vencer este ano!")

    total_funcionarios = int(input("Digite o total de funcionários: "))
    treinamentos_em_dia = int(input("Digite quantos estão com treinamentos em dia: "))

    # Mostrar resumo na tela
    print("\nRESUMO")
    print("Total de funcionários:", total_funcionarios)
    print("Treinamentos em dia:", treinamentos_em_dia)

print(cadastro())
print(alerta_de_reciclagem())