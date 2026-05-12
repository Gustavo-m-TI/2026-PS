"""
agenda.py — Aula 23 (Programação de Sistemas, 2026)

Agenda de Contatos: classe inicial.
"""

import pickle
caminho="2026-PS/02_poo/agenda/agenda.txt"

class Contato:
    """Representa um contato simples na agenda."""

    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def exibir(self):
        print(f" Nome : {self.nome}")
        print(f" Telefone: {self.telefone}")
        print(f" Email : {self.email}")


# Teste rápido da classe
if __name__ == "__main__":
    c1 = Contato("Little Neguinha", "42 67642-6967", "ellis@gmail.com")
    c1.exibir()

def menu():
    contatos = carregar_de_txt(caminho)
    while True:
        print("\n========= AGENDA =========")
        print("1 - Cadastrar contato")
        print("2 - Listar contatos")
        print("3 - Remover contato")
        print("4 - Salvar em .txt")
        print("5 - Salvar em binário")
        print("0 - Sair")
        opcao = input("Opção: ")

        if opcao == "1":
            cadastrar(contatos)
        elif opcao == "2":
            listar(contatos)
        elif opcao == "3":
            remover(contatos)
        elif opcao == "4":
            salvar_em_txt(contatos, caminho)
        elif opcao == "5":
            salvar_em_binario(contatos, "agenda.bin")

        elif opcao == "0":
            print("Até logo!")
            break
        else:
            print("Opção inválida.")


def cadastrar(contatos):
    print("\n--- Novo contato ---")
    nome = input("Nome : ")
    telefone = input("Telefone: ")
    email = input("Email : ")
    contatos.append(Contato(nome, telefone, email))
    print("√ Contato cadastrado.")


def listar(contatos):
    if not contatos:
        print("\n(agenda vazia)")
        return

    print(f"\n--- Agenda ({len(contatos)} contatos) ---")
    for i, c in enumerate(contatos, start=1):
        print(f"\n[{i}]")
        c.exibir()


def remover(contatos):
    listar(contatos)
    if not contatos:
        return

    indice = int(input("\nNº do contato a remover: ")) - 1

    if 0 <= indice < len(contatos):
        removido = contatos.pop(indice)
        print(f"√ Contato '{removido.nome}' removido.")
    else:
        print("Índice inválido.")

def salvar_em_txt(contatos, caminho):
    with open(caminho, "w", encoding="utf-8") as arquivo:
        for c in contatos:
            arquivo.write(f"{c.nome};{c.telefone};{c.email}\n")
    print(f"√ {len(contatos)} contato(s) salvo(s) em {caminho}")    

def carregar_de_txt(caminho):
    contatos = []
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if not linha:
                    continue
                partes = linha.split(";")
                nome, telefone, email = partes[0], partes[1], partes[2]
                contatos.append(Contato(nome, telefone, email))
    except FileNotFoundError:
        print(f"Arquivo '{caminho}' ainda não existe. Começando vazio.")
    return contatos 

def salvar_em_binario(contatos, caminho):
    with open(caminho, "wb") as arquivo:
        pickle.dump(contatos, arquivo)
    print(f"√ {len(contatos)} contato(s) salvo(s) em {caminho}")

def carregar_de_binario(caminho):
    try:
        with open(caminho, "rb") as arquivo:
            return pickle.load(arquivo)
    except FileNotFoundError:
        print(f"Arquivo '{caminho}' ainda não existe. Começando vazio.")
        return []
    
if __name__ == "__main__":
    menu()