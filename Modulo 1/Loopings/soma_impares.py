# Crie um programa que some todos os números ímpares que são múltiplos de 3 e 1 a 30 
# E apresente o resultado

# Etapas para resolução
# 1) Criar um for de para captar os números impares
# 2) Criar uma condicional para checar se on úmero é multiplo de 3
# 3) Somar os números que atende a condicional
# 4) Apresentar os resultados



multiplos_tres = 0 # Variavel que irá receber os números ímpares e multiplos de 3
for i in range(1, 31, 2): # Contagem dos números ímpares
    if i % 3 == 0: # Checagem se os números são multiplos de 3
        print(i, end=",") # Apresentação dos numeros que atendem os requisitos
        multiplos_tres += i # Soma dos números que atendem a condicional
print() # Pular a linha
print(f"A soma dos números ímpares e multiplos de 3 é {multiplos_tres}") # Apresentação do resultado
