# Exercício 4:
# Crie um arquivo chamado "log.txt" e escreva a mensagem "Log de atividades". Depois, leia o comando do arquivo e exiba na tela.

with open("log.txt" , "w") as arquivo:
    arquivo.write("Log de atividades")
with open("log.txt", "r") as arquivo:
    conteúdo = arquivo.read()
    print(conteúdo)
    