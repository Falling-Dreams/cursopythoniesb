"""
Crie um programa que dados os valores a, b, e c de uma 
função de segundo grau, as raizes da equação. (y = a*x² + b*x + c)
"""

a = int(input("Valor a: "))
b = int(input("Valor b: "))
c = int(input("Valor c: "))

delta = b**2 - 4*a*c

if delta:
    print("x1:", (-b + delta**.5)/(2*a))
    print("x2:", (-b - delta**.5)/(2*a))

