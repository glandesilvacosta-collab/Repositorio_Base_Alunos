# Crie um código python que peça o valor da conta. Se for maior que R$100,00 
# Adicione uma gorjeta de 10% e exiba o total a pagar
# Caso contrário, adicione uma gorjeta de 5%

# Etapas para resolução

# 1) SOlicitar o valor da conta para o usuário
# 2) Se a conta for maior que 100 adicionar 10% da gorjeta e apresentar o total a pagar
# 3) Se a conta for menor que 100 adicionar 5% de gorjeta e apresentar o total a pagar


valorconta = float(input("Quanto foi gasto na refeição: "))

if valorconta >= 100:
    gorjeta = valorconta * 0.10
else:
    gorjeta = valorconta * 0.05

totalapagar = valorconta + gorjeta

print(f"O total a pagar éa R${totalapagar :2f}")