# Crie um código em python que peça um número ao usuário e exiba "Número par" se ele for diisível por 2

# Etapas de resolução

# 1) Solicitar um número ao usuário
# 2) Verificar se o número par ou impar
# 3) Informar se o número é par ou impar


numero = float(input("Digite um número: "))

if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é impar.")
