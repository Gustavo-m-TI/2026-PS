from datetime import date, datetime

nasc = input("Digite sua data de nascimento (dd/mm/aaaa): ")

def calcular_idade(nasc):
    hoje = date.today()
    data_formatada = hoje.strftime("%d/%m/%Y")

    nascimento = datetime.strptime(nasc, '%d/%m/%Y')
    
    idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
    return idade

idade_calculada = calcular_idade(nasc)
print(f"Sua idade é: {idade_calculada} anos")