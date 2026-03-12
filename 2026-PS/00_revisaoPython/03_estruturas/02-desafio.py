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
# Catálogo de livros, que mostra ano, autor, titulo e
# se esta disponivel ou não, também deve poder adicionar
# novos livros, pesquisar por autor e mostrar os disponiveis no final.
#====================================================

# Lista dos livros salvos na biblioteca, onde salva nome, autor, ano e se esta disponivel
catalogo = [
    {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1899, "disponivel": True},
    {"titulo": "1984", "autor": "George Orwell", "ano": 1949, "disponivel": False},
    {"titulo": "O Hobbit", "autor": "J.R.R. Tolkien", "ano": 1937, "disponivel": True}
]

# --- CADASTRO DE NOVO LIVRO ---
print("=" *49)
print("-" *15, "CADASTRO DE LIVRO", "-" *15)
print("=" *49)
novo_titulo = input("Título: ")
novo_autor = input("Autor: ")
novo_ano = int(input("Ano: "))

# Adicionando o novo livro com o status de diponível
catalogo.append({
    "titulo": novo_titulo, 
    "autor": novo_autor, 
    "ano": novo_ano, 
    "disponivel": True
})

# --- EXIBIÇÃO E BUSCA POR AUTOR ---
print("\n" + "=" *48)
print(f"-------- CATÁLOGO ATUALIZADO ({len(catalogo)} livros) --------")
print("=" *48)
for livro in catalogo:
    status = "Disponível" if livro["disponivel"] else "Emprestado"
    print(f"- {livro['titulo']} ({livro['autor']}, {livro['ano']}) | Status: {status}")

print("\n" + "=" *35)
print("--------- BUSCA POR AUTOR ---------")
print("=" *35)
busca_autor = input("Digite o nome do autor para buscar: ").strip().lower()
encontrados = [l for l in catalogo if busca_autor in l["autor"].lower()]

if encontrados:
    for l in encontrados:
        print(f"Encontrado: {l['titulo']} - {l['autor']}")
else:
    print("Nenhum livro encontrado para este autor.")

# --- 4. SISTEMA DE EMPRÉSTIMO / DEVOLUÇÃO ---
print("\n" + "="*46)
print("------ REGISTRO DE EMPRÉSTIMO/DEVOLUÇÃO ------")
print("="*46)
titulo_busca = input("Digite o título exato do livro para alterar o status: ").strip().lower()
livro_localizado = False

for livro in catalogo:
    if livro["titulo"].lower() == titulo_busca:
        # Inverte o status: True vira False, False vira True
        livro["disponivel"] = not livro["disponivel"]
        novo_status = "Disponível" if livro["disponivel"] else "Emprestado"
        print(f"Sucesso! O status de '{livro['titulo']}' agora é: {novo_status}")
        livro_localizado = True
        break

if not livro_localizado:
    print("Erro: Título não encontrado no sistema.")

# --- RELATÓRIO FINAL ---
print("\n" + "="*30)
print("RELATÓRIO FINAL DA BIBLIOTECA")
print("="*30)

total = len(catalogo)
disponiveis = sum(1 for l in catalogo if l["disponivel"])
emprestados = total - disponiveis
lista_emprestados = [l["titulo"] for l in catalogo if not l["disponivel"]]

print(f"Total de livros: {total}")
print(f"Disponíveis: {disponiveis}")
print(f"Emprestados: {emprestados}")
if lista_emprestados:
    print(f"Títulos Atualmente Emprestados: {', '.join(lista_emprestados)}")
print("="*30)
