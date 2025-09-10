# Criar um código python que indique se a temperatura está agradavel ou não
#Condições:
# Temperatura >= 30° informar que está muito quente
# Temperatura >= 20° informar que a temperatura está agradável
#Temperatura >= 10° informar que esta frio
#Temperatura abaixo de 10° informar que está muito frio

# Etapas para resolução:
# 1) Solicitar a temperatura para o usuário
# 2) verificar a condicional
# 3) imprimir a resposta segundo a temperaratura







temperatura = float(input("Digite a temperatura em ° Celsius"))

if temperatura >=30:
    print("Está quente!")
elif temperatura >= 20:
    print("Está agradável!")
elif temperatura >= 10:
    print("Está frio!")
else:
    print("Está frio pra caralho")
    