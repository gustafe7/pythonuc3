class Pessoa:
    quantidade = 0

    def __init__(self, nome):
        self.nome = nome
        Pessoa.quantidade += 1


p1 = Pessoa("Gustavo")
p2 = Pessoa("Maria")
p3 = Pessoa("João")
p4 = Pessoa("Tainá")
p5 = Pessoa("Fernanda")
p6 = Pessoa("Luis")
p7 = Pessoa("Maycon")
p8 = Pessoa("Carol")
p9 = Pessoa("Átila")

print("Objetos criados:", Pessoa.quantidade)