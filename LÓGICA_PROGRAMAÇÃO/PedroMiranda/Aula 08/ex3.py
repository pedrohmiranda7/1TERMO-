# Exercício 3:
# Crie uma pasta chamada "projetos" e depois renomeie para "meus_projetos". Por fim, exclua a pasta.

import os
#Criar pasta
os.mkdir("projetos")
#Renomear pasta
os.rename("projetos", "meus_projetos")
# Excluir pasta
os.rmdir("meus_projetos")