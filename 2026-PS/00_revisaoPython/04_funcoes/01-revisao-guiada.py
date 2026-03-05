# ===================================================
# SISTEMA DE CÁLCULO DE IMC
# ---------------------------------------------------
# Disciplina : Programação de Sistemas (PS)
# Aula       : 06 - Revisão: Funções
# Autor      : [Gustavo Maciel da Silva]
# Data       : [03/03/2026]
# Repositório: https://github.com/[Gustavo-m-TI]/2026-PS
# ===================================================
#
# DESCRIÇÃO:
# Calcula e classifica o IMC de uma pessoa.
# Demonstra definição de funções, parâmetros,
# retorno, escopo e recursão.
# ===================================================
#
# ---- FUNÇÃO SEM PARÂMETROS E SEM RETORNO ----

def exibir_cabecalho():
    """Exibe o cabeçalho do sistema no terminal."""
    print("=" * 40)
    print("     SISTEMA DE CÁLCULO DE IMC")
    print("=" * 40)

def exibir_rodape():
    """Exibe mensagem de encerramento."""
    print("\n" + "=" * 40)
    print("     FIM DO PROGRAMA")
    print("=" * 40)

# ---- FUNÇÃO COM PARÂMETROS E RETORNO ----

def calcular_imc(peso, altura):
    """Calcula e retorna o IMC. Fórmula: peso / altura²"""
    imc = peso / (altura ** 2)  # ** é o operador de potência
    return imc  # devolve o resultado para quem chamou

# ---- ESCOPO LOCAL vs. GLOBAL ----

versao = "1.0"  # variável GLOBAL — existe fora de qualquer função

def demonstrar_escopo():
    mensagem = "Olá do interior da função"  # variável LOCAL
    print("Dentro da função:")
    print(f"  mensagem = {mensagem}")  # OK: local existe aqui
    print(f"  versao   = {versao}")    # OK: global é visível dentro

# ---- VALOR PADRÃO E MÚLTIPLOS RETORNOS ----

def classificar_imc(imc, unidade="kg/m²"):
    """Classifica o IMC e retorna classificação & emoji de status.
    Parâmetro 'unidade' tem valor padrão – não é obrigatório informar."""
    
    if imc < 18.5:
        classificacao = "Abaixo do peso"
        emoji = "😔"
    elif imc < 25.0:
        classificacao = "Peso normal"
        emoji = "😊"
    elif imc < 30.0:
        classificacao = "Sobrepeso"
        emoji = "⚠"
    else:
        classificacao = "Obesidade"
        emoji = "😢"
    
    return classificacao, emoji  # retorna dois valores — Python empacota como tupla

# ---- RECURSÃO BÁSICA ----

def contagem_regressiva(n):
    """Exibe contagem regressiva de n até 0 usando recursão."""
    if n < 0:       # CASO BASE: para a recursão
        return
    print(n)
    contagem_regressiva(n - 1)  # CHAMADA RECURSIVA: resolve problema menor

# Fatorial: exemplo clássico de recursão com retorno
def fatorial(n):
    """Calcula n! recursivamente. Ex: 5! = 5 × 4 × 3 × 2 × 1 = 120"""
    if n == 0 or n == 1:  # caso base
        return 1
    return n * fatorial(n - 1)  # caso recursivo

# ---- FUNÇÃO PRINCIPAL ----

def processar_pessoa():
    """Coleta dados, calcula IMC e exibe resultado completo."""
    nome   = input("\nNome: ")
    peso   = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))
    
    imc = calcular_imc(peso, altura)    # reutiliza funções já definidas
    classificacao, emoji = classificar_imc(imc)
    
    print("\n--- Resultado ---")
    print(f"Nome           : {nome}")
    print(f"IMC            : {imc:.2f} kg/m²")
    print(f"Classificação  : {classificacao} {emoji}")

# ---- EXECUÇÃO PRINCIPAL ----

exibir_cabecalho()

continuar = "s"
while continuar == "s":
    processar_pessoa()
    continuar = input("\nProcessar outra pessoa? (s/n): ").lower()

exibir_rodape()
