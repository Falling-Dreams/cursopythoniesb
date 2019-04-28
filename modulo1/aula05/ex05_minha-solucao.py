#5. Crie uma funcao que recebe infinitos parametros e retorne 
#o maior e o menor entre eles.
def ex05_aula05(*numero):
	lista = list()
	minimo = 0
	maximo = 0		
	for n in numero:
		lista.append(n)
	minimo = lista.pop(0)	
	maximo = lista.pop()
	return minimo,maximo

print(ex05_aula05(545,998,2335,14,236,11,32))

