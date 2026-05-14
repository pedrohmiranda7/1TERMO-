# Explicação de def: A palavra chave "def" é usada para definir uma função em Python. Uma função é um bloco de código reutilizável que realiza uma tarefa específica.
# return: A palavra-chave "return" é usada para finalizar a execução de uma função e retornar um valor para o local onde a função foi chamada. O valor retornado pode ser usado posteriormente no código.

def nome():
    nome = input("Digite seu nome:")
    return nome
print(f"Olá, {nome()}!")

def valores():
    print("Digite três valores:")
    a = int(input("Digite o primeiro valor: \n"))
    b = int(input("Digite o segundo valor: \n"))
    c = int(input("Digite o terceiro valor: \n"))
    return a, b, c
print(f"O maior valor é: {max(valores())}")

# Reutilizando funções
nome()
valores()

# Conceitos Chave
# def: Indica o início da definição da função.
# Nome: Identifica a função para você chama-lá depois.
# Parâmetros: Dados que a função recebe (opcional)
# return: Envia o resultado de volta para quem chmaou a função (opcional).
def calcular_dobro(numero):
    return numero * 2
# Como usar: resultado = calcular_dobro(5)
print(calcular_dobro(5))
