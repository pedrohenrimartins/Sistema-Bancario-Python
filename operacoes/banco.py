# Projeto Bancário - Sistema Bancário em Python com Programação Orientada a Objetos
# Módulo que define a classe principal do Banco, que gerencia clientes e contas.

# Importa a classe Cliente
from entidades.cliente import Cliente

# Importa a classe base Conta e suas subclasses (Corrente e Poupança)
from entidades.conta import Conta, ContaCorrente, ContaPoupanca

# Importa exceção personalizada para conta inexistente
from utilitarios.exceptions import ContaInexistenteError

class Banco():
        """
        Classe que gerencia as operações do banco.
        Demonstra Composição, pois "tem" clientes e contas.
        """

        # Construtor da classe Banco
        def __init__(self, nome: str):

            # Nome do banco
            self.nome = nome

            # Dicionário de clientes (chave: CPF, valor: objeto Cliente)
            self._clientes = {}

            # Dicionário de contas (chave: número da conta, valor: objeto Conta)
            self._contas = {}


        def adcionar_clientes(self, nome: str, cpf: int) -> Cliente:

            """Cria e adiciona um novo cliente ao banco."""

            # Verifica se já existe cliente com o mesmo CPF
            if cpf in self._clientes:
                print("Erro: Cliente com este CPF já cadastrado.")
                return self._clientes[cpf]

            # Cria objeto Cliente e adiciona ao dicionário
            novo_clinte = Cliente(nome, cpf)
            self._clientes[cpf] = novo_clinte
            print(f"Cliente {nome} adicionado com sucesso!")

            return novo_clinte

        def adicionar_contas(self, cliente: Cliente, tipo: str) -> Conta:

            """Cria uma nova conta para um cliente existente."""

            # Número da nova conta será baseado no total de contas + 1
            numero_conta = Conta.get_total_contas() + 1

            # Cria conta poupança se o tipo informado for "poupanca"
            if tipo.lower() == "poupanca":
                nova_conta = ContaPoupanca(numero_conta, cliente)

            # Cria conta corrente se o tipo informado for "corrente"
            elif tipo.lower() == "corrente":
                nova_conta = ContaCorrente(numero_conta, cliente)

            # Caso o tipo não seja válido
            else:
                print("Tipo de conta inválido. Escolha 'corrente' ou 'poupanca'.")
                return None

            # Adiciona a conta ao dicionário de contas
            self._contas[numero_conta] = nova_conta

            # Associa a conta ao cliente
            print(f"Conta de número {numero_conta} adicionado para o cliente {cliente.nome}.")
            cliente.adicionar_conta(nova_conta)
            return nova_conta

        def buscar_conta(self, numero_conta:int) -> Conta:
            """Busca uma conta pelo seu número."""

            # Tenta recuperar a conta do dicionário
            conta = self._contas.get(numero_conta)

            # Se não encontrar, lança exceção personalizada
            if not conta:
                raise ContaInexistenteError(numero_conta)
            return conta


