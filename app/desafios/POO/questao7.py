class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, contato):
        self.contatos.append(contato)


agenda = Agenda()

agenda.adicionar_contato("Gustavo")
agenda.adicionar_contato("Maria")
agenda.adicionar_contato("Tainá")
agenda.adicionar_contato("Luís")
agenda.adicionar_contato("Fernanda")
agenda.adicionar_contato("Clara")
agenda.adicionar_contato("Thamiris")
agenda.adicionar_contato("Bruna")
agenda.adicionar_contato("Larissa")
agenda.adicionar_contato("Gabrielly")
agenda.adicionar_contato("Letícia")
agenda.adicionar_contato("Carol")
agenda.adicionar_contato("Sarah")
agenda.adicionar_contato("Melissa")
agenda.adicionar_contato("Lara")

print("Contatos:", agenda.contatos)