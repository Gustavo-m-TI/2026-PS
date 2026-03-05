# Arquivo: 01b-debug.py
# ATENÇÃO: 4 erros propositais. Encontre e corrija todos!

def saudacao(nome, turno="manhã"):
    mensagem = f"Bom {turno}, {nome}!"
    return mensagem

saudacao("Ana")
print(saudacao("Bruno", "tarde"))

def dobrar(x):
    resultado = x * 2
    return resultado

print("Dobro de 5:", dobrar(5))

total = 0
def incrementar():
    global total
    total = total + 1

incrementar()
print("Total:", total)

def contagem(n):
    if n< 0:
        return
    print(n)
    contagem(n - 1)

contagem(3)
