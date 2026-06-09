class Teclado:
    def __init__(self,marca,preco,cor):
        self.marca = marca
        self.preco = preco
        self.cor= cor

    def __str__(self):
        return f"Marca: {self.marca}\n Preço: {self.preco}\n Cor: {self.cor}"

tecladologtec = Teclado("logtec",7.50,"preto")
print(tecladologtec)
outroteclado = Teclado("multilaser",10,"vermelho")
print(outroteclado)

#Herença
class Animal:
    def __init__(self, revestimento_externo):
        self.revestimento_externo = revestimento_externo

    def __str__(self):
        return f"Revestimento externo: {self.revestimento_externo}"


class Carnivoro(Animal):
    def comer(self):
        print("Está comendo carne")


class Mamifero(Animal):
    def comer(self):
        print("Está mamando")


cachorro = Carnivoro("Pelo")
print(cachorro)
cachorro.comer()

baleia = Mamifero("Pele")
print(baleia)
baleia.comer()

#Polimorfismo
class Passaro:
    def voar(self):
        return "Voando alto"
    
class Aviao:
    def voar(self):
        return "Avião em velocidade de cruzeiro"


def come(obj):
    print(obj.voar())

come(Passaro())
come(Aviao())