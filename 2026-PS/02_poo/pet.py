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

class Pet:
    '''
    Esta classe representa um Pet em um sistema simples de hotel para para pets.

    Em vez de guardar os dados do pet em um dicionário solto, como
    fazíamos na programação estruturada, agora agrupamos os dados e comportamentos
    dentro de uma classe.
    '''

    def __init__(self, nome, especie, idade, peso, nome_dono, vacinado, observacoes):
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

        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.hospedado = False
        self.peso = peso
        self.nome_dono = nome_dono
        self.vacinado = vacinado
        self.observacoes = observacoes


        '''
        # ============================================================
        # ATIVIDADE 1:
        # Adicione pelo menos 3 novos atributos para o pet.
        #
        # Sugestões:
        # self.raca
        # self.peso
        # self.nome_dono
        # self.telefone_dono
        # self.vacinado
        # self.observacoes
        #
        # Atenção:
        # Se você adicionar novos atributos, também precisará alterar
        # os parâmetros do __init__.
        # ============================================================
        '''

    def exibir_dados(self):
        '''
        Exibe os dados principais do pet.

        Atualmente, mostra apenas nome, espécie, idade e status de
        hospedagem.

        ATIVIDADE:
        Modifique este método para exibir também os novos atributos
        que você adicionou no __init__.
        '''

        print("\n--- Dados do Pet ---")
        print(f"Nome: {self.nome}")
        print(f"Espécie: {self.especie}")
        print(f"Idade: {self.idade}")
        print(f"Peso: {self.peso} kg")
        print(f"Dono: {self.nome_dono}")
        print(f"Vacinado: {'Sim' if self.vacinado else 'Não'}")
        print(f"Observações: {self.observacoes}")
        print(f"Hospedado: {'Sim' if self.hospedado else 'Não'}")

    def registrar_entrada(self):
        '''
        Registra a entrada do pet no hotel.

        Se o pet ainda não estiver hospedado, muda o atributo hospedado para True
        
        ATIVIDADE:
        Melhore este método para verificar se o pet já está hospedado.
        Se já estiver, mostre uma mensagem avisando.
        '''

        if self.hospedado:
            print(f"Atenção: {self.nome} já está hospedado.")
        else:
            self.hospedado = True
            print(f"{self.nome} entrou no hotel.")

    def registrar_saida(self):
        '''
        Registra a saída do pet do hotel.

        Se o pet estiver hospedado, muda o atributo hospedado para False
        
        ATIVIDADE:
        Melhore este método para verificar se o pet já está hospedado.
        Se não estiver, mostre uma mensagem avisando.
        '''

        if not self.hospedado:
            print(f"Atenção: {self.nome} não está hospedado.")
        else:
            self.hospedado = False
            print(f"{self.nome} saiu do hotel.")

    def calcular_diaria(self):
        '''
        Calcula o valor da diária para o pet.

        ATIVIDADE:
        Implemente uma regra simples para calcular a diária.
        
        Sugestão:
        - Pet com idade até 3 anos: R$ 50,00
        - Pet com idade entre 4 e 10 anos: R$ 60,00
        - Pet com mais de 10 anos: R$ 75,00
        
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

        ATIVIDADE:
        Para este metódo funcionar, você precisa criar um atributo 
        chamado self.vacinado no __init__.
            
        Se o pet estiver vacinado, exiba:
        "Vacinação em dia."
            
        Caso contrário, exiba:
        "Atenção: Vacinação pendente."
        '''

        if self.vacinado:
            print("Vacinação em dia.")
        else:
            print("Atenção: Vacinação pendente.")

    def atualizar_peso(self, novo_peso):
        '''
        Atualiza o peso do pet.

        ATIVIDADE:
        Para este método funcionar, você precisa criar um atributo
        chamado self.peso no __init__.

        O método deve receber um novo peso e atualizar o valor antigo.

        Exemplo:
        pet1.atualizar_peso(12.5)
        '''

        self.peso = novo_peso
        print(f"Peso de {self.nome} atualizado para {self.peso} kg.")

    def emitir_resumo(self):
        '''
        Exibe um resumo geral do pet.

        ATIVIDADE:
        Crie uma mensagem organizada contendo:
        - nome do pet
        - espécie
        - idade
        - nome do dono
        - peso
        - status de vacinação
        - status de hospedagem
        - valor da diária

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
pet2 = Pet("Mia", "Gato", 2, 4.5, "Maria Oliveira", False, "Gosta de dormir no sol")
pet3 = Pet("Buddy", "Cachorro", 8, 30.0, "Carlos Santos", True, "Adora passear")

print("=== Teste dos Pets ===")

print("\n--- Pet 1 ---")
pet1.exibir_dados()
pet1.verificar_vacinacao()
pet1.registrar_entrada()
pet1.emitir_resumo()

print("\n--- Pet 2 ---")
pet2.exibir_dados()
pet2.verificar_vacinacao()
pet2.atualizar_peso(5.0)
pet2.emitir_resumo()

print("\n--- Pet 3 ---")
pet3.exibir_dados()
pet3.registrar_entrada()
pet3.emitir_resumo()
pet3.registrar_saida()
pet3.registrar_saida()  # teste de saída quando não está hospedado