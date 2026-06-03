nome = 'Gustavo'
listanomes = ["Bruno", "Gustavo", "Carol", "Bruna", "Clara"]
print(nome)
print(listanomes)
print(len(listanomes)) #Conta quantos elementos existem
listanomes.append("Ana") # adiciona um elemento ao final da lista
print(listanomes)
print(listanomes.index("Clara"))
nova_lista = [1,4,"kyo","yori"]
print(nova_lista)
#nova_lista.remove(4) # remove elementos de dentro das listas
#nova_lista.remove("kyo") # remove elementos de dentro das listas
nova_lista.reverse() # faz a lista ao inverso
print(nova_lista)
nova_lista.append([10,56,9]) #adiciona uma lista dentro de outra lista
print(nova_lista)

mercado = ["arroz", "feijao", "carne", "ovo", "biscoito"]
print("arroz" in mercado) # arroz está na lista mercado
print(mercado[0]) # retorna o primeiro item da lista
print(mercado[4]) # retorna o último item da lista
print("biscoito" not in mercado)
print(mercado[-1])
print(mercado[-5])
numeros = [5,3,1,4,2]
print(numeros.sort()) # Ordenando crescente
numeros.sort(everse=True) # Ordenando decrescente
listanumeros2 = numeros.copy() #copia lista

#fatia lista
n1 = numeros[0]
n2 = numeros[1]
#ou
print(numeros[1:5])

print(numeros.clear) #remove todos os itens da lista