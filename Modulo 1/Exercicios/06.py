#6) Acesso ao Wi-Fi Peça a senha do Wi-Fi ao usuário. Se for: "senha123", exiba "Conectado" caso contrário, exiba "Senha incorreta".

senhawifi = "senha123"
senhainserida = input("Qual sua senha?")

if senhawifi == senhainserida:
    print("Conectado")
else:
    print("Senha Incorreta")