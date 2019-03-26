#2. A partir de uma lista, construa outra deixando apenas os valores impares

lista = ["Joao", 18, "Python", "Maria", 20, "C", -10, 2, 8, 5]
impares = []
n = 0
#Retorna uma lista n com os numeros de uma lista mista
for element in lista:
	n = [x for x in lista if (isinstance(x, int))]
#Itera sobre a lista retornada, retornando os numeros impares dessa lista 
#e anexando-os a uma nova lista
for a in n:
	if (a % 2 != 0):
		impares.append(a)
print(impares)			


		