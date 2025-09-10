#5) Cálculo de gorjeta Peça o valor da conta. Se for maior que R$100,00, adicione uma gorjeta de 10% e exiba o total a pagar. Caso contrário, adicione uma gorjeta de 5%.


valorconta = float(input("Quanto foi gasto na refeição: "))

if valorconta >= 100:
    gorjeta = valorconta * 0.10
else:
    gorjeta = valorconta * 0.05

totalapagar = valorconta + gorjeta

print(f"O total a pagar éa R${totalapagar:.2f}")