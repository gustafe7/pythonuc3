class Contador:
    def __init__(self):
        self.valor = 0

    def aumentar(self):
        self.valor += 1

    def diminuir(self):
        self.valor -= 1


contador = Contador()

contador.aumentar()
contador.aumentar()
print("Valor:", contador.valor)

contador.diminuir()
print("Valor:", contador.valor)