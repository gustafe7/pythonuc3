class Veiculo:
    def __init__(self, marca):
        self.marca = marca


class Carro(Veiculo):
    pass


class Moto(Veiculo):
    pass


carro = Carro("Toyota")
moto = Moto("Honda")

print("Carro:", carro.marca)
print("Moto:", moto.marca)