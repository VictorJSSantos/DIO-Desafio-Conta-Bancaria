class Cliente:

    def __init__(self, nome, data_de_nascimento, cpf, endereco):
        self.nome = nome
        self.data_de_nascimento = data_de_nascimento
        self.cpf = self.formatar_cpf(cpf)  # Formata o CPF
        self.endereco = endereco
        self.contas = []

        # Tenta adicionar o usuário automaticamente
        if not ClienteManager.adicionar_usuario(self):
            print("Não foi possível adicionar o usuário, CPF já cadastrado.")

    def formatar_cpf(self, cpf):
        """
        Remove caracteres inválidos do CPF e retorna apenas os números.
        """
        return "".join(filter(str.isdigit, cpf))

    def adicionar_conta(self, conta):
        """
        Adiciona uma conta à lista de contas do cliente.
        """
        self.contas.append(conta)
        print(f"Conta {conta.numero_da_conta} adicionada ao cliente {self.nome}.")

    def listar_contas_do_usuario(self):
        """
        Retorna uma string com a lista de contas cadastradas para este cliente
        """
        if not self.contas:
            return "Nenhuma conta cadastrada."

        contas = [
            f"Agência: {conta.agencia}, Conta: {conta.numero_da_conta}"
            for conta in self.contas
        ]
        return "\n".join(contas)

    def __str__(self):
        texto = f"""
        O usuário {self.nome}, nascido em {self.data_de_nascimento}, com CPF {self.cpf},
        residente em {self.endereco}.
        Contas associadas:
        {self.listar_contas_do_usuario()}
        """
        return texto


class ClienteManager:
    _dict_de_usuarios = {}

    @classmethod
    def adicionar_usuario(cls, cliente):
        """
        Adiciona um cliente ao dicionário. Retorna True se o cliente for adicionado, False caso contrário.
        """
        if cliente.cpf in cls._dict_de_usuarios:
            print(
                f"Erro: O CPF {cliente.cpf} já está cadastrado para {cls._dict_de_usuarios[cliente.cpf].nome}."
            )
            return False

        cls._dict_de_usuarios[cliente.cpf] = cliente
        print(f"Cliente {cliente.nome} adicionado com sucesso.")
        return True

    @classmethod
    def listar_usuarios(cls):
        """
        Retorna uma string com a lista de clientes cadastrados.
        """
        if not cls._dict_de_usuarios:
            return "Nenhum cliente cadastrado."

        usuarios = [
            f"CPF: {cpf}, Nome: {cliente.nome}"
            for cpf, cliente in cls._dict_de_usuarios.items()
        ]
        return "\n".join(usuarios)

    @classmethod
    def buscar_cliente_por_cpf(cls, cpf):
        """
        Retorna o cliente associado ao CPF fornecido, ou None se não encontrado.
        """
        return cls._dict_de_usuarios.get(cpf)

    @classmethod
    def remover_cliente(cls, cpf):
        """
        Remove o cliente associado ao CPF fornecido. Retorna True se o cliente foi removido, False caso contrário.
        """
        if cpf in cls._dict_de_usuarios:
            cliente = cls._dict_de_usuarios.pop(cpf)
            print(f"Cliente {cliente.nome} removido com sucesso.")
            return True
        print(f"Erro: Cliente com CPF {cpf} não encontrado.")
        return False
