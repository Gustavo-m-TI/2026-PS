# ===================================================
# SISTEMA DE CADASTRO PARA EVENTO
# ---------------------------------------------------
# Disciplina : Programação de Sistemas (PS)
# Autores    : [Gustavo Maciel da Silva, Alcides Diniz Veiga, Artur Lacerda da Silva]
# Data       : [03/03/2026]
# Repositório: https://github.com/[Gustavo-m-TI]/2026-PS
# ===================================================
#
# DESCRIÇÃO:
# É um sistema de cadastro de evento contendo cadastro e login
# de usuarios, ele também mostra os detalhes do evento para usuarios logados 
# e mostra uma lista de todo usuario cadastrado, ele le esses cadastros do aquivo txt
# e os salva no mesmo arquivo. Ele valida e-mail, nome, data de nascimento, senha e tipo do ingresso.
# ===================================================

import json
import random
import re
import os

# Arquivo onde os dados serão salvos
ARQUIVO = os.path.join(os.path.dirname(__file__), "dados.txt")
SEPARADOR = "|"

# Lista de eventos
eventos = [
    "14 de novembro: Gusttavo Lima",
    "15 de novembro: Desfile de blocos com banda e DJ",
    "19 de novembro: Hugo e Guilherme",
    "20 de novembro: Jota Quest + baile + infantil",
    "21 de novembro: Matuê",
    "22 de novembro: Daniel",
    "28 de novembro: Gustavo Mioto",
    "29 de novembro: Chitãozinho e Xororó"
]

# Carregar dados do arquivo
def carregar_cadastros():
    if os.path.exists(ARQUIVO):
        try:
            with open(ARQUIVO, "r", encoding="utf-8") as f:
                usuarios_carregados = []
                for linha in f:
                    if linha.strip():
                        partes = linha.strip().split(SEPARADOR)
                        if len(partes) >= 5:
                            usuarios_carregados.append({
                                "nome": partes[0],
                                "nascimento": partes[1],
                                "email": partes[2],
                                "senha": partes[3],
                                "ingresso": partes[4]
                            })
                return usuarios_carregados
        except Exception as e:
            print(f"Erro ao carregar: {e}")
            return []
    return []

usuarios = carregar_cadastros()

# Funções de validação
def validar_nome(nome):
    return bool(re.fullmatch(r"[A-Za-zÀ-ÿ ]+", nome.strip()))

def validar_data(data):
    return bool(re.fullmatch(r"\d{2}/\d{2}/\d{4}", data.strip()))

def validar_email(email):
    return bool(re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email.strip()))

def validar_senha(senha):
    return len(senha.strip()) > 0

def salvar_cadastro(lista_usuarios=None):
    """Grava toda a lista no arquivo .txt."""
    if lista_usuarios is None:
        lista_usuarios = usuarios
    try:
        # 'w' = write: cria se não existir, subscreve se existir
        with open(ARQUIVO, 'w', encoding="utf-8") as f:
            for cadastro in lista_usuarios:
                linha = f"{cadastro['nome']}{SEPARADOR}{cadastro['nascimento']}{SEPARADOR}{cadastro['email']}{SEPARADOR}{cadastro['senha']}{SEPARADOR}{cadastro['ingresso']}\n"
                f.write(linha)
    except IOError as e:
        #IOError: disco cheio, permissão negada, etc.
        print(f"❌ Erro ao salvar: {e}")

# Cadastro
def cadastrar():
    while True:
        nome = input("Nome completo: ")
        if validar_nome(nome):
            break
        print("Nome inválido!")

    while True:
        nascimento = input("Data de nascimento (dd/mm/aaaa): ")
        if validar_data(nascimento):
            break
        print("Data inválida!")

    while True:
        email = input("Email: ")
        if not validar_email(email):
            print("Email inválido!")
            continue
        # Verifica duplicado
        if any(u["email"] == email for u in usuarios):
            print("Email já cadastrado!")
            continue
        break

    while True:
        senha = input("Senha: ")
        if validar_senha(senha):
            break
        print("Senha não pode estar vazia!")

    while True:
        print("Tipo de ingresso:")
        print("1 - Comum")
        print("2 - VIP")
        print("3 - Estudante")
        opcao = input("Escolha: ")
        if opcao in ["1","2","3"]:
            break
        print("Opção inválida!")
    ingresso = {"1":"Comum","2":"VIP","3":"Estudante"}[opcao]

    usuario = {
        "nome": nome,
        "nascimento": nascimento,
        "email": email,
        "senha": senha,
        "ingresso": ingresso
    }

    usuarios.append(usuario)
    salvar_cadastro(usuarios)
    print("Cadastro realizado e salvo!\n")

# Login
def login():
    email = input("Email: ")
    senha = input("Senha: ")

    for u in usuarios:
        if u["email"] == email and u["senha"] == senha:
            print(f"\nBem-vindo, {u['nome']}!")
            print(f"Ingresso: {u['ingresso']}")

            # Escolhe evento aleatório
            evento = random.choice(eventos)
            hora = random.randint(18,23)

            # Salva o evento no usuário
            u["evento"] = evento
            u["local"] = "Centro de Eventos"
            u["horario"] = f"{hora}:00"
            salvar_cadastro(usuarios)

            print("\n--- DETALHES DO EVENTO ---")
            print(f"Evento: {evento}")
            print(f"Local: Centro de Eventos")
            print(f"Horário: {hora}:00\n")
            return

    print("Login inválido!\n")

# Mostrar todos usuários
def mostrar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado!\n")
        return
    print("\n--- TODOS OS USUÁRIOS ---")
    for u in usuarios:
        print(f"Nome: {u['nome']}, Email: {u['email']}, Ingresso: {u['ingresso']}")
        if "evento" in u:
            print(f"Evento: {u['evento']}, Local: {u['local']}, Horário: {u['horario']}")
        print("-------------------------")
    print()

# Menu
while True:
    print("1 - Cadastrar")
    print("2 - Login")
    print("3 - Mostrar usuários")
    print("4 - Sair")
    opcao = input("Escolha: ")

    if opcao=="1":
        cadastrar()
    elif opcao=="2":
        login()
    elif opcao=="3":
        mostrar_usuarios()
    elif opcao=="4":
        break
    else:
        print("Opção inválida!\n")