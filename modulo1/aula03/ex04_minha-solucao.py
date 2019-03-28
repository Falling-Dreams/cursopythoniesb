#4. Ao informar um numero, responda se o mesmo e primo.
#n = [x for x in range(2, 20) if all(x % y != 0 for y in range(2, x))]
lista = ["Joao", 18, "Python", "Maria", 20, "C", -10, 2, 8, 5, 7]

#Retorna lista de numeros a partir de uma lista mista
for a in lista:
	n = [x for x in lista if (isinstance(x, int))]

for b in n:
	if (b % b != 0):
		for c in range(2, b):		
			break
	else:
		print("Numeros primos: ", b)
		



