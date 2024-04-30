from abc import ABC, abstractmethod

class Cliente():

    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    @property
    def contas(self):
        return self._contas
    
    def realizar_transacao(self, conta, transacao):
            if transacao is Saque:
                conta.sacar()
            else:
                conta.depositar()

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    @classmethod
    def novo_cliente(cls, cpf, nome, data_nascimento, endereco):
        return PessoaFisica(cpf, nome, data_nascimento, endereco)


class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento
    
    @property
    def cpf(self):
        return self._cpf

    @property
    def nome(self):
        return self._nome

    @property
    def endereco(self):
        return self._endereco
    
    @property
    def data_nascimento(self):
        return self._data_nascimento


class Transacao(ABC):

    @abstractmethod
    def registrar(self):
        pass

    @property
    def valor(self):
        pass


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        conta.historico.adicionar_transacao(self)

    def __str__(self):
        return f"DEPÓSITO - R$ {self.valor:.2f}"


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        conta.historico.adicionar_transacao(self)

    def __str__(self):
        return f"SAQUE - R$ {self.valor:.2f}"


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)


class Conta:
    _AGENCIA = "0001"

    def __init__(self, cliente, numero):
        self._numero = numero
        self._cliente = cliente
        self._saldo = 0
        self._historico = Historico()

    def __str__(self):
        return f"""
Número da conta - {self.numero}
Agência - {self.agencia}
Cliente - {self.cliente.nome}"""
    
    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._AGENCIA

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    @classmethod
    def nova_conta(cls, cliente, numero):
        return ContaCorrente(cliente, numero)

    def sacar(self, valor):
        if valor <= 0:
            print("\nImpossível sacar valores negativos ou nenhum valor, por favor insira um valor positivo para sacar na próxima!")
            return False
        elif valor > self.saldo:
            print(f"""
Valor excede o valor do seu saldo em conta, que no momento é: R${self.saldo:.2f}
Insira um valor de saque condizente com a quantidade de seu saldo""")
            return False
        else:
            saque = Saque(valor)
            self._saldo -= saque.valor
            saque.registrar(self)
            print("\nSaque efetuado com sucesso!")
            return True
        
    def depositar(self, valor):
            deposito = Deposito(valor)
            self._saldo += deposito.valor
            deposito.registrar(self)
            print("\nDepósito efetuado com sucesso!")
            return True
    
    def mostrar_extrato(self):
        print("\nEXTRATO ABAIXO:\n\n" + "\n".join([tran.__str__() for tran in self.historico.transacoes]))
        print(f"\nSALDO - {self.saldo:.2f}" )


class ContaCorrente(Conta):
    _LIMITE = 500
    _limite_saques = 3

    def __init__(self, cliente, numero):
        super().__init__(cliente, numero)

    @property
    def limite(self):
        return self._LIMITE
    
    @property
    def limite_saque(self):
        return self._limite_saques
    
    def sacar(self):
        if self.limite_saque == 0:
            print("\nNão há mais saques disponíveis, tente de novo outro dia!")
            return False
        valor = int(input("\nInsira o valor que deseja sacar: "))
        if valor > self.limite:
            print("\nValor do saque maior do que o limite, por favor insira um valor de 1 até 500!")
            return False
        if super().sacar(valor):
            self._limite_saques -= 1
            return True
    
    def depositar(self):
        valor = int(input("\nInsira o valor que deseja depositar: "))
        if valor <= 0:
            print("\nImpossível depositar valores negativos ou nenhum valor, por favor insira um valor positivo para depositar na próxima!")
            return False
        return super().depositar(valor)
    

class Menu:
    decisao_sair = 0
    clientes = []
    def sair(decisao_sair):
        while decisao_sair != 1 and decisao_sair != 2:
                print("\nTem certeza que deseja sair?")
                decisao_sair = int(input("\nSelecione 1 para SIM ou 2 para NÃO: "))
                if decisao_sair == 1:
                    print("\nEntão tá :( até outro dia!\n")
                    return 1
                elif decisao_sair != 2:
                    print("\nSelecione uma das opções para sua decisão!")
                else:
                    print("\nObrigado por continuar conosco :D")
                    return 0

    def cliente_existe(clientes, cpf):
        cliente = [cliente_x for cliente_x in clientes if cliente_x.cpf == cpf]
        return cliente

    def conta_existe(contas, numero):
        conta = [conta_x for conta_x in contas if conta_x.numero == numero]
        return conta
    
    @classmethod
    def main(self):
        while self.decisao_sair != 1:
            print("""
                Bem-vindo ao nosso banco!!
                O que deseja fazer hoje?

                1 - Depositar
                2 - Sacar
                3 - Ver extrato
                4 - Criar cliente
                5 - Criar conta corrente
                6 - Sair
            """)
            opcao = int(input())
            if opcao == 1:
                cpf = input("Digite seu cpf: ")
                cliente_x = self.cliente_existe(self.clientes, cpf)
                if cliente_x:
                    print("\n".join([conta.__str__() for conta in cliente_x[0].contas]))
                    conta_numero = int(input("Ótimo, agora digite o número da conta que deseja depositar: "))
                    conta_x = self.conta_existe(cliente_x[0].contas, conta_numero)
                    if conta_x:
                        conta_x[0].depositar()
                    else:
                        print("\nEsta conta com este número não existe para este cliente!")
                else:
                    print("\nEste CPF não está registrado no nosso banco!")

            elif opcao == 2:
                cpf = input("Digite seu cpf: ")
                cliente_x = self.cliente_existe(self.clientes, cpf)
                if cliente_x:
                    print("\n".join([conta.__str__() for conta in cliente_x[0].contas]))
                    conta_numero = int(input("\nÓtimo, agora digite o número da conta que deseja sacar: "))
                    conta_x = self.conta_existe(cliente_x[0].contas, conta_numero)
                    if conta_x:
                        conta_x[0].sacar()
                    else:
                        print("\nEsta conta com este número não existe para este cliente!")
                else:
                    print("\nEste CPF não está registrado no nosso banco!")

            elif opcao == 3:
                cpf = input("Digite seu cpf: ")
                cliente_x = self.cliente_existe(self.clientes, cpf)
                if cliente_x:
                    print("\n".join([conta.__str__() for conta in cliente_x[0].contas]))
                    conta_numero = int(input("Ótimo, agora digite o número da conta que deseja ver o extrato: "))
                    conta_x = self.conta_existe(cliente_x[0].contas, conta_numero)
                    if conta_x:
                        conta_x[0].mostrar_extrato()
                    else:
                        print("\nEsta conta com este número não existe para este cliente!")
                else:
                    print("\nEste CPF não está registrado no nosso banco!")

            elif opcao == 4:
                cpf = input("Digite seu cpf: ")
                if self.cliente_existe(self.clientes, cpf):
                    print("\nCliente já existe no banco!")
                else:    
                    nome = input("Digite seu nome: ")
                    data = input("Digite sua data de nascimento (dd-mm-aaaa): ")
                    endereco = input("Digite seu endereço (logradouro, número - bairro - cidade/sigla do estado): ")
                    self.clientes.append(Cliente.novo_cliente(cpf, nome, data, endereco))
                    print(f"\nCliente registrado com sucesso, bem vindo {nome}!")

            elif opcao == 5:
                cpf = input("Digite seu cpf: ")
                cliente_x = self.cliente_existe(self.clientes, cpf)
                if cliente_x:
                    cliente_x[0].contas.append(Conta.nova_conta(cliente_x[0], len(cliente_x[0].contas) + 1))
                    print(f"\nConta registrada com sucesso!")
            elif opcao == 6:
                self.decisao_sair = self.sair(self.decisao_sair)

            else:
                print("\nSelecione uma das opções do menu para prosseguir com sua ação!")

Menu.main()