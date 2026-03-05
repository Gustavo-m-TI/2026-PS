# ===================================================
# SISTEMA DE CÁLCULO DE NOTAS E SITUAÇÃO ACADÊMICA
# ---------------------------------------------------
# Disciplina : Programação de Sistemas (PS)
# Aula       : 06 - Revisão: Funções (Nível Básico + Intermediário)
# Autor      : [SEU NOME AQUI]
# Data       : [DATA DE HOJE]
# Repositório: https://github.com/[SEU-USUARIO]/2026-PS
# ===================================================
#
# DESCRIÇÃO:
# Calcula a média de notas de alunos e verifica sua
# situação acadêmica conforme critérios IFPR.
# Processa múltiplos alunos com validação de entrada.
# ===================================================

# ---- NÍVEL BÁSICO ----

def calcular_media(nota1, nota2):
    """Calcula e retorna a média aritmética de duas notas."""
    media = (nota1 + nota2) / 2
    return media

def verificar_situacao(media):
    """Verifica e retorna a situação do aluno com base na média.
    
    Critérios IFPR:
    ≥ 6.0  → Aprovado
    4.0 até 5.9 → Recuperação
    < 4.0 → Reprovado
    """
    if media >= 6.0:
        return "Aprovado"
    elif media >= 4.0:
        return "Recuperação"
    else:
        return "Reprovado"

# ---- NÍVEL INTERMEDIÁRIO ----

def solicitar_notas(nome_aluno):
    """Solicita e valida as notas de um aluno (0-10).
    
    Retorna uma tupla com as duas notas validadas.
    """
    print(f"\n--- Notas de {nome_aluno} ---")
    
    # Valida primeira nota
    while True:
        try:
            nota1 = float(input(f"Nota 1 (0-10): "))
            if 0 <= nota1 <= 10:
                break
            else:
                print("❌ Nota deve estar entre 0 e 10!")
        except ValueError:
            print("❌ Digite um número válido!")
    
    # Valida segunda nota
    while True:
        try:
            nota2 = float(input(f"Nota 2 (0-10): "))
            if 0 <= nota2 <= 10:
                break
            else:
                print("❌ Nota deve estar entre 0 e 10!")
        except ValueError:
            print("❌ Digite um número válido!")
    
    return nota1, nota2

def gerar_relatorio(nome, media, situacao):
    """Exibe um relatório formatado com os dados do aluno.
    
    Recebe como parâmetros o nome, média e situação
    do aluno (sem usar variáveis globais).
    """
    print("\n" + "=" * 50)
    print(f"📋 RESULTADO - {nome.upper()}")
    print("=" * 50)
    print(f"  Média        : {media:.2f}")
    print(f"  Situação     : {situacao}")
    
    # Emoji de status
    if situacao == "Aprovado":
        emoji = "✅"
    elif situacao == "Recuperação":
        emoji = "⚠️"
    else:
        emoji = "❌"
    
    print(f"  Status       : {emoji}")
    print("=" * 50)

def processar_aluno(nome_aluno):
    """Processa um aluno: solicita notas, calcula média e exibe relatório."""
    nota1, nota2 = solicitar_notas(nome_aluno)
    media = calcular_media(nota1, nota2)
    situacao = verificar_situacao(media)
    gerar_relatorio(nome_aluno, media, situacao)

# ---- EXECUÇÃO PRINCIPAL ----

if __name__ == "__main__":
    print("=" * 50)
    print("  SISTEMA DE CÁLCULO DE NOTAS - IFPR")
    print("=" * 50)
    
    # Lista de alunos a processar
    alunos = ["Ana Silva", "Bruno Costa", "Carlos Santos"]
    
    # Processa cada aluno
    for aluno in alunos:
        processar_aluno(aluno)
    
    print("\n✅ Processamento concluído!")
