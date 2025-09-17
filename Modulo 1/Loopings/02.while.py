bombons = 10

while bombons > 0: # Enquanto bombons > o o while continua executando
    print(f"Eu tenho {bombons} bombons.")
    bombons -= 1 # Diminui um bombom
    print(f"Comi 1 e fiquei com {bombons} bombons.") # Informa a quantidade
    # De bombons após a subtração
    if bombons == 0:
        print("acabaram os bombons")