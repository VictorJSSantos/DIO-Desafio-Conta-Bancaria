from cliente.cliente import *


class ContaCorrente:
    def __init__(self, cliente: Cliente, agencia="0001", numero_de_saques=10, saldo=0):
        self.agencia: str = agencia
        self.cliente: Cliente = cliente
        self.numero_da_conta: int = None  # Será atribuído pelo gerenciador
        self.numero_de_saques: int = numero_de_saques
        self.saldo: float = saldo
        self.historico_transacoes = []  # Lista para armazenar o histórico de transações

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente para o saque.")
        else:
            if self.numero_de_saques > 0:
                self.saldo -= valor
                self.numero_de_saques -= 1
                self.historico_transacoes.append(
                    f"Saque de R${valor:.2f} - Saldo restante: R${self.saldo:.2f}"
                )
                print(f"O saque foi feito. Saldo restante: R${self.saldo}")
            else:
                print("Problema ao sacar: Número de saques insuficientes.")
                return None

    def depositar(self, valor):
        self.saldo += valor
        self.historico_transacoes.append(
            f"Depósito de R${valor:.2f} - Saldo atual: R${self.saldo:.2f}"
        )
        print(f"O depósito foi feito. Saldo atual: R${self.saldo}")

    def exibir_extrato(self):
        """
        Exibe o extrato completo da conta.
        """
        if not self.historico_transacoes:
            print("Nenhuma transação realizada até o momento.")
        else:
            print(
                f"\nExtrato da Conta Corrente {self.numero_da_conta} - Agência {self.agencia}:"
            )
            for transacao in self.historico_transacoes:
                print(transacao)
            print(f"Saldo atual: R${self.saldo:.2f}")
            print(f"Saques restantes: {self.numero_de_saques}")

    def __str__(self):
        texto = f"""C/C número: {self.numero_da_conta} | Agência: {self.agencia} | Saldo: {self.saldo} | Dono: {self.cliente.nome}."""
        return texto


class GerenciadorDeContaCorrente:
    _lista_de_contas = []

    @classmethod
    def criar_conta(cls, cliente, agencia="0001"):
        """
        Cria uma nova conta corrente associada a um cliente.
        """
        numero_da_conta = (
            len(cls._lista_de_contas) + 1
        )  # Gera número da conta automaticamente
        conta = ContaCorrente(cliente, agencia)
        conta.numero_da_conta = numero_da_conta
        cls._lista_de_contas.append(conta)

        # Vincular a conta ao cliente
        cliente.adicionar_conta(conta)

        print(f"Conta criada: {conta}")
        return conta

    @classmethod
    def listar_contas(cls):
        """
        Retorna uma string com a lista de todas as contas correntes e seus dados.
        """
        if not cls._lista_de_contas:
            return "Nenhuma conta cadastrada."

        contas = [
            f"Agência: {conta.agencia}, Conta: {conta.numero_da_conta}, Cliente: {conta.cliente.nome}"
            for conta in cls._lista_de_contas
        ]
        print("\n".join(contas))

    @classmethod
    def buscar_conta_por_numero(cls, numero_da_conta):
        """
        Busca uma conta corrente pelo número.
        """
        for conta in cls._lista_de_contas:
            if conta.numero_da_conta == numero_da_conta:
                return conta
        print(f"Conta número {numero_da_conta} não encontrada.")
        return None

    @classmethod
    def remover_conta(cls, numero_da_conta):
        """
        Remove uma conta corrente pelo número. Retorna True se a conta foi removida, False caso contrário.
        """
        conta = cls.buscar_conta_por_numero(numero_da_conta)
        if conta:
            # Remover a conta da lista de contas
            cls._lista_de_contas.remove(conta)
            print(f"Conta número {numero_da_conta} removida com sucesso.")
            return True
        print(f"Conta número {numero_da_conta} não encontrada.")
        return False
