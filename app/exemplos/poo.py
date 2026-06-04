#criando base(planta do objeto)
class Carro:
    def __init__(self,motor,quant_rodas):
        self.motor = motor
        self.quant_rodas = quant_rodas

#criando um objeto
car1 = Carro("v8",4)
car2 = Carro("v12",4)

#mostrar as informações do objeto
print("Carro 1 tem o motor: ",car1.motor)
print("Carro 2 tem o motor: ",car2.motor)


def __init__(self):
        pass
#sem valores obrigatórios
class Conta:
    def __init__(self):
        pass

#iniciar classe com valores padrão
class Funcinario:
   nome = ""
   idade = 0
   cargo = ""

print("\n====================\n")

class Cliente:
    def __init__(self,nome,cpf,telefone,email):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email

cliente1 = Cliente(nome="Camila",cpf="123.145.123-02",telefone="(21)99256-6325",email="camilia@gmail.com")
cliente2 = Cliente(nome="Gustavo",cpf="253.256.256-03",telefone="(21)99865-9632",email="gustavo@gamil.com")

print("nome: ",cliente1.nome)
print("cpf: ",cliente1.cpf)
print("telefone:", cliente1.telefone)
print("email: ",cliente1.email)

print("\n====================\n")

print("nome: ",cliente2.nome)
print("cpf: ",cliente2.cpf)
print("telefone:", cliente2.telefone)
print("email: ",cliente2.email)

print("\n====================\n")

class Televisao:
    def __init__(self):
        self.ligada = False

    def ligar(self):
        self.ligada = True

    def desligar(self):
        self.ligada = False

tv = Televisao()

tv.ligar()
print(tv.ligada)

tv.desligar()
print(tv.ligada)

print("\n====================\n")

class Aluno:
    def estudar(self):
        for i in range(5):
            print("Estou estudando!")
    
    def VouEstudar(self,resposta):
        if resposta == "sim":
            print("Bom estudo!")
        else:
            print("Acho melhor você estudar!")

aluno = Aluno()
aluno.estudar()
resposta = input("Você vai estudar hoje? ")
aluno.VouEstudar(resposta)