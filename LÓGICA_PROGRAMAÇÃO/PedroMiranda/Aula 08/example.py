# Exemplo

# Exemplo 2: Criar um script de limpeza de arquivos 
# Escreva um script que liste os arquivos de uma pasta e exclua os arquivos com extensão ".temp". O script deve exibir uma mensagem para cada arquivo excluído.

import os
pasta = os.listdir()
for arquivo in pasta:
    if arquivo.endswith(".txt"):
        os.remove(arquivo)
        print(f"Arquivo {arquivo} excluído.")
print("Limpeza de arquivos concluída.")
