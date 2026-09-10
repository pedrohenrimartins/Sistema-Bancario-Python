"""
Projeto Bancário - Sistema Bancário em python com programação orientada a objetos
Módulo da Entidade Cliente
"""

# Define a classe do cliente
class Cliente:

    # Metodo construtor que inicializa os atributos da classe
    def __init__(self, nome, cpf):

        # Atributo para armazenar o nome do cliente
        self.nome = nome

        # Atributo para armazenar o cpf do cliente
        self.cpf = cpf

        # Atributo para armazenar as contas associadas ao cliente
        self.contas = []


    # Metodo para adicionar uma conta a lista de contas do cliente
    def adicionar_conta(self, conta):

        # Insere o objeto conta na lista de contas
        self.contas.append(conta)


    # Metodo especial que define a reapresentação em string do objeto
    def __str__(self):

        # Retorna uma string formatada com o nome e cpf do cliente
        return f"Cliente: {self.nome} (CPF: {self.cpf})"
