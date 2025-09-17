# Crie um programa que leia o peso de 5 pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

# Etapas para resolução:
# 1) Crie uma lista vazia para receber os pesos
# 2) Crie um for para receber os pesos das 5 pessoas
# 3) Adicione os pesos recebidos na lsta
# 4) Utilize as funções max() e min() ou ordene a lista e busque o primeiro e últio elemento
# 5) Apresente os resultados

pesos = []

for i in range(4):
    peso = float(input(f"Digite o peso da {i+1}ª pessoa: "))
    pesos.append(peso)
print(f"O maior peso é {max(pesos)}")
print(f"O menor peso é {min(pesos)}")   