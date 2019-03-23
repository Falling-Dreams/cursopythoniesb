"""
Crie uma calculadora capaz de fazer as operações 
de soma, subtração, multiplicação, divisião e potência entre dois números.
"""

a = int(input("Valor a: "))
op = input("Operação: ")
b = int(input("Valor b: "))

if op == '+':
    print("Soma:", a+b)
elif op == '-':
    print("Subtração:", a-b)
elif op == '*':
    print("Multiplicação:", a*b)
elif op == '/':
    print("Divisião:", a/b)    
elif op == '**':
    print("Potência:", a**b)    
else:
    print("Operação inválida!")
