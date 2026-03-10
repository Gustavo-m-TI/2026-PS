# ===================================================
#
# SISTEMA DE AVALIAÇÃO DE ALUNOS
#
# ===================================================
#
# Disciplina : Programação de Sistemas (PS)
#
# Aula       : 04 — Funções
#
# Autor      : [Gustavo Maciel da Silva]
#
# Data       : [05.03.2026]
#
# Repositório: https://github.com/[Gustavo-m-TI]/2026-PS
#
# Descrição  : Sistema que calcula média e classifica alunos según critérios IFPR
#              NÍVEL INTERMEDIÁRIO (Conceito B)
#
# ===================================================

# ---- BLOCO 1: FUNÇÕES - NÍVEL BÁSICO ----

def calcular_media(nota1, nota2):
    """
    Calcula a média aritmética de duas notas.
    
    Args:
        nota1 (float): Primeira nota do aluno
        nota2 (float): Segunda nota do aluno
    
    Returns:
        float: A média das duas notas
    """
    return (nota1 + nota2) / 2


def verificar_situacao(media):
    """
    Classifica o aluno conforme sua média.
    
    Critérios IFPR:
    - Aprovado: média ≥ 6.0
    - Recuperação: 4.0 ≤ média < 6.0
    - Reprovado: média < 4.0
    
    Args:
        media (float): A média do aluno
    
    Returns:
        str: A situação do aluno
    """
    if media >= 6.0:
        return "Aprovado"
    elif media >= 4.0:
        return "Recuperação"
    else:
        return "Reprovado"


# ---- BLOCO 2: FUNÇÕES - NÍVEL INTERMEDIÁRIO ----

def solicitar_notas(nome_aluno):
    """
    Solicita e valida as notas do aluno.
    Só aceita notas entre 0 e 10.
    
    Args:
        nome_aluno (str): Nome do aluno
    
    Returns:
        tuple: Uma tupla contendo (nota1, nota2) validadas
    """
    while True:
        try:
            nota1 = float(input(f"  {nome_aluno} - 1ª nota (0-10): "))
            if not (0 <= nota1 <= 10):
                print("  ❌ Erro: A nota deve estar entre 0 e 10!")
                continue
            
            nota2 = float(input(f"  {nome_aluno} - 2ª nota (0-10): "))
            if not (0 <= nota2 <= 10):
                print("  ❌ Erro: A nota deve estar entre 0 e 10!")
                continue
            
            return nota1, nota2
        
        except ValueError:
            print("  ❌ Erro: Digite um número válido!")


def gerar_relatorio(nome, media, situacao):
    """
    Exibe o resultado formatado de forma clara.
    
    Args:
        nome (str): Nome do aluno
        media (float): Média do aluno
        situacao (str): Situação do aluno (Aprovado/Recuperação/Reprovado)
    """
    linha = "─" * 50
    print(f"\n{linha}")
    print(f" ALUNO(A): {nome.upper()}")
    print(f" MÉDIA: {media:.2f}")
    print(f" SITUAÇÃO: {situacao}")
    print(f"{linha}\n")


# ---- BLOCO 3: PROGRAMA PRINCIPAL ----

def main():
    """Função principal que executa o programa."""
    
    # Exibir cabeçalho
    linha_sep = "=" * 50
    print(f"\n{linha_sep}")
    print(" SISTEMA DE AVALIAÇÃO DE ALUNOS - NÍVEL INTERMEDIÁRIO")
    print(f"{linha_sep}\n")
    
    # Lista de alunos a processar
    nomes_alunos = [
        "João Silva",
        "Maria Santos",
        "Pedro Oliveira"
    ]
    
    # Processar cada aluno
    for nome in nomes_alunos:
        # Solicitar notas validadas
        nota1, nota2 = solicitar_notas(nome)
        
        # Calcular média
        media = calcular_media(nota1, nota2)
        
        # Verificar situação
        situacao = verificar_situacao(media)
        
        # Gerar relatório
        gerar_relatorio(nome, media, situacao)
    
    print(f"{linha_sep}")
    print(" Avaliação de todos os alunos concluída!")
    print(f"{linha_sep}\n")


# ---- BLOCO 4: EXECUÇÃO ----

if __name__ == "__main__":
    main()
