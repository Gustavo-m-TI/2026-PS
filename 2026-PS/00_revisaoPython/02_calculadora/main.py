def Leia ():
    n1 = int(input('Digite 1 valor: '))
    n2 = int(input('Digite outro valor: '))
    op = input('Digite a Operação [* / + -]: ')
    while op != '*' and '/' and '+' and '-':
        print('Sinal invalido')
        op = input('Digite a Operação [* / + -]: ')
    msg = f'{n1} {op} {n2}'
    if op == '+':
        res = Soma(n1, n2)
    elif op == '-':
        res = Subtração(n1, n2)
    elif op == '*':
        res = Multiplicação(n1, n2)
    elif op == '/':
        res = Divisão(n1, n2)
    Escreva(msg, res)

def Soma (n1, n2):
    return (n1 + n2)

def Subtração (n1, n2):
    return (n1 - n2)

def Multiplicação (n1, n2):
    return (n1 * n2)

def Divisão (n1, n2):
    return (n1 / n2)
def Escreva (msg, resultado):
    print(f'{msg} = {resultado}')

Leia()
