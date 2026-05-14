# Clean Code - Aula 8
# Para que usar?
# Como usar?
print("Clean Code - Aula 8")
aula = 8
print(f"Estamos na aula {aula} de Clean Code")

# Manipulação de arquivos e Texto
texto = "Python é muito legal!"
print(texto.strip().upper()) # "PYTHON"
print(texto.strip().lower()) # "python"
print(texto.strip().capitalize()) # "Python"
print(texto.strip().title()) # "Python"
print(texto.strip().replace(" ", "_")) # "Python"
print(texto.strip().split()) # ["Python"]

# Escrevendo
with open("notas.txt", "w") as arquivo:
    arquivo.write("Estudar Python  hoje!")
    arquivo.write("\nLer sobre Clean Code.")

# Lendo
with open("notas.txt", "r") as arquivo:
    conteúdo = arquivo.read()
    print(conteúdo)

# Execução de comandos do sistema
import os #importa o módulo os para interagir com o sistema operacional

# Onde estou?
print(os.getcwd())

# Listar arquivos na pasta
print(os.listdir())
print(os.listdir("..")) #Lista de arquivos da pasta pai
print(os.listdir("..\\..")) #Lista de arquivos da pasta avô
print(os.listdir("C:\\")) #Lista de arquivos da raíz do C
print(os.listdir("C:\\Users")) #lista de arquivos da pasta Users
print(os.listdir("C:\\Users\\Public")) #Lista de arquivos da pasta Public

#Outros comandos úteis:
# Criar pasta
os.mkdir("Nova pasta")
# Renomear pasta
os.rename("Nova_pasta", "Pasta_renomeada")
# Excluir pasta
os.rmdir("Pasta_renomeada")