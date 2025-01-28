from datetime import datetime
import pytz
import sys


def obter_dia_e_hora():
    dia = datetime.now().strftime("%d-%m-%Y")
    hora = datetime.now().strftime("%H:%M:%S")
    return dia, hora


class ContaBancaria:
    def __init__(self):
        self.saldo = 0
        self.limite_de_saque = 500
        self.quantidade_de_transacoes = 10
        self.registro_de_transacoes = {}
        self.horario_das_transacoes = []

    def adicionar_registro_de_transacao(self):
        dia, hora = obter_dia_e_hora()
        self.horario_das_transacoes.append(hora)
        self.registro_de_transacoes.update({dia: self.horario_das_transacoes})
        self.quantidade_de_transacoes -= 1
        print(f"Total de transações restantes é de {self.quantidade_de_transacoes}")

    def depositar(self, valor):

        if valor > 0:
            self.saldo += valor
            self.adicionar_registro_de_transacao()
            print(
                f"Valor de R${valor:.2f} adicionado ao saldo. Saldo total em R${self.saldo:.2f}"
            )

    def sacar(self, valor):

        if (
            (valor <= 500)
            and (self.saldo - valor >= 0)
            and (self.quantidade_de_transacoes > 0)
        ):
            self.saldo -= valor
            self.adicionar_registro_de_transacao()
            print(
                f"O valor de {valor:.2f} foi sacado da conta e agora o saldo é {self.saldo:.2f}. Restam {self.quantidade_de_transacoes} operações de saque."
            )
        elif valor > 500:
            print(f"O valor do saque {valor:.2f} é maior que o permitido de R$500.00")
        elif self.saldo - valor <= 0:
            print(
                f"O seu saldo é insuficiente para sacar. Saldo de R${self.saldo:.2f} e tentativa de saque de R${valor:.2f}"
            )
        else:
            print(f"Você não possui mais operações de saque a realizar.")

    def consultar_extrato(self):
        if self.registro_de_transacoes:
            for key, value_list in self.registro_de_transacoes.items():
                for value in value_list:
                    print(f"No dia {key}, na hora {value} tivemos uma transação")
        else:
            print(f"Ainda não aconteceu nenhuma transação.")


if __name__ == "__main__":

    conta = ContaBancaria()

    while True:

        menu = """

        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair

        => """

        opcao = input(menu)

        if opcao == "d":

            valor = float(input("Informe o valor do depósito na conta: "))
            conta.depositar(valor)

        if opcao == "s":
            valor = float(input("Informe o valor a ser sacado da conta: "))
            conta.sacar(valor)

        if opcao == "e":
            conta.consultar_extrato()

        if opcao == "q":
            print(f"Programa terminado pelo usuário")
            break
