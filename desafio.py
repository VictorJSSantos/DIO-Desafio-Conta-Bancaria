import sys


class ContaBancaria:
    def __init__(self):
        self.saldo = 0
        self.limite_de_saque = 500
        self.quantidade_de_saques_a_realizar = 3

    def depositar(self, valor):

        if valor > 0:
            self.saldo += valor
            print(
                f"Valor de R${valor:.2f} adicionado ao saldo. Saldo total em R${self.saldo:.2f}"
            )

    def sacar(self, valor):

        if (
            (valor <= 500)
            and (self.saldo - valor >= 0)
            and (self.quantidade_de_saques_a_realizar > 0)
        ):
            self.saldo -= valor
            self.quantidade_de_saques_a_realizar -= 1
            print(
                f"O valor de {valor:.2f} foi sacado da conta e agora o saldo é {self.saldo:.2f}. Restam {self.quantidade_de_saques_a_realizar} operações de saque."
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
        extrato = f"""
    A sua conta contém {self.quantidade_de_saques_a_realizar} operações de saques para realizar.
    O saldo total é R${self.saldo:.2f}
"""
        print(extrato)


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
