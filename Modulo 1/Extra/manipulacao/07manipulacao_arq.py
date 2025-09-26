# Criar um arquivo nomes.txt

nomes = ['João\n', 'Maria\n', 'Ana\n'] # Criamos uma lista com nome para ser
# inseridos no arquivo nomes.txt

with open('nomes.txt', 'w', encoding='utf-8') as arquivo: # Estamos criando o arquivo
    arquivo.writelines(nomes) # Estamos pedindo para escrever a lista no arquivo