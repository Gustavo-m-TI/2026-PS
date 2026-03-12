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
# Este programa funciona como um estoque de produtos,
# ele contém três produtos pré cadastrados e xibe a quantidade
# 
# ===================================================

# --- Base de Dados dos Produtos ---
# Lista dos produtos armazenandos em uma biblioteca, armazenando nome e quantidade
produtos = [
    {"nome": "Teclado", "quantidade": 3},
    {"nome": "Chiclete", "quantidade": 15},
    {"nome": "Monster", "quantidade": 25},
    {"nome": "Café", "quantidade": 8}
]

# Contadores dos estados de estoque dos produtos
critico = 0
adequado = 0
excesso = 0

print("=" * 52)
print("-" *15, "RELATÓRIO DE ESTOQUE", "-" *15)
print("=" * 52)

# --- Processamento das quantidades e Relatório ---
# Usa laço for para percorrer a lista usando if/elif/else para a situação
for i in produtos:
    nome = i["nome"]
    qtd = i["quantidade"]
    
    if qtd < 5:
        situacao = "Crítico"
        critico += 1
    elif 5 <= qtd <= 20:
        situacao = "Adequado"
        adequado += 1
    else:
        situacao = "Excesso"
        excesso += 1
        
    print(f"Produto: {nome:<12} | Qtd: {qtd:>2} | Situação: {situacao}")

# --- Resumo Geral ---
print("=" * 52)
print(f"RESUMO: Crítico: {critico} | Adequado: {adequado} | Excesso: {excesso}")
print("=" * 52)

# --- Busca Interativa ---
# Usa laço while para permitir consultas sobre produtos específicos
while True:
    opcao = input("\nDeseja consultar um produto específico? (s/n): ").lower()
    
    if opcao != 's':
        print("Obrigado por utilizar o sistema de estoque!")
        break
        
    busca = input("Digite o nome do produto: ").strip().lower()
    encontrado = False
    
    for i in produtos:
        if i["nome"].lower() == busca:
            print(f"-> Resultado da Busca: {i['nome']} possui {i['quantidade']} unidades em estoque.")
            encontrado = True
            break
    
    if not encontrado:
        print("-> Erro: Produto não encontrado, tente novamente.")
