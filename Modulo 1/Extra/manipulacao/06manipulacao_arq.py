# Ler o arquivo e exibir o texto em letras maiúsculas

with open('mensagem.txt', 'r') as arquivo:
    for linha in arquivo: # Aqui percorremos as linhas do arquivo
        print(linha.strip().upper()) # Imprimimos cada linha em maiúscula e 
# tiramos os espaços com o strip()