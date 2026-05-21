# ===================================================
# SISTEMA DE ESTOQUE INTERATIVO
# ===================================================
# Disciplina : Programação de Sistemas (PS)
# Aula       : 04 – Revisão: Variáveis, Tipos e Controle de Fluxo
# Autor      : [Gustavo Maciel da Silva]
# Data       : [10.03.2026]
# Repositório: https://github.com/[Gustavo-m-TI]/2026-PS
# ===================================================
#
# DESCRIÇÃO:
# Este programa gerencia um estoque de produtos em um menu
# interativo. O usuário pode listar produtos, cadastrar novos,
# pesquisar por nome, atualizar quantidades e ver um resumo.
# ===================================================

produtos = [
    {"nome": "Teclado", "quantidade": 3},
    {"nome": "Chiclete", "quantidade": 15},
    {"nome": "Monster", "quantidade": 25},
    {"nome": "Café", "quantidade": 8}
]


def listar_produtos(produtos):
    print("\n" + "=" * 52)
    print("RELATÓRIO DE ESTOQUE")
    print("=" * 52)

    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    for produto in produtos:
        qtd = produto["quantidade"]
        if qtd < 5:
            situacao = "Crítico"
        elif qtd <= 20:
            situacao = "Adequado"
        else:
            situacao = "Excesso"

        print(f"Produto: {produto['nome']:<12} | Qtd: {qtd:>2} | Situação: {situacao}")


def adicionar_produto(produtos):
    print("\n" + "=" * 15 + " CADASTRAR PRODUTO " + "=" * 15)
    nome = input("Nome do produto: ").strip()
    quantidade = input("Quantidade: ").strip()

    if not nome or not quantidade:
        print("⚠️  Nome e quantidade são obrigatórios.")
        return

    if not quantidade.isdigit():
        print("⚠️  Quantidade deve ser um número inteiro.")
        return

    produtos.append({
        "nome": nome,
        "quantidade": int(quantidade)
    })
    print(f"✅ Produto '{nome}' cadastrado com sucesso!")


def buscar_produto(produtos):
    print("\n" + "=" * 15 + " BUSCAR PRODUTO " + "=" * 15)
    termo = input("Digite o nome do produto: ").strip().lower()

    if not termo:
        print("⚠️  Informe um nome para buscar.")
        return

    encontrados = [p for p in produtos if termo in p["nome"].lower()]
    if encontrados:
        for produto in encontrados:
            print(f"- {produto['nome']} possui {produto['quantidade']} unidades.")
    else:
        print("❌ Produto não encontrado.")


def atualizar_quantidade(produtos):
    print("\n" + "=" * 15 + " ATUALIZAR QUANTIDADE " + "=" * 15)
    nome = input("Digite o nome do produto: ").strip().lower()

    if not nome:
        print("⚠️  Informe um nome para atualizar.")
        return

    for produto in produtos:
        if produto["nome"].lower() == nome:
            nova_qtd = input(f"Nova quantidade de '{produto['nome']}': ").strip()
            if not nova_qtd.isdigit():
                print("⚠️  Quantidade deve ser um número inteiro.")
                return
            produto["quantidade"] = int(nova_qtd)
            print(f"✅ Quantidade de '{produto['nome']}' atualizada para {produto['quantidade']}. ")
            return

    print("❌ Produto não encontrado.")


def relatorio_final(produtos):
    total = len(produtos)
    critico = sum(1 for p in produtos if p["quantidade"] < 5)
    adequado = sum(1 for p in produtos if 5 <= p["quantidade"] <= 20)
    excesso = sum(1 for p in produtos if p["quantidade"] > 20)

    print("\n" + "=" * 52)
    print("RESUMO GERAL DO ESTOQUE")
    print("=" * 52)
    print(f"Total de produtos: {total}")
    print(f"Crítico: {critico}")
    print(f"Adequado: {adequado}")
    print(f"Excesso: {excesso}")


def menu():
    while True:
        print("\n" + "=" * 40)
        print("SISTEMA DE ESTOQUE INTERATIVO")
        print("=" * 40)
        print("1 - Listar produtos")
        print("2 - Cadastrar produto")
        print("3 - Buscar produto")
        print("4 - Atualizar quantidade")
        print("5 - Relatório final")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            listar_produtos(produtos)
        elif opcao == "2":
            adicionar_produto(produtos)
        elif opcao == "3":
            buscar_produto(produtos)
        elif opcao == "4":
            atualizar_quantidade(produtos)
        elif opcao == "5":
            relatorio_final(produtos)
        elif opcao == "0":
            print("\nObrigado por utilizar o sistema!")
            break
        else:
            print("⚠️  Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
