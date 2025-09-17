# Solicite ao usuário 4 notas.
# Calcule a média
# Informe se o aluno está aprovado (media>=7), recuperação(5<media>7) ou reprovado.
# Apresente as notas que o aluno tirou, a media e o status da sua solicitação  

# lista
# For
# if/elif/else



notas = [] # Lista vazia para armazenar as notas

for i in range(4):  # Repete 4 vezes (de 0 até 3)
    nota = float(input(f"Digite a nota {i+1}: "))  # Pede uma nota ao usuário e converte para float
    notas.append(nota)  # Adiciona a nota digitada na lista 'notas'

media = sum(notas) / len(notas)  # Calcula a média das notas

if media >= 7:
    print(f"Aprovado, sua média foi {media}")
elif 5 < media < 7:
    print(f"Recuperação, sua média foi {media}")
else:
    print(f"Reprovado, sua média foi {media}")

print("Notas:", notas)