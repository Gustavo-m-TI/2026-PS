import random
import re
import os

ARQUIVO = os.path.join(os.path.dirname(__file__), "dados.txt")
SEPARADOR = "|"

tipos_consulta = [
    "Clínico Geral",
    "Odontologia",
    "Psicologia",
    "Pediatria",
    "Cardiologia"
]

# ------------------ CARREGAR ------------------
def carregar_cadastros():
    if os.path.exists(ARQUIVO):
        try:
            with open(ARQUIVO, "r", encoding="utf-8") as f:
                lista = []
                for linha in f:
                    partes = linha.strip().split(SEPARADOR)
                    if len(partes) >= 7:
                        lista.append({
                            "nome": partes[0],
                            "nascimento": partes[1],
                            "email": partes[2],
                            "senha": partes[3],
                            "consulta": partes[4],
                            "data": partes[5],
                            "hora": partes[6]
                        })
                return lista
        except:
            return []
    return []

usuarios = carregar_cadastros()

# ------------------ SALVAR ------------------
def salvar():
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        for u in usuarios:
            linha = f"{u['nome']}{SEPARADOR}{u['nascimento']}{SEPARADOR}{u['email']}{SEPARADOR}{u['senha']}{SEPARADOR}{u['consulta']}{SEPARADOR}{u['data']}{SEPARADOR}{u['hora']}\n"
            f.write(linha)

# ------------------ VALIDAÇÕES ------------------
def validar_nome(nome):
    return bool(re.fullmatch(r"[A-Za-zÀ-ÿ ]+", nome.strip()))

def validar_data(data):
    return bool(re.fullmatch(r"\d{2}/\d{2}/\d{4}", data.strip()))

def validar_email(email):
    return bool(re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email.strip()))

def validar_senha(senha):
    return len(senha.strip()) > 0

# ------------------ CADASTRO ------------------
def cadastrar():
    while True:
        nome = input("Nome: ")
        if validar_nome(nome):
            break
        print("Nome inválido!")

    while True:
        nascimento = input("Nascimento (dd/mm/aaaa): ")
        if validar_data(nascimento):
            break
        print("Data inválida!")

    while True:
        email = input("Email: ")
        if not validar_email(email):
            print("Email inválido!")
            continue
        if any(u["email"] == email for u in usuarios):
            print("Email já existe!")
            continue
        break

    while True:
        senha = input("Senha: ")
        if validar_senha(senha):
            break
        print("Senha inválida!")

    usuario = {
        "nome": nome,
        "nascimento": nascimento,
        "email": email,
        "senha": senha,
        "consulta": "",
        "data": "",
        "hora": ""
    }

    usuarios.append(usuario)
    salvar()
    print("Conta criada!\n")

# ------------------ GERAR DATA/HORA ------------------
def gerar_data_hora():
    dia = random.randint(1, 28)
    mes = random.randint(4, 12)
    ano = 2026
    hora = random.randint(8, 17)

    data = f"{dia:02d}/{mes:02d}/{ano}"
    hora_str = f"{hora}:00"

    return data, hora_str

# ------------------ MENU DO USUÁRIO ------------------
def menu_usuario(u):
    while True:
        print("\n--- MENU ---")
        print("1 - Marcar consulta")
        print("2 - Ver consulta")
        print("3 - Logout")

        op = input("Escolha: ")

        # MARCAR CONSULTA
        if op == "1":
            print("\nTipos de consulta:")
            for i, tipo in enumerate(tipos_consulta, 1):
                print(f"{i} - {tipo}")

            escolha = input("Escolha: ")

            if escolha.isdigit() and 1 <= int(escolha) <= len(tipos_consulta):
                u["consulta"] = tipos_consulta[int(escolha)-1]
                u["data"], u["hora"] = gerar_data_hora()
                salvar()
                print("Consulta marcada com sucesso!")
            else:
                print("Opção inválida!")

        # VER CONSULTA
        elif op == "2":
            if u["consulta"] == "":
                print("Nenhuma consulta marcada!")
            else:
                print("\n--- SUA CONSULTA ---")
                print(f"Tipo: {u['consulta']}")

                if u['consulta'] == "Clínico Geral":
                    local = "Postinho"
                else:
                    local = "Clínica Central"

                print(f"Local: {local}")
                print(f"Data: {u['data']}")
                print(f"Hora: {u['hora']}")

        elif op == "3":
            break
        else:
            print("Opção inválida!")

# ------------------ LOGIN ------------------
def login():
    email = input("Email: ")
    senha = input("Senha: ")

    for u in usuarios:
        if u["email"] == email and u["senha"] == senha:
            print(f"\nBem-vindo, {u['nome']}!")
            menu_usuario(u)
            return

    print("Login inválido!\n")

# ------------------ MOSTRAR ------------------
def mostrar_usuarios():
    for u in usuarios:
        print(f"{u['nome']} - {u['email']} - {u['consulta']}")

# ------------------ MENU PRINCIPAL ------------------
while True:
    print("\n==== SISTEMA ====")
    print("1 - Cadastrar")
    print("2 - Login")
    print("3 - Mostrar usuários")
    print("4 - Sair")

    op = input("Escolha: ")

    if op == "1":
        cadastrar()
    elif op == "2":
        login()
    elif op == "3":
        mostrar_usuarios()
    elif op == "4":
        break
    else:
        print("Opção inválida!")