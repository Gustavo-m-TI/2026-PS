'''
================================================================
# ARQUIVO    : pet.py
# Disciplina : Programação de Sistemas (2026-2)
# Aula       : Aula 20 - Por que POO?
# Autor      : [Gustavo Maciel da Silva]
# Conceitos  : Classe, objeto, atributos, métodos, encapsulamento
# Atividade: Classe Pet
================================================================
'''

class Pet:  # Define a classe Pet para representar um animal de estimação
    '''
    Esta classe representa um Pet em um sistema simples de hotel para para pets.

    Em vez de guardar os dados do pet em um dicionário solto, como
    fazíamos na programação estruturada, agora agrupamos os dados e comportamentos
    dentro de uma classe.
    '''

    def __init__(self, nome, especie, idade, peso, nome_dono, vacinado, observacoes):  # Método construtor da classe, chamado ao criar um objeto Pet
        '''
        Método construtor.

        Ele é executado automaticamente quando criamos um novo objeto Pet.

        Exemplo:
        pet1 = Pet("Rex", "Cachorro", 5, 25.0, "João Silva", True, "Muito brincalhão")

        Parâmetros:
        - nome: nome do pet
        - especie: espécie do pet
        - idade: idade do pet
        - peso: peso do pet
        - nome_dono: nome do dono
        - vacinado: se o pet está vacinado
        - observacoes: observações sobre o pet
        '''

        self.nome = nome  # Atribui o nome do pet ao atributo da instância
        self.especie = especie  # Atribui a espécie do pet ao atributo da instância
        self.idade = idade  # Atribui a idade do pet ao atributo da instância
        self.hospedado = False  # Inicializa o status de hospedagem como falso (não hospedado)
        self.peso = peso  # Atribui o peso do pet ao atributo da instância
        self.nome_dono = nome_dono  # Atribui o nome do dono ao atributo da instância
        self.vacinado = vacinado  # Atribui o status de vacinação ao atributo da instância
        self.observacoes = observacoes  # Atribui as observações sobre o pet ao atributo da instância


    def exibir_dados(self):  # Método para exibir os dados do pet
        '''
        Exibe os dados principais do pet.

        '''

        print("\n--- Dados do Pet ---")  # Imprime um cabeçalho para os dados do pet
        print(f"Nome: {self.nome}")  # Imprime o nome do pet
        print(f"Espécie: {self.especie}")  # Imprime a espécie do pet
        print(f"Idade: {self.idade}")  # Imprime a idade do pet
        print(f"Peso: {self.peso} kg")  # Imprime o peso do pet em kg
        print(f"Dono: {self.nome_dono}")  # Imprime o nome do dono
        print(f"Vacinado: {'Sim' if self.vacinado else 'Não'}")  # Imprime se o pet está vacinado (Sim ou Não)
        print(f"Observações: {self.observacoes}")  # Imprime as observações sobre o pet
        print(f"Hospedado: {'Sim' if self.hospedado else 'Não'}")  # Imprime se o pet está hospedado (Sim ou Não)

    def registrar_entrada(self):  # Método para registrar a entrada do pet no hotel
        '''
        Registra a entrada do pet no hotel.

        Se o pet ainda não estiver hospedado, muda o atributo hospedado para True
        '''

        if self.hospedado:
            print(f"Atenção: {self.nome} já está hospedado.")
        else:
            self.hospedado = True
            print(f"{self.nome} entrou no hotel.")

    def registrar_saida(self):
        '''
        Registra a saída do pet do hotel.
        '''

        if not self.hospedado:
            print(f"Atenção: {self.nome} não está hospedado.")
        else:
            self.hospedado = False
            print(f"{self.nome} saiu do hotel.")

    def calcular_diaria(self):
        '''
        Calcula o valor da diária para o pet.
        Este método deve retornar o valor da diária.
        '''

        if self.idade <= 3:
            return 50.00
        elif self.idade <= 10:
            return 60.00
        else:
            return 75.00

    def verificar_vacinacao(self):
        '''
        Verifica se o pet está vacinado.
        '''

        if self.vacinado:
            print("Vacinação em dia.")
        else:
            print("Atenção: Vacinação pendente.")

    def atualizar_peso(self, novo_peso):
        '''
        Atualiza o peso do pet.

        '''

        self.peso = novo_peso
        print(f"Peso de {self.nome} atualizado para {self.peso} kg.")

    def emitir_resumo(self):
        '''
        Exibe um resumo geral do pet.

        Este método deve usar informações dos atributos e também pode
        chamar outros métodos, como calcular_diaria().
        '''

        diaria = self.calcular_diaria()
        print("\n--- Resumo do Pet ---")
        print(f"Nome: {self.nome}")
        print(f"Espécie: {self.especie}")
        print(f"Idade: {self.idade} anos")
        print(f"Dono: {self.nome_dono}")
        print(f"Peso: {self.peso} kg")
        print(f"Vacinação: {'Em dia' if self.vacinado else 'Pendente'}")
        print(f"Hospedagem: {'Hospedado' if self.hospedado else 'Não hospedado'}")
        print(f"Diária: R$ {diaria:.2f}")

'''
# ============================================================
# TESTE DA CLASSE:
# ============================================================
# Depois de completar a classe, crie pelo menos 3 objetos Pet.
# 
# Exemplo:
# pet1 = Pet("Rex", "Cachorro", 5)
# 
# Atenção:
# Se você adicionou novos parâmetros no __init__, será necessário
# informar esse dados na criação do objeto.
# ============================================================
'''

pet1 = Pet("Rex", "Cachorro", 5, 25.0, "João Silva", True, "Muito brincalhão")
pet2 = Pet("Clepton", "Monstro do lago Ness", 3000, 87000.0, "Rei Arthur", True, "Gosta de derrubar embarcações")
pet3 = Pet("Bruu Bruu Patapim", "Guardião da floresta", 10000000, 1000.0, "Thung Thung Thung Sahur", True, "Gosta de matar lenhadores e caçadores")

print("=== Teste dos Pets ===")

print("\n--- Pet 1 ---")
pet1.exibir_dados()
pet1.verificar_vacinacao()
pet1.registrar_entrada()
pet1.emitir_resumo()

print("\n--- Pet 2 ---")
pet2.exibir_dados()
pet2.verificar_vacinacao()
pet2.atualizar_peso(90000.0)
pet2.emitir_resumo()

print("\n--- Pet 3 ---")
pet3.exibir_dados()
pet3.registrar_entrada()
pet3.emitir_resumo()
pet3.registrar_saida()
pet3.registrar_saida()  # teste de saída quando não está hospedado