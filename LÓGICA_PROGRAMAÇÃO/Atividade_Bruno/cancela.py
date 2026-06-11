from math import ceil
from datetime import datetime

# =========================
# 1. CONFIGURAÇÕES INICIAIS
# =========================

TOTAL_VAGAS = 500
vagas_ocupadas = int(input("Digite o número de vagas ocupadas: "))

tipo_acesso = input("Entrada por TAG ou TICKET? ").upper()

if tipo_acesso == "TICKET":

    if vagas_ocupadas >= TOTAL_VAGAS:
        print("Estacionamento lotado!")
        print("Cancela fechada para novos clientes.")
        exit()  # encerra o programa

# =========================
# 2. FLUXO DE ENTRADA
# =========================

tipo_acesso = input("Entrada por TAG ou TICKET? ").upper()

if tipo_acesso == "TAG":

    tag_ativa = input("A TAG está ativa? (S/N): ").upper()

    if tag_ativa == "S":

        id_tag = input("Digite o ID da TAG: ")

        horario_entrada = datetime.now()

        print("TAG válida!")
        print("Cancela aberta automaticamente.")
        print("ID da TAG:", id_tag)
        print("Horário de entrada:", horario_entrada)

        vagas_ocupadas += 1

    else:
        print("TAG inválida. Entrada negada.")

# =========================
# 3. TABELA DE VALORES
# =========================

print("\n=== SAÍDA ===")

perdeu_ticket = input("Perdeu o ticket? (S/N): ").upper()

if perdeu_ticket == "S":

    # Situação especial
    valor = 50.00

else:

    minutos = int(input("Tempo de permanência (em minutos): "))

    # Até 15 minutos = grátis
    if minutos <= 15:
        valor = 0

    # Até 3 horas = R$15
    elif minutos <= 180:
        valor = 15

    # Acima de 3 horas
    else:
        horas_extras = ceil((minutos - 180) / 60)
        valor = 15 + (horas_extras * 3)

    # Desconto para TAG
    if tipo_acesso == "TAG":
        valor = valor * 0.90

print(f"\nValor a pagar: R$ {valor:.2f}")

# =========================
# 4. SITUAÇÕES ESPECIAIS
# =========================

status_pagamento = input("Pagamento realizado? (S/N): ").upper()

if status_pagamento == "S":
    print("Pagamento confirmado.")
    print("Cancela de saída aberta.")
    vagas_ocupadas -= 1
else:
    print("Pagamento não realizado.")
    print("Cancela de saída fechada.")

# Relatório final
print("\n=== RELATÓRIO ===")
print("Vagas ocupadas:", vagas_ocupadas)
print("Vagas disponíveis:", TOTAL_VAGAS - vagas_ocupadas)