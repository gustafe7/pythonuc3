def impares_sem_multiplos_de_7(inicio, fim):
    for i in range(inicio, fim + 1):

        # pula números pares
        if i % 2 == 0:
            continue

        # pula múltiplos de 7
        if i % 7 == 0:
            continue

        print(i)

impares_sem_multiplos_de_7(1, 50)