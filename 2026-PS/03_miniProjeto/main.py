# ===================================================
# SISTEMA DE CADASTRO PARA CONSULTA
# ---------------------------------------------------
# Disciplina : Programação de Sistemas (PS)
# Autores    : [Gustavo Maciel da Silva, Alcides Diniz Veiga, Artur Lacerda da Silva]
# Data       : [03/03/2026]
# Repositório: https://github.com/[Gustavo-m-TI]/2026-PS
# ===================================================
#
# DESCRIÇÃO:
# É um sistema de cadastro de consulta contendo cadastro e login
# de usuarios, ele também mostra os detalhes da consulta para usuarios logados 
# e mostra uma lista de todo usuario cadastrado, ele le esses cadastros do aquivo txt
# e os salva no mesmo arquivo. Ele valida e-mail, nome, data de nascimento, senha e tipo da consulta.
# ===================================================

#Explicar o que o sistema faz e suas funcionalidades e também, qual problema ele resolve: facilita o processo de agendamento de consultas

import random
import re
import os
from datetime import date, datetime

# Não existem operadores lógicos nesse código, ja que o sistema só necessita de variaveis do tipo de string

# Mostrar que no código não existe nada escrito fora de alguma função, somente a chamada do menu principal 

# Aponte a função que le o arquivo ao iniciar e explique o que acontece quando o arquivo ainda não existe: A função carregar_cadastros() é chamada ao iniciar o programa e lê os dados do arquivo "dados.txt". Quando o arquivo ainda não existe, a função retorna uma lista vazia.

# Aponte a função que grava os dados e explique quando ela é chamada; mostre o dados.txt gerado após a execução

ARQUIVO = os.path.join(os.path.dirname(__file__), "dados.txt")
SEPARADOR = "|"

tipos_consulta = [ # variavel do tipo lista, ela serve para armzanenar todos os tipos de consulta disponíveis que o usuário pode escolher
    "Clínico Geral",
    "Odontologia",
    "Psicologia",
    "Pediatria",
    "Cardiologia"
]

# ------------------ CARREGAR ------------------
def carregar_cadastros(): # esta é a função que permite a LEITURA dos dados, ou seja, ela lê os dados salvos no arquivo txt e os carrega para a lista de usuários do sistema, ela é essencial paragarantir que todos os cadatros feitos sejam lidos e msotrados no sistema
    if os.path.exists(ARQUIVO):
        try: # esse try/except é utilizado para lidar com possíveis erros que possam ocorrer durante a leitura do arquivo, como por exemplo, o arquivo estar corrompido ou ter um formato inesperado, caso ocorra algum erro, ele retorna uma lista vazia, garantindo que o programa continue funcionando mesmo que haja problemas com o arquivo de dados
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
            print("Sem dados")
            return []
    return []

usuarios = carregar_cadastros()

# ------------------ SALVAR ------------------
def salvar(): #esta é a função que permite a PERSISTÊNCIA dos dados, ou seja, os dados ficam salvos mesmo após o programa ser fechado
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        for u in usuarios:
            linha = f"{u['nome']}{SEPARADOR}{u['nascimento']}{SEPARADOR}{u['email']}{SEPARADOR}{u['senha']}{SEPARADOR}{u['consulta']}{SEPARADOR}{u['data']}{SEPARADOR}{u['hora']}\n" #esse é o formato que os dados serão salvos no arquivo txt, cada campo separado por um SEPARADOR (|) e cada usuário em uma nova linha
            f.write(linha) # isso manda para o arquivo já linkado.

# ------------------ VALIDAÇÕES ------------------
def validar_nome(nome): # esta é a função que valida o nome do usuário, ela verifica se o nome contém apenas letras (maiúsculas ou minúsculas), acentos e espaços, garantindo que o nome seja válido e não contenha caracteres indesejados, isso é importante para manter a integridade dos dados e evitar problemas futuros com nomes inválidos
    return bool(re.fullmatch(r"[A-Za-zÀ-ÿ ]+", nome.strip()))

def validar_data(data):
    return bool(re.fullmatch(r"\d{2}/\d{2}/\d{4}", data.strip()))

def validar_email(email):
    return bool(re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email.strip()))

def validar_senha(senha):
    return len(senha.strip()) > 0

# ------------------ CADASTRO ------------------
def cadastrar(): # esta é a função que permite o cadastro de um novo usuário, ela solicita ao usuário que insira seu nome, data de nascimento, email e senha, e valida cada um desses campos utilizando as funções de validação correspondentes, garantindo que os dados inseridos sejam válidos antes de criar o cadastro do usuário, isso é essencial para manter a qualidade dos dados e evitar problemas futuros com informações inválidas
    while True:
        nome = input("Nome: ") # aqui temos uma variavel do string, ela serve para armazenar o nome do usuário
        if validar_nome(nome):
            break
        print("Nome inválido!")

    while True:
        nascimento = input("Nascimento (dd/mm/aaaa): ")
        global nasc
        nasc = nascimento
        if validar_data(nascimento):
            break
        print("Data inválida!")

    while True:
        email = input("Email: ")
        if not validar_email(email): # operador lógico de negação, ele é utilizado para verificar se o email escrito é válido, ou seja, se ele corresponde ao formato de email esperado, caso contrário, ele exibe a mensagem de email inválido
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


def calcular_idade(nasc):
    hoje = date.today()
    data_formatada = hoje.strftime("%d/%m/%Y")
    nasc_formatado = datetime.strptime(nasc, '%d/%m/%Y')
    idade = hoje.year - nasc_formatado.year - ((hoje.month, hoje.day) < (nasc_formatado.month, nasc_formatado.day))
    return idade



# ------------------ GERAR DATA/HORA ------------------
def gerar_data_hora():
    dia = random.randint(1, 28) # dado no formato INT,
    mes = random.randint(5, 12)
    ano = 2026 # variavel com INT
    hora = random.randint(8, 17)

    data = f"{dia:02d}/{mes:02d}/{ano}"
    hora_str = f"{hora}:00"

    return data, hora_str

# ------------------ MENU DO USUÁRIO ------------------
# Explicar e mostrar todas as opções do menu, como funciona, como marcar uma consulta, ver a consulta marcada, etc.
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

            if escolha.isdigit() and 1 <= int(escolha) <= len(tipos_consulta): # estrutura de decisão, ela é utilizada para verificar se a escolha do usuario é um número e se ele corresponde a uma das opções de consulta disponíveis, caso contrário, ele exibe a mensagem de opção inválida
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
        if u["email"] == email and u["senha"] == senha: # operador relacional de igualdade, ele é utilizado para verificar se o email escrito e a senha existem no txt e estão no mesmo cadastro, ou seja se o email e senha correspondem ao mesmo usuário
            print(f"\nBem-vindo, {u['nome']}!")
            menu_usuario(u)
            return

    print("Login inválido!\n")

# ------------------ MOSTRAR ------------------
def mostrar_usuarios():
    for i in usuarios: # estrutura de repetição, ela é utilizada para percorrer a lista de usuários e exibir o nome, email e tipo de consulta de cada usuário cadastrado, foi utilizado o for pois ele é mais simples e direto para percorrer a lista, já que não precisamos de um índice específico para acessar os elementos da lista, apenas queremos iterar sobre eles
        print(f"{i['nome']} - {i['email']} - {i['consulta']} - {[calcular_idade(i['nascimento'])]} anos")

# ------------------ MENU PRINCIPAL ------------------
while True: # estrutura de repetição, ela é utilizada para exibir o menu principal do sistema e permitir que o usuário escolha uma opção, o loop continua até que o usuário escolha a opção de sair (4), caso contrário, ele exibe o menu novamente após cada ação realizada, foi utilizado while true para criar um loop infinito que só é interrompido quando o usuário escolhe a opção sair ou uma das opçoes do menu, isso garante que o menu seja exibido continuamente até que o usuário decida encerrar o programa
    print("\n==== SUS CONSULTAS ====")
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
        print('Até mais!')
        break
    else:
        print("Opção inválida!")