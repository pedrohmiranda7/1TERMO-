# Exercício 1
print("Bem-vindo ao mundo da programação em Python!")

# Exercício 2
print("Pedro Henrique Miranda \n")
print("15")

# Exercício 3
print("Bem-vindo à calculadora! \n")
print("135 + 246 \n")
print("512 - 128 \n") 

num1 = 135
num2 = 246
num3 = 512
num4 = 128

print("Resultado da soma =", num1 + num2, end="\n\n")
print("Resultado da subtração =", num3 - num4)

# Exercício 4
print("15 x 8 =", 15 * 8, end="\n\n")
print("78 / 3 =", 78 / 3)

# Exercício 5
print("5³ =", 5 ** 3)

# Exercício 6

nome = str("Pedro")
sobrenome = str("Miranda")

print(nome + " " + sobrenome)

# Exercício 7
pecas_produzidas = int(input("\nDigite a quantidade de peças produzidas:\n"))
pecas_defeituosas = int(input("\nDigite a quantidade de peças defeituosas:\n"))   

pecas_total = pecas_produzidas - pecas_defeituosas
taxa_aproveitamento = pecas_total / pecas_produzidas

print("\nPeças boas:", pecas_total)
print("\nTaxa de aproveitamento:", taxa_aproveitamento)

# Exercício 8
idade = 25

print("Eu tenho", idade, "anos e, em 10 anos, terei", idade + 10, "anos.")

# Exercício 9
custo_hotel = 250.50
custo_passagem = 412
dias_viagem = float(int(input("\nDigite quantos dias você vai ficar: \n")))
resultado_final = (custo_hotel * dias_viagem) + custo_passagem
print("\nCusto total da viagem: \n R$", resultado_final)

# Exercício 10
produto = input("Digite o nome do produto:\n ")
quantidade = int(input("\nDigite a quantidade vendida:\n "))
preco_unitario = int(float(input("\nDigite o preço unitário:\n R$ ")))

total = quantidade * preco_unitario

print("\n==========================")
print("   Relatório de Vendas")
print("==========================")
print("Produto:", produto)
print("Quantidade vendida:", quantidade)
print(f"Preço unitário: R$ {preco_unitario:.2f}")
print(f"Total de vendas: R$ {total:.2f}")
print("==========================")