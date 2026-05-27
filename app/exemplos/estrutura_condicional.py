idade = int(input("Digite a sua idade: "))
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade!")

senha = 123456
int(input("Digite a sua senha: "))

if senha == 123456:
    print("Aceso liberado")
else:
    print("Acesso negado")

nota = int(input("Digite a sua nota: ")) 

if nota > 8:
    print("Excelente!")
elif nota >= 7:
    print("Aprovado!")
elif nota >= 5:
    print("Média!")
else:
    print("Reprovado!")
