# Ler um arquivo

arquivo = open('pessoa.txt', 'r',) # A leitura está sendo feita na memória
conteudo = arquivo.read() # Eu armazenoa leitura em uma variavel
print(conteudo) # Peço para imprimir a leitura
arquivo.close() # sempre que utilizamos a função open precisamos
# fechar o arquivo
