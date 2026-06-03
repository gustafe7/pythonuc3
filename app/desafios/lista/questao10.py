numeros = []

for numero in range(5):
    numero = int(input("Digite 5 números: "))
    numeros.append(numero)

soma = sum(numeros)
print("Numeros Digitados", numeros)
print("Soma", soma)
