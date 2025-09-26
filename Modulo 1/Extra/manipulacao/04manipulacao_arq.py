# Adicionar uma nova frase no meu arquivo

# Caso eu queira adicionar uma nova frase no arquivo já criado
# Utilizamos o modo 'a' para não subescrever o conteúdo existente

with open('mensagem.txt', 'a', encoding='utf-8') as arquivo:
    arquivo.write('\nAprender python é muito bom!')