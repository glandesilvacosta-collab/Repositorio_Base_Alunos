# Crie um código que receba 3 notas, calcule a média e informe se o aluno está aprovado, em recuperação ou reprovado.

# Aprovado média >=7
# Recuperaão média > 4
# Reprovado média < 4

# Etapas
# 1) Solicitar as notas ao usuário
# 2) Calcular a média
# 3) Checar a condição do aluno
# 4) Informar o resultado



# 1
n1 = float(input("Qual sua nota do 1° Bim"))
n2 = float(input("Qual sua nota do 2° Bim"))
n3 = float(input("Qual sua nota do 3° Bim"))
# 2
media = (n1 + n2 + n3)/3
# 3 e 4
if media >= 7:
    print(f"O Aluno tem média {media:.2f} e está aprovado")
elif media > 4:
       print(f"O Aluno tem média {media:.2f} e está em recuperação") 
else:
      print(f"O Aluno tem média {media:.2f} e está reprovado")      
