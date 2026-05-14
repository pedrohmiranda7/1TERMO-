# Exercício 8
# Criar um script de monitoramento de temperatura:
# Escreva um script que monitore a temperatura de um motor. O script deve ler a temperatura de um arquivo "temperatura.txt" e exibir uma mensagem de alerta se a temperatura estiver acima de 70°C

with open("temperatura.txt") as arquivo_origem:
    conteúdo = arquivo_origem.read()

temperatura = float(input("Digite a temperatura do motor"))
if temperatura > 70:
    print("ALERTA!")

# não terminei e esta errado algumas coisas