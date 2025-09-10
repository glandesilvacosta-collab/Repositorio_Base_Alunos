# Crie um código Python que verifique se a senha digitada pelo usuário for "1234", exiba acesso permitido.

# Etapas
# 1) Criar uma variavel e atribuir a ela uma senha
# 2) Através de um input solicitar a senha ao usuário
# 3) Através da condicional checar se a senha é igual a senha armazenada
# 4) Liberar ou não o acesso ao usuário


senhacerta = "1234"
senha = float(input("Digite sua senha: "))

if senha == senhacerta:
    print("Acesso concedido")
else:
    print("Acesso negado")

