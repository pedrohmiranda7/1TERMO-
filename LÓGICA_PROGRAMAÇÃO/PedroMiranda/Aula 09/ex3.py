# Exercício 3
# Escrever um programa mais simples com testes de tratamento de erros, como por exemplo, solicitar ao usuário um número. O programa deve tratar os seguintes erros:
# - ValueError: se o usuário digitar um valor que não seja um número.
# - ZeroDivisionError: se o usuário digitar zero como divisor 

print("Tratamento de erros")
try: 
    variavel = int(input("Digite o número: "))
    n1 = int(input("Digite o primeiro valor"))
    n2 = int(input("Digite o segundo valor"))
    resultado = n1 / n2
    print(f"O resultado da divisão é: {resultado:.2f}")

except ValueError:
    print(f"Erro: Valor desconhecido")

except ZeroDivisionError:
    print(f"Valor não permitido")              