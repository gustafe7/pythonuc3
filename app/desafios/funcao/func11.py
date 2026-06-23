def login():
    senha_correta = "python123"
    tentativas = 0

    while tentativas < 3:
        senha = input("Digite a senha: ")

        if senha == senha_correta:
            print("Login bem-sucedido!")
            return

        else:
            print("Senha incorreta.")
            tentativas += 1

    print("Número de tentativas excedido. Acesso bloqueado.")

login()