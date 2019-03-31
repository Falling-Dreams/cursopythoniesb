#4. Ao informar um numero, responda se o mesmo e primo.
#n = [x for x in range(2, 20) if all(x % y != 0 for y in range(2, x))]
lista = ["Joao", 18, "Python", "Maria", 20, "C", -10, 2, 8, 5, 7]
x = 0
lista_primos = list()
#Retorna lista de numeros e a soma total dos seus elementos,
#a partir de uma lista mista
for a in lista:
	n = [x for x in lista if (isinstance(x, int))]
	x = sum(n)

for b in n:
	for c in range(1, x):		
		if(all(abs(b) % i for i in range(2, b))):
			lista_primos.append(b)
			break
print(lista_primos)

				