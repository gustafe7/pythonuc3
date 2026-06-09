class Produto:
    def __init__(self, preco):
        self.preco = preco

    def aplicar_desconto(self, percentual):
        self.preco -= self.preco * (percentual / 100)


produto = Produto(200)

print("Preço original:", produto.preco)

produto.aplicar_desconto(15)

print("Preço com desconto:", produto.preco)