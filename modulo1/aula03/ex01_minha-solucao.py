#1. Dado uma lista, informa a soma de todos os valores contidos nela.
#numsum = sum(list(numbers))
#return [x for x in testList if (isinstance(x, int) or isinstance(x, long)) 
#and not isinstance(x, bool)]
#from decimal import Decimal

lista = ["Joao", 18, "Python", "Maria", 20, "C", -10]
n = 0
for element in lista:	
	n = [x for x in lista if (isinstance(x, int) or isinstance(x, long))]
	x = sum(n)
	#and not isinstance(x, bool)]
	#n =+ element
print(x)