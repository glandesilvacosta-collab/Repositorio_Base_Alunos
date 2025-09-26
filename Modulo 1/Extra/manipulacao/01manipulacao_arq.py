# Criar arquivo, recebendo informação do usuário

#solicitação de entrada
nome = input("Digite seu nome: ")
email = input("Digite seu email: ")

#criação do arquivo
arquivo = open("pessoas.txt", 'a', encoding='utf-8') # Estamos criando o arquivo 
# armazenando o na variavel arquivo, o modo 'a' escreve sempre no final,
# enconding utf 8 é para utilizar o conjunto de caracteres que engloba a lingua portuguesa
arquivo.write(nome + '|'+ email + '\n') #.write é para escrever e o /n
# é para pular uma linha
arquivo.close() #.close é para fechar o arquivo