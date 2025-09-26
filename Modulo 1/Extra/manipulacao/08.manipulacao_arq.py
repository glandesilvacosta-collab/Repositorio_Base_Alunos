# Contar quantas linhas tem no arquivo

with open('nomes.txt', 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines() # Aqui estamos lendo o arquivo e armazenando
# a  leitura na variável linhas
    print(f'O arquivo tem {len(linhas)} linhas.') # a função len() conta quantas
    # linhas tem no arquivo lido