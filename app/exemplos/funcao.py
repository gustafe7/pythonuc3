def soma(num1,num2):
    total = num1+num2
    return total

def exibirmsg():
    print("Isso é uma função")

def exibirmsg2():
    return "Isso é uma função 2"

#temp = soma()
print(soma(5,15))

print(exibirmsg2)
exibirmsg2()

def subtracao(num1,num2):
    total = num1 - num2
    return total

print(subtracao(10,5))

def multiplicacao(num1,num2):
    total = num1 * num2
    return total

print(multiplicacao(10,5))

def test(senha):
    if senha == "123456":
        print("senha correta")
    else:
        print("senha incorreta")

test(input("Digite a sua senha: "))

def contnum():
    for i in range(5):
        print(i)

contnum()

def contnum(num):
    for i in range(num):
        print(i)

contnum(50)

def countwhile():
    count=0
    while count<3:
        print(count)
        count+=1

countwhile()