# ==================================================
# SISTEMA DE BIBLIOTECA
# ==================================================
# Disciplina : Programação de Sistemas (PS)
# Aula       : 05 - Revisão: Estruturas de dados
# Autor      : [Gustavo Maciel da Silva]
# Data       : [12.03.2026]
# Repositório: https://github.com/[Gustavo-m-TI]/2026-PS
# ===================================================
#
# DESCRIÇÃO:
# Catálogo de livros, que mostra ano, autor, título e
# se está disponível ou não. O sistema permite adicionar
# novos livros, pesquisar por autor, alterar status e
# exibir um relatório final.
#====================================================

catalogo = [
    {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1899, "disponivel": True},
    {"titulo": "1984", "autor": "George Orwell", "ano": 1949, "disponivel": False},
    {"titulo": "O Hobbit", "autor": "J.R.R. Tolkien", "ano": 1937, "disponivel": True}
]


def listar_catalogo(catalogo):
    print("\n" + "=" * 50)
    print(" 📚 CATÁLOGO DA BIBLIOTECA")
    print("=" * 50)

    if not catalogo:
        print("Nenhum livro cadastrado.")
        return

    for i, livro in enumerate(catalogo, 1):
        status = "Disponível" if livro["disponivel"] else "Emprestado"
        print(f"{i}. {livro['titulo']} ({livro['autor']}, {livro['ano']}) | Status: {status}")


def adicionar_livro(catalogo):
    print("\n" + "=" * 15 + " ADICIONAR LIVRO " + "=" * 15)
    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()
    ano = input("Ano: ").strip()

    if not titulo or not autor or not ano:
        print("⚠️  Todos os campos são obrigatórios.")
        return

    if not ano.isdigit():
        print("⚠️  Ano deve ser um número inteiro.")
        return

    catalogo.append({
        "titulo": titulo,
        "autor": autor,
        "ano": int(ano),
        "disponivel": True
    })
    print(f"✅ Livro '{titulo}' adicionado com sucesso!")


def buscar_por_autor(catalogo):
    print("\n" + "=" * 15 + " BUSCA POR AUTOR " + "=" * 15)
    autor_busca = input("Digite o nome do autor: ").strip().lower()

    if not autor_busca:
        print("⚠️  Informe um autor para buscar.")
        return

    encontrados = [l for l in catalogo if autor_busca in l["autor"].lower()]
    if encontrados:
        print(f"\n{len(encontrados)} resultado(s) encontrado(s):")
        for livro in encontrados:
            status = "Disponível" if livro["disponivel"] else "Emprestado"
            print(f"- {livro['titulo']} ({livro['ano']}) | {status}")
    else:
        print("Nenhum livro encontrado para este autor.")


def alterar_status(catalogo):
    print("\n" + "=" * 15 + " EMPRÉSTIMO / DEVOLUÇÃO " + "=" * 15)
    titulo_busca = input("Digite o título exato do livro: ").strip().lower()

    if not titulo_busca:
        print("⚠️  Informe o título do livro.")
        return

    for livro in catalogo:
        if livro["titulo"].lower() == titulo_busca:
            livro["disponivel"] = not livro["disponivel"]
            novo_status = "Disponível" if livro["disponivel"] else "Emprestado"
            print(f"✅ O status de '{livro['titulo']}' agora é: {novo_status}")
            return

    print("❌ Título não encontrado no sistema.")


def relatorio_final(catalogo):
    print("\n" + "=" * 30)
    print("RELATÓRIO FINAL DA BIBLIOTECA")
    print("=" * 30)

    total = len(catalogo)
    disponiveis = sum(1 for livro in catalogo if livro["disponivel"])
    emprestados = total - disponiveis
    lista_emprestados = [livro["titulo"] for livro in catalogo if not livro["disponivel"]]

    print(f"Total de livros: {total}")
    print(f"Disponíveis: {disponiveis}")
    print(f"Emprestados: {emprestados}")
    if lista_emprestados:
        print(f"Títulos atualmente emprestados: {', '.join(lista_emprestados)}")


def menu(catalogo):
    while True:
        print("\n" + "=" * 40)
        print("📚 SISTEMA DE BIBLIOTECA")
        print("=" * 40)
        print("1 - Listar livros")
        print("2 - Adicionar livro")
        print("3 - Buscar por autor")
        print("4 - Empréstimo / Devolução")
        print("5 - Relatório final")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            listar_catalogo(catalogo)
        elif opcao == "2":
            adicionar_livro(catalogo)
        elif opcao == "3":
            buscar_por_autor(catalogo)
        elif opcao == "4":
            alterar_status(catalogo)
        elif opcao == "5":
            relatorio_final(catalogo)
        elif opcao == "0":
            print("\nAté logo! 👋")
            break
        else:
            print("⚠️  Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu(catalogo)
