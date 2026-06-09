import subprocess

#arquivo = open("app\exemplos\dados.txt","r")
#conteudo = arquivo.read()
#print(conteudo)
#arquivo.close()

with open("app/exemplos/dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

try:
    with open("app/exemplos/dados.txt", "r") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
except FileNotFoundError:
    print("Arquivo não encontrado")

#Sobrescrita
with open("app/exemplos/dados.txt", "w") as arquivo:
    conteudo = arquivo.write("Bem vindo ao python")

#Adicionar novo conteúdo
with open("app/exemplos/dados.txt", "a") as arquivo:
    arquivo.write(" Usuario logado\n")

#abrindo em um programa da minha escolha
subprocess.Popen(["code","app/exemplos/dados.txt"])