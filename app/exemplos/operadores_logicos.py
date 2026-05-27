"""
op1     logico  op2
operando1  >  operando2
operando1  >=  operando2
operando1  <  operando2
operando1  <=  operando2
operando1  ==  operando2
operando1  !=  operando2
operação1    not    operação2
operação1    and    operação2
operação1    or    operação2
Reseultados valor True/False
"""

op1 = input("digite uma informação: ")
op2 = input("Digite outra informação: ")

print(op1 > op2)
print(op1 >= op2)
print(op1 < op2)
print(op1 <= op2)
print(op1 == op2)
print(op1 != op2)
print(op1 and op2)
print(op1 or op2)
print(op1>op2 and op1==op2) # duas operações verd(V)
print(op1>op2 or op1==op2) # uma operação verd(V)