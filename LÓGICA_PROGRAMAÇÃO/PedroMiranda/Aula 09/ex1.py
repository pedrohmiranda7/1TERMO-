# Exercício 1:
# Escreva um programa que solicite ao usuário um número inteiro e calcule a média de uma lista de números. O programa deve tratar os seguintes erros:
# - ValueError: se o usuário digitar um valor que não seja um número inteiro

print("Exemplo de tratamento de erros")
try:
    num1 = int(input("Digite o primeiro número..."))
    num2 = int(input("Digite o segundo número..."))
    resultado = num1 / num2
    print(f"O resultado da divisão é: {resultado:.2f}")

except ValueError:
    print("Erro: Entrada inválida. Por favor, digite um número inteiro.")

    for i in range(1,2):
        print(f"{num1} x {i} = {num1 * i}")
        número = float(input("Digite um valor"))

