for numero in range(5):
    print(numero)

for numero in range(0,11,2):
    print(numero)

for numero in range(1,10):
    print(f"6 x {numero} = {6*numero}")

contador = 0
while contador < 5:
    print(contador)
    contador += 1 

for numero in range(0,11):
    if numero == 5:
        break
    print(numero)

for numero in range(10):
    if numero == 5:
        continue
    print(numero)