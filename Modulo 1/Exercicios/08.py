#8) Verificação de múltiplo de 5. Peça um número ao usuário e verifique se ele é múltiplo de 5. Se for, exiba "Múltiplo de 5", senão exiba "Não é múltiplo de 5".

numero = float(input("Digite um número: "))

if numero % 5 == 0:
    print(f"O número {numero} é múltiplo de 5.")
else:
    print(f"O número {numero} não é múltiplo de 5.")