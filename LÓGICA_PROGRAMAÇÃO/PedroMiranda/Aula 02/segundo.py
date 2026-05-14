# Funções

a = 1 # a é uma variável
b = 2
c = a + b
print('O valor de A e B é:', c)

# Variáveis sõa formas de armazenar informações

# Função Input
# Irá permitir inserir informações
input("Qual o seu nome?")

# Operadores matemáticos
# + = soma
# - = subtração
# * = multiplicação
# / = divisão

# Exemplo 1
# \n quebra linha
v1 = input("Digite o primeiro valor: \n")
v2 = input("Digite o segundo valor: \n")
vtotal = v1 + v2
print("Qual é o resultado?", vtotal)

# int = retorna valores inteiros Ex 1, -5
# float = valores com casas decimais Ex 10.2 , -10.1

# Exemplo 2
x1 = int(input('Digite o primeiro valor da subtração: \n'))
x2 = int(input('Digite o segundo valor da subtração: \n'))
xtotal = x1 - x2
print('Qual é o valor do X \n', xtotal)

# Exemplo 3 e Exemplo 4
# Multiplicar e Dividir
m1 = int(input('Digite o primeiro valor da multiplicação: \n'))
m2 = int(input('Digite o segundo valor da multiplicação: \n'))
mtotal = m1 * m2
print('Qual é o valor do M \n', mtotal)

print("Vamos dividir \n")
d1 = float(input("Digite o primeiro valor desejado \n"))
d2 = float(input("Digite o segundo valor desejado \n"))
dtotal = d1 / d2
print("Sua divisão é: \n", dtotal)

# Concatenar
print('Eu gosto de programar \n' + '\n Python \n')

# Exercício 1
# Apresente as mensagens
# O programa deve permitir que você digite seu nome, seu curso e sua idade e também seu hobby

nome = input("Qual é o seu nome \n")
curso = input("Qual é o seu curso? \n")
idade = int(input("Qual é a sua idade? \n"))
hobby = input("Qual é o seu hobby? \n")

print("Qual é o seu nome?", nome)
print("Qual é o seu curso?", curso)
print("Qual é a sua idade?", idade)
print("Qual é o seu hobby?", hobby)

# Exercício 2
# Calculadora de IMC (Potência e Divisão)
# O Índice de Massa Corporal (IMC) é calculado dividindo o peso pela altura ao quadrado
print("Bem-Vindo a nossa Calculadora de IMC")

p1 = float(input('Digite o primeiro valor da divisão: \n'))
p2 = float(input('Digite o segundo valor da divisão: \n'))
ptotal = p1 / (p2 * p2)
print('O valor do seu IMC é: \n', ptotal)

# Exercício 3
# Calculadora completa com os quatros operadores matemáticos
print("Bem-Vindo a nossa Calculadora")
n1 = float(input("Digite o primeiro valor \n"))
n2 = float(input("Digite o segundo valor \n"))
adição = n1 + n2
subtração = n1 - n2
divisão = n1 / n2
multiplicação = n1 * n2
print("A soma é \n", n1 + n2)
print("A subtração é \n", n1 - n2)
print("A divisão é \n", n1 / n2)
print("A multiplicação é \n", n1 * n2)

# Converter em string
# Adição = n1 + n2
#print("A soma é", str(adição))