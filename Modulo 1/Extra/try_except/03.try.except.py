# Crie uma função chamada calculadora que receba três parâmetros:
# dois números e uma operação( +, -, *, /)
# A função deve retornar o resultado da operação, mas precisa
# Tratar as seguintes exceções
# Divisão por zero(ZeroDivisionError)
# Tipo de dado inválido (ValueError)

def calculadora():
    try:
        n = input('Digite um número ou x para sair do sistema: ')
        if n.lower() == 'x':
            print('Até breve.')
            return
        n1=input('Digite um número ou x para sair do sistema: ')
        if n1.lower() == 'x':
            print('Até breve.')
        operador = input('Informe um operador matemático (+, -, *, /) ou x para sair do sistema: ')
        if operador.lower() == 'x':
            print('Até breve. ')
            return
        # Converter as entradas (inputs) em float
        n = float(n)
        n1 = float(n1)

        if operador == "+":
            resultado = n + n1
        elif operador == "-":
            resultado = n - n1
        elif operador == "*":
            resultado = n * n1  
        elif operador == "/":
            resultado = n / n1  
            if n1 == 0:
                raise ZeroDivisionError('Não é possível dividir por zero.')
            resultado = n / n1
        else:
            print('Operador inválido. Tente novamente.')
            return
        print(f'Operação: {n} {operador} {n1} = {resultado}')
    except ValueError:
        print('Valor inválido. Tente novamente.')
    except ZeroDivisionError as zero:
        print(zero)
calculadora()
    