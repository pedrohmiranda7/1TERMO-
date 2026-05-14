for i in range(1, 11):
    print(f"\nTabuada do {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")

#Lista de temperaturas lidas pelo sensor por minuto
leituras = [70, 75, 82, 98, 110, 85, 80]

for temp in leituras:
    if temp > 100:
        print(f"CRÍTICO: {temp}°C detectado! Acionando parada de emergência.")
        break #O loop para aqui e NÃO lê os próximos valores (85 e 80)
    print(f"Temperatura está em {temp}°C. Operação normal.")

    print("Sistema desligado. Aguardando manutenção.")
    

materiais = ["metal", "metal", "plástico", "metal", "vidro", "metal"]
for peca in materiais:
    if peca!= "metal":
        print(f"Aviso: Peça de {peca} detectada. Desviando para descarte...")
        continue #Pula o restante do código abaixo e vai para a próxima peça

    #Este código só roda se a peça for de metal
    print(f"Processando peça de {peca}. Furando e polindo...")

print("Fim do lote de produção.")

#Exercício 1
#Tente criar um código que conte de 1 a 10, mas use o continue para não imprimir o número 5 (simulando uma falha de sensor específica no item 5).

from time import sleep
for i in range(1,11):
    if i == 5:
        print(f"Falha ao ler o n° {i}")
        sleep(1.8)
        continue
    print(i)
    sleep(0.7)
print("Acabou")


    #Exercício 2
    #Simule um semáforo com parada para cada cor. Determine um tempo que deseja para que quando mudar para tal cor ele represente uma pausa.

from time import sleep
print("vermelho=1")
print("amarelo=2")
print("verde=3")
vermelho = 1
amarelo = 2
verde = 3
cores = (input("Qual cor você deseja?"))

if cores ==3:
    print("verde")
    sleep(5)
elif cores ==1:
    print("Vermelho")
    sleep(3)
elif cores ==2:
    print("Amarelo")
    sleep(2)
else:
    print("Somente essas cores!!") 


# Exercício 4 - Soma de Cargas de Energia (for)
# Uma fábrica tem 5 máquinas. Peça ao usuário (via input dentro do loop) o consumo em kWh de cada uma das 5 máquinas. Ao final do loop, o programa deve exibir o consumo total da fábrica.

for i in range (5):
    consumo = float (input(f"Digite o valor do consumo das máquinas: \n"))
    total = consumo + i
    print ("o valor final do consumo das máquinas é:" , total)

    #Exercício 5 - Identificador de Peças Defeituosas (for + if)
    #Percorra uma lista de medidas de peças:
    #Medidas = [50.1, 49.8, 52.0, 50.0, 48.5].
    #O padrão de qualidade aceita apenas peças com exatamente 50.0 ou mais.
    #Use um for para ler a lista e, para cada peça, diga se ele está "Aprovada" ou "Rejeitada".
    
medida = [50.1, 49.8, 52.0, 48.5]
for i in range(medida):
    if i > 50.0:
        print(f"{i} peça aprovada")

    elif i <50.0:
        print(f"{i} peça reprovada")

    else:
        print("Sistema encerrado")
 
 
#  Exercício 6 - Uma balança industrial está pesando um lote de 6 sacos de insumos. O peso ideal de casa saco é de 50 kg, mas o sistema aceita variações.

peso = float(input("Digite o peso"))
for i in range(1,6):
    if peso >50.0:
        print(f"{peso} dentro do padrão")

    elif peso < 50.0:
        print(f"{peso} fora do padrão")

# Exercício 7: Sistema Inteligente de Manutenção
# Crie um programa que receba dois dados: a pressão atual (float) e as horas de uso acumuladas (int) de uma turbina.
# O programa deve classsificar o estado de uma máquina seguindo esta hierarquia:
# Crítico (Prioridade 1): Se a pressão for maior que 100 OU as horas de uso forem maiores que 10.000
# Mensagem: "PARADA IMEDIATA: Risco de falha catastrófica."
# Alerta (Prioridade 2): Se a pressão estiver entre 80 e 100 (inclusive).
# Mensagem: "MANUTENÇÃO AGENDADA: Pressão acima do ideal."
# Monitoramento (Prioridade 3): Se as horas de uso forem entre 8.000 e 10.000.
# Mensagem: "AVISO: Máquina aproximando-se da revisão de 10K horas."
# Normal: Para qualquer outro caso que não se encaixe nos acima.
# Mensagem: "SISTEMA OPERAL: Todos os parâmetros dentro da normalidade."