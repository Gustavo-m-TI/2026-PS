# ===================================================
# SISTEMA DE APROVAÇÃO DE ALUNOS
# ===================================================
# Disciplina : Programação de Sistemas (PS)
# Aula       : 04 – Revisão: Variáveis, Tipos e Controle de Fluxo
# Autor      : [Gustavo Maciel da Silva]
# Data       : [10.03.2026]
# Repositório: https://github.com/[Gustavo-m-TI]/2026-PS
# ===================================================
#
# DESCRIÇÃO:
# Este programa processa as notas de uma turma e determina
# a situação de cada aluno (Aprovado, Recuperação ou Reprovado).
# Conceitos utilizados: variáveis, tipos de dados, operadores,
# estruturas de seleção e estruturas de repetição.
# ===================================================

# ---- DADOS DA TURMA ----
# Uma lista de dicionários: cada dicionário representa um aluno

turma = [
    {"nome": "Ana",   "nota1": 8.0, "nota2": 7.5},
    {"nome": "Bruno", "nota1": 4.5, "nota2": 5.0},
    {"nome": "Carla", "nota1": 2.0, "nota2": 3.5},
    {"nome": "Atila", "nota1": 2.3, "nota2": 0.5},
]

print("=== Resultado da Turma ===")
print()

# O 'for' percorre cada aluno da lista automaticamente
for aluno in turma:
    nome = aluno["nome"]
    nota1 = aluno["nota1"]
    nota2 = aluno["nota2"]
    
    # Cálculo da média simples
    media = (nota1 + nota2) / 2
    
    # Estrutura de decisão para definir a situação
    if media >= 6.0:
        situacao = "✅ Aprovado"
    elif media >= 4.0:
        situacao = "⚠️  Recuperação"
    else:
        situacao = "❌ Reprovado"
        
    # Exibição dos resultados formatados
    print(f"Aluno    : {nome}")
    print(f"Média    : {media:.2f}")
    print(f"Situação : {situacao}")
    print("-" * 30)
