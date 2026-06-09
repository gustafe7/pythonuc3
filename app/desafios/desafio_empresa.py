class Cliente:
    def __init__(self,nome,cpf):
        self.nome = nome
        self.cpf = cpf

class Conta:
    def cliente(self,numero_conta,titular,saldo):
        self.numero_conta = numero_conta
        self.titular = titular
        self,saldo = saldo

class Operacoes:
    def cliente(self,depositar,sacar,transferir,consultar_saldo):
        self.depositar = depositar
        self.sacar = sacar
        self.transferir = transferir
        self.consultar_saldo = consultar_saldo