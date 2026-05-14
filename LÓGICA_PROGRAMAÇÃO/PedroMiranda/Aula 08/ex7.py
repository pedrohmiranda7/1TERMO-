# Exercício 7
# Escreva um script que crie um arquivo de backup do arquivo "notas.txt" com o nome "notas_backup.txt". O script deve ler o conteúdo de "notas.txt" e escrever no novo arquivo.

with open("notas.txt", "r") as arquivo_origem:
    conteúdo = arquivo_origem.read()

with open("notas_backup.txt", "w") as backup:
    backup.write(conteúdo)
print("Backup criado com sucesso!")
