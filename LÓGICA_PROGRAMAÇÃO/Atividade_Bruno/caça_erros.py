# Exercício 1
idade = int(input("Digite sua idade:\n "))

if idade >= 18:
    print("Você é maior de idade.")
# (Eu apenas adicionei um "int")

# Exercício 2
nome = "Mariana"

print("Seja bem-vinda", nome)
# (Eu tirei as aspas do nome porque ele estava sendo tratado como um texto e não como uma variável)

# Exercício 3
numero = 10

if numero > 5:
    print("O número é maior que cinco.")
else:
    print("O número é menor ou igual a cinco.")
# (Eu apenas alinhei cada coisa, no caso, eu joguei os prints para dentro do if e do else)

# Exercício 4
usuario = "aluno123"

if usuario == "aluno123":
    print("Login realizado com sucesso.")
# (Eu apenas acrescentei dois pontos (:) na frente do "aluno123")

# Exercício 5
clima = "ensolarado"

if clima == "chuvoso":
    print("Leve um guarda-chuva!")
# (Eu adicionei mais um igual (=) no if clima, para poder fazer uma comparação e não uma atribuição)

# Exercício 6
pontos = 50

print(f"Parabéns! Você fez {pontos} pontos.")
# (Eu adicionei um "f" antes da string para poder chamar a váriavel depois dentro da chave)

# Exercício 7
nota = 9.5

if nota >= 9:
    print("Excelente!")
elif nota >= 7:
    print("Aprovado")
# (Eu apenas inverti os valores do if e elif)

# Exercício 8
for i in range(1, 6):
    print(i)
# (Eu modifiquei o range, no caso, (1, 6), porque se colocar (5), ele lista 0 até quatro)

# Exercício 9
tentativas = 1

while tentativas <= 3:
    print("Tentando conectar...")
    tentativas += 1
# (Eu tive que colocar embaixo do código que a cada tentativa ele subia mais um, fazendo com que o while não fique em loop infinito)

# Exercício 10
senha = ""

while senha != "python123":
    senha = input("Digite a senha secreta: ")

print("Acesso concedido!")
# (Eu adicionei um ponto de exclamação para mostrar que a senha "python123" e não a "", para fazer que enquanto a pessoa não digitar "python123", o sistema fique pedindo para colocar a senha certa)
