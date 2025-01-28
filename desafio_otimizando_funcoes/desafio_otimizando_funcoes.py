from datetime import datetime
import pytz
import sys


from cliente.cliente import *
from conta_bancaria.conta import *


"""
Devemos ter duas funções obrigatórias: criar usuário e criar conta corrente
Podemos adicionar mais outras funções, como listar_contas

A função criar_usuarios deverá: Armazenar os usuários em uma lista.
Cada usuário é composto por nome, data_de_nascimento, cpf e endereco
endereco é uma string com formato: Logradouro + ',' + numero + ' - ' + bairro + ' - ' + Cidade + '/' + UF
CPF deve ter validação de input e str = sub([.- ], '', str) 
CPF deve ser a chave única de cadastro

A função criar_conta_corrente deverá: Armazenar as contas em uma lista
Cada conta é composta por agencia, numero_da_conta e usuário
O numero_da_conta é autoincrementável e começa em 1
A agencia é fixa e é 0001
O usuário pode ter mais de uma conta, mas cada conta só pertence a um usuário
"""


def obter_dia_e_hora():
    dia = datetime.now().strftime("%d-%m-%Y")
    hora = datetime.now().strftime("%H:%M:%S")
    return dia, hora


if __name__ == "__main__":

    while True:
        cpf = input("Digite seu cpf: ")
        cpf = "".join(filter(str.isdigit, cpf))
        cliente = ClienteManager.buscar_cliente_por_cpf(cpf)

        menu = """
        Olá, seja bem vindo ao App do Banco Signature!
        Você deseja fazer o que?

        Com relação aos nossos clientes, podemos fazer:

        [a] Realizar seu cadastro
        [b] Olhar suas informações cadastrais
        [c] Abrir uma conta em seu cadastro
        [d] Ver a sua lista de contas abertas
        [e] Fechar uma conta corrente
        [f] Encerrar seu cadastro
        
        Com relaçao a contas correntes:
        [g] Realizar um saque
        [h] Realizar um depósito
        [i] Ver extrato da conta

        Digite 'q' para sair.

        Caso você seja um fucionário do banco, digite 'x' para prosseguir para opções privadas:
        [x] Acesso de funcionário
    """

        resposta = input(menu)

        # Realizar o cadastro do cliente
        if resposta.lower() == "a":
            while True:
                nome = input("Digite seu nome: ")
                data_de_nascimento = input("Digite sua data de nascimento: ")
                endereco = input("Digite seu endereco: ")

                ans = input(
                    'Seus dados estão corretos e podemos prosseguir? Digite "sim" para prossguir e qualquer outro dígito para refazer'
                )
                if ans.lower() == "sim":
                    break

            ClienteManager.adicionar_usuario(
                Cliente(
                    nome,
                    data_de_nascimento=data_de_nascimento,
                    cpf=cpf,
                    endereco=endereco,
                )
            )

        # Mostrar detalhes do cadastro do cliente
        if resposta.lower() == "b":
            if cliente:
                print(cliente)
                input("Aperte enter para continuar")
            else:
                print("Cliente não encontrado. Verifique o CPF informado.")
                input("Aperte enter para continuar")

        # Criar uma conta corrente para o cliente
        if resposta.lower() == "c":
            if cliente:
                GerenciadorDeContaCorrente.criar_conta(cliente)
            else:
                print("Por favor, realize seu cadastro antes de criar uma conta!")
                input("Aperte qualquer tecla para continuar")

        # Consultar lista de contas abertas
        if resposta.lower() == "d":
            if cliente:
                cliente.listar_contas()
            else:
                print("Por favor, realize seu cadastro antes de criar uma conta!")
                input("Aperte qualquer tecla para continuar")

        # Remover uma conta corrente específica
        if resposta.lower() == "e":
            if cliente:
                cliente.listar_contas()
                ans = input("Digite o número da conta que deseja deletar: ")
                GerenciadorDeContaCorrente.remover_conta(ans)
            else:
                print("Por favor, realize seu cadastro antes de criar uma conta!")
                input("Aperte qualquer tecla para continuar")

        # Remover o cliente
        if resposta.lower() == "f":
            if cliente:
                ClienteManager.remover_cliente(cpf)
            else:
                print("Cadastro removido com sucesso!")
                input("Aperte qualquer tecla para continuar")

            ...

        if resposta.lower() == "q":
            sys.exit()
