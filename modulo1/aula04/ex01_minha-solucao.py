#1. Receba um string e retorne ela ao contrario
s = "Abacate doce"
t = ''
lista = list()
for a in s:
	lista.append(a)
lista.reverse()
for b in range(len(lista)):
	t += lista[b]
	
print(t)
