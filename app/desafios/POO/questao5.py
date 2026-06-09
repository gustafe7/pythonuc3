class Livro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.disponivel = True


livro1 = Livro("Dom Casmurro")

print("Título:", livro1.titulo)
print("Disponível:", livro1.disponivel)