class Cliente:
    def __init__(self,nome,cpf):
        self.nome = nome
        self.cpf = cpf
    
class Conta:
    def __init__(self, numero_conta, titular, saldo):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo
        self.saldo_inicial = saldo
        self.extrato = []

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.append(f"Depósito: +R$ {valor:.2f}")

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.extrato.append(f"Saque: -R$ {valor:.2f}")
        else:
            print("Saque não pode ser realizado: saldo insuficiente")

    def transferir(self, valor, conta_destino):
        if self.saldo >= valor:
            self.saldo -= valor
            conta_destino.saldo += valor
            self.extrato.append(f"Transferência enviada: -R$ {valor:.2f}")
            conta_destino.extrato.append(f"Transferência recebida: +R$ {valor:.2f}")
        else:
            print("Transferência não pode ser realizada: saldo insuficiente")

    def consultar_saldo(self):
        return self.saldo
        
class ContaCorrente(Conta):
    def __init__(self, numero_conta, titular, saldo, limite):
        super().__init__(numero_conta, titular, saldo)
        self.limite = limite

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.extrato.append(f"Saque: -R$ {valor:.2f}")

        elif self.saldo + self.limite >= valor:
            valor_restante = valor - self.saldo
            self.saldo = 0
            self.limite -= valor_restante
            self.extrato.append(f"Saque com limite: -R$ {valor:.2f}")

        else:
            print("Saque não pode ser realizado: saldo e limite insuficientes")

    def ver_extrato(self):
        print("\n==============================")
        print(f"EXTRATO - Conta Corrente {self.numero_conta}")
        print(f"Titular: {self.titular.nome}")
        print("------------------------------")

        print(f"Saldo inicial: R$ {self.saldo_inicial:.2f}")
        print("------------------------------")

        if not self.extrato:
            print("Nenhuma movimentação")
        else:
            for op in self.extrato:
                print(op)

        print("------------------------------")
        print(f"Saldo atual: R$ {self.saldo:.2f}")
        print(f"Limite extra disponível: R$ {self.limite:.2f}")
        print("==============================\n")        

class ContaPoupanca(Conta):
    def ver_extrato(self):
        print("\n==============================")
        print(f"EXTRATO - Conta Poupança {self.numero_conta}")
        print(f"Titular: {self.titular.nome}")
        print("------------------------------")

        print(f"Saldo inicial: R$ {self.saldo_inicial:.2f}")
        print("------------------------------")

        if not self.extrato:
            print("Nenhuma movimentação")
        else:
            for operacao in self.extrato:
                print(operacao)

        print("------------------------------")
        print(f"Saldo atual: R$ {self.saldo:.2f}")
        print("==============================\n")

print("\n=== INÍCIO DAS OPERAÇÕES ===\n")

cliente1 = Cliente("João", "123.456.789-12")
cliente2 = Cliente("Maria", "321.654.987.21")

conta1 = ContaCorrente(1234, cliente1, 1000, 500)
conta2 = ContaPoupanca(3214, cliente2, 9000)

conta1.depositar(2000)
conta1.sacar(900)
conta1.transferir(600, conta2)
conta1.depositar(100)
conta1.sacar(50)
conta1.transferir(200, conta2)
conta2.transferir(2699, conta1)

conta1.ver_extrato()
conta2.ver_extrato()


