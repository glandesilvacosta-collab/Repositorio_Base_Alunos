#7) Verificação de turno Peça ao usuário para digitar "M"print para manhã ou qualquer outra tecla para tarde. Se for "M" exiba "Bom dia!" senão exiba "Boa tarde!"

turno = input("Digite 'm' para manhã ou qualquer outra tecla para tarde")

if turno == "m":
    print ("Bom dia!")
else:
    print("Boa tarde!")