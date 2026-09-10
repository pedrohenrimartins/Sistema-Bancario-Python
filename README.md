# Sistema Bancário

Projeto pessoal feito para praticar **Programação Orientada a Objetos em Python**.

É um sistema bancário simples, rodado via terminal, onde é possível cadastrar clientes, criar contas (corrente ou poupança) e realizar operações básicas como depósito, saque e consulta de extrato.

## Objetivo

Esse projeto não tem fins comerciais — é só para fixar conceitos de POO como:

- Herança e classes abstratas
- Polimorfismo
- Encapsulamento
- Composição e agregação
- Exceções personalizadas

## Como rodar

```bash
git clone https://github.com/pedrohenrimartins/Sistema-Bancario.git
cd Sistema-Bancario
python projeto_bancario.py
```

## Funcionalidades

- Cadastro de clientes
- Criação de contas (corrente e poupança)
- Depósito
- Saque (com regras diferentes para cada tipo de conta)
- Extrato com histórico de transações

## Estrutura do projeto

```
ProjetoBancario/
├── entidades/
│   ├── cliente.py
│   └── conta.py
├── operacoes/
│   └── banco.py
├── utilitarios/
│   └── exceptions.py
└── projeto_bancario.py
```

## Status

Em evolução — projeto usado para estudo contínuo, então pode receber melhorias e novas funcionalidades com o tempo.
