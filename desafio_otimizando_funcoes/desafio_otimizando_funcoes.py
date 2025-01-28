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
    ClienteManager()
    GerenciadorDeContaCorrente()

    while True:
        try:
            if cpf:
                mudar_cpf = input(
                    f'Quer mudar o CPF? Se sim, digite "sim", se não seguiremos com o cpf {cpf}. '
                )
                if mudar_cpf.lower == "sim":
                    cpf = input("Digite seu cpf: ")
                    cpf = "".join(filter(str.isdigit, cpf))
        except:
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
                print(cliente.listar_contas_do_usuario())
            else:
                print("Por favor, realize seu cadastro antes de criar uma conta!")
                input("Aperte qualquer tecla para continuar")

        if resposta.lower() == "e":
            if cliente:
                print(cliente.listar_contas_do_usuario())
                ans = int(input("Digite o número da conta que deseja deletar: "))
                # Remover a conta do GerenciadorDeContaCorrente
                if GerenciadorDeContaCorrente.remover_conta(ans):
                    # Caso a conta seja removida com sucesso, também remova da lista de contas do cliente
                    for conta in cliente.contas:
                        if conta.numero_da_conta == ans:
                            cliente.contas.remove(conta)
                            break
                else:
                    print("Falha ao remover a conta.")
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

        if resposta.lower() == "q":
            sys.exit()
