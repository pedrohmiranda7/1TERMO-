# Exercício 6
# Desligar o PC (comando para Windows)
# os.system("Shutdown / s /t 0") #CUIDADO: este comando irá desligar o computador imediatamente!
# os.system("echo Desligamento simulado. Comando de desligamento comentado para segurança.")

with open("Desliga.bat" , "w") as desligar:
    desligar.write("shutdown -s -t 3600 -c \"Desligamento programado para daqui 1 hora. Salve seu trabalho!\"")
    # -s: comando para desligar
    # -t: tempo para definir
    # -a cancelar desligamento 

with open("Desliga.bat", "r") as desligar:
    conteúdo = desligar.read()
    print(conteúdo)

