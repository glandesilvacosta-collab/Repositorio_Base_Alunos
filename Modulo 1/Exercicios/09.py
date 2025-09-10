#9) Desconto em compras por valor mínimo. Se o valor da compra for maior que R$150,00, aplique um desconto de R$20,00. Caso contrário, não aplique desconto.

valorcompra = float(input("Qual foi o valor da compra? "))
desconto = 20

if valorcompra > 150:
    desconto = 20
    precofinal = valorcompra - desconto
    print(f"Valor com desconto: {precofinal}")
else:
    precofinal = valorcompra
    print(f"Desconto não aplicado")
    