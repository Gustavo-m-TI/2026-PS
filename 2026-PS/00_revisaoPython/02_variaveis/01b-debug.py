# Arquivo: 01b-debug.py
# ATENÇÃO: Este código contém 4 erros propositais. Encontre e corrija todos!

nome = input("Digite o nome do aluno: ")
#erro no input, estava escrito com "m" ao inves de "n"
nota1 = float(input("Digite a nota 1: "))
# mudado notal para nota1, para manter o padrão da nota2
nota2 = float(input("Digite a nota 2: "))

media = (nota1 + nota2) / 2
#adicionado parenteses para que seja feito a soma antes da divisão

if media >= 6.0:
    situacao = "Aprovado"
elif media >= 4.0:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

print(f"Aluno: {nome} | Média: {media:.2f} | Situação: {situacao}")
# erro no print, estava escrito"pront" ao inves de "print"
