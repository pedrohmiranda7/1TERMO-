# Exercício 2
# Escreva um programa que solicite ao usuário uma lista de palavras e conte quantas vezes cada palavra aparece na lista. O programa deve tratar os seguintes erros:
# - ValueError: se o usuário digitar um valor que não seja uma string. 

print("Exemplo de tratamento de erros")
try:
    palavra = str(input("Digite alguma coisa:"))

except ValueError:
    print("Erro: Valor desconhecido")

for i in range(10):
    print(f"{palavra}")

# Exemplo do professor:
 
try:
    palavras = input("Digite uma lista de palavras separadas por espaço...").split()
    contagem = {}
    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
    print("Contagem de palavras:")
    for palavra, contagem in contagem.items():
        print(f"{palavra}: {contagem}")
except ValueError:
    print("Erro: Entrada inválida. Por favor, digite uma lista de palavras separadas por espaço.")
