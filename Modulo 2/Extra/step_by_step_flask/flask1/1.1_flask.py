# Exercicio 1.3: Parâmetros na URL (Rotas dinâmicas)
# Adicione uma nova rota '/sobre' que retorna uma mensagem
# Crie um app Flask básico que exibe "Olá, Mundo!" na rota principal (/).

from flask import Flask

app = Flask(__name__) # representa o nome do arquivo
# O código eve ser escrito entre o app e o app.run

@app.route('/') # @decorador de função
def home():

    return 'Olá Mundo!'

if __name__ == '__main__':
    app.run(debug=True)