def soma_valores():
    soma = 0

    while True:
        valor = int(input("Digite um número (0 para sair): "))

        if valor == 0:
            break

        soma += valor

    return soma
print("Soma total: ", soma_valores())