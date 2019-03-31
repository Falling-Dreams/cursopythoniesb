#crie uma funcao que dada uma lista
#, retorne duas listas, um dos pares e outra dos impares

def devolve_par_e_impar(lista1):
	lista2 = []
	lista3 = []
	for a in lista1:
		if a%2 == 0:
			lista2.append(a)
		else:
			lista3.append(a)
	return lista2, lista3

lista1 = [1,2,3,4,5,6,7]
print(devolve_par_e_impar(lista1))
