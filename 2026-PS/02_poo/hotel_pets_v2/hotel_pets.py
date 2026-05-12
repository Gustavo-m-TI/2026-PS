'''
================================================================
# ARQUIVO    : hotel_pets.py
# Disciplina : Programação de Sistemas (2026-2)
# Autor      : [Gustavo Maciel da Silva]
# Conceitos  : Classe, objeto, atributos, métodos, encapsulamento, arquivos, persistência
# Atividade: Hotel para pets (versão 2)
================================================================
'''

import pickle
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
caminho = os.path.join(BASE_DIR, "pets.txt")
caminho_bin = os.path.join(BASE_DIR, "pets.bin")


class Pet:

    def __init__(self, nome, especie, idade, peso,
                 nome_dono, vacinado, observacoes):

        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.peso = peso
        self.nome_dono = nome_dono
        self.vacinado = vacinado
        self.observacoes = observacoes

        self.hospedado = False
        self.pagamento = False

    def exibir(self):

        print(f"Nome: {self.nome}")
        print(f"Espécie: {self.especie}")
        print(f"Idade: {self.idade}")
        print(f"Peso: {self.peso} kg")
        print(f"Dono: {self.nome_dono}")
        print(f"Vacinado: {'Sim' if self.vacinado else 'Não'}")
        print(f"Hospedado: {'Sim' if self.hospedado else 'Não'}")
        print(f"Pagamento: {'Pago' if self.pagamento else 'Pendente'}")
        print(f"Observações: {self.observacoes}")

    def calcular_diaria(self):

        if self.idade <= 3:
            return 50.0
        elif self.idade <= 10:
            return 60.0
        elif self.idade <= 15:
            return 70.0
        else:
            return 100.0

    def checkin(self):

        if self.hospedado:
            print(f"{self.nome} já está hospedado.")
        else:
            self.hospedado = True
            print(f"{self.nome} fez check-in.")

    def checkout(self):

        if not self.hospedado:
            print(f"{self.nome} não está hospedado.")
        else:
            self.hospedado = False
            print(f"{self.nome} fez check-out.")

    def pagar(self):

        self.pagamento = True
        valor = self.calcular_diaria()
        print(f"Pagamento de R$ {valor:.2f} realizado.")

    def vacinar(self):

        if self.vacinado:
            print(f"{self.nome} já está vacinado.")
        else:
            self.vacinado = True
            print(f"{self.nome} foi vacinado.")


# ---------------- FUNÇÕES ---------------- #

def cadastrar(pets):

    print("\n=== Cadastro de Pet ===")

    nome = input("Nome: ")
    especie = input("Espécie: ")
    idade = int(input("Idade: "))
    peso = float(input("Peso: "))
    dono = input("Nome do dono: ")
    vacinado = input("Vacinado (s/n): ").lower() == "s"
    obs = input("Observações: ")

    pets.append(Pet(nome, especie, idade, peso, dono, vacinado, obs))

    print("√ Pet cadastrado.")


def listar(pets):

    if not pets:
        print("\nNenhum pet cadastrado.")
        return

    print(f"\n=== PETS ({len(pets)}) ===")

    for i, p in enumerate(pets, start=1):
        print(f"\n[{i}]")
        p.exibir()


def remover(pets):

    listar(pets)

    if not pets:
        return

    i = int(input("\nNúmero do pet: ")) - 1

    if 0 <= i < len(pets):
        removido = pets.pop(i)
        print(f"{removido.nome} removido.")
    else:
        print("Índice inválido.")


def atualizar_peso(pets):

    listar(pets)

    if not pets:
        return

    i = int(input("\nNúmero do pet: ")) - 1

    if 0 <= i < len(pets):

        novo_peso = float(input("Novo peso: "))
        pets[i].peso = novo_peso

        print(f"√ Peso atualizado para {novo_peso} kg")

    else:
        print("Índice inválido.")


def buscar_pet(pets):

    nome_busca = input("\nDigite o nome do pet: ").strip().lower()

    encontrados = []

    for p in pets:
        if nome_busca in p.nome.lower():
            encontrados.append(p)

    if not encontrados:
        print("Nenhum pet encontrado.")
        return

    print(f"\n=== RESULTADOS ({len(encontrados)}) ===")

    for i, p in enumerate(encontrados, start=1):
        print(f"\n[{i}]")
        p.exibir()


def salvar_em_txt(pets, caminho):

    with open(caminho, "w", encoding="utf-8") as f:

        for p in pets:

            f.write(
                f"{p.nome};{p.especie};{p.idade};{p.peso};"
                f"{p.nome_dono};{p.vacinado};{p.observacoes};"
                f"{p.hospedado};{p.pagamento}\n"
            )

    print("√ Salvo em TXT")


def carregar_de_txt(caminho):

    pets = []

    try:
        with open(caminho, "r", encoding="utf-8") as f:

            for linha in f:

                dados = linha.strip().split(";")

                if len(dados) < 9:
                    continue

                pet = Pet(
                    dados[0],
                    dados[1],
                    int(dados[2]),
                    float(dados[3]),
                    dados[4],
                    dados[5] == "True",
                    dados[6]
                )

                pet.hospedado = dados[7] == "True"
                pet.pagamento = dados[8] == "True"

                pets.append(pet)

    except FileNotFoundError:
        print("Arquivo não encontrado. Iniciando vazio.")

    return pets


def salvar_em_binario(pets, caminho):

    with open(caminho, "wb") as f:
        pickle.dump(pets, f)

    print("√ Salvo em BINÁRIO")


def salvar_tudo(pets, caminho_txt, caminho_bin):

    salvar_em_txt(pets, caminho_txt)
    salvar_em_binario(pets, caminho_bin)


def checkin(pets):

    listar(pets)

    i = int(input("\nNúmero do pet: ")) - 1

    if 0 <= i < len(pets):
        pets[i].checkin()


def checkout(pets):

    listar(pets)

    i = int(input("\nNúmero do pet: ")) - 1

    if 0 <= i < len(pets):
        pets[i].checkout()


def vacinar(pets):

    listar(pets)

    i = int(input("\nNúmero do pet: ")) - 1

    if 0 <= i < len(pets):
        pets[i].vacinar()


def pagar(pets):

    listar(pets)

    i = int(input("\nNúmero do pet: ")) - 1

    if 0 <= i < len(pets):
        pets[i].pagar()


# ---------------- MENU ---------------- #

def menu():

    pets = carregar_de_txt(caminho)

    while True:

        print("\n====== HOTEL PET ======")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Check-in")
        print("4 - Check-out")
        print("5 - Vacinar")
        print("6 - Pagar")
        print("7 - Remover")
        print("8 - Atualizar peso")
        print("9 - Buscar pet por nome")
        print("10 - Salvar (TXT + BIN)")
        print("0 - Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            cadastrar(pets)

        elif opcao == "2":
            listar(pets)

        elif opcao == "3":
            checkin(pets)

        elif opcao == "4":
            checkout(pets)

        elif opcao == "5":
            vacinar(pets)

        elif opcao == "6":
            pagar(pets)

        elif opcao == "7":
            remover(pets)

        elif opcao == "8":
            atualizar_peso(pets)

        elif opcao == "9":
            buscar_pet(pets)

        elif opcao == "10":
            salvar_tudo(pets, caminho, caminho_bin)

        elif opcao == "0":
            salvar_tudo(pets, caminho, caminho_bin)
            print("Até logo!")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()