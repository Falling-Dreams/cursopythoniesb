#3. Dada uma lista, avalie se algum dos numeros e multiplo de 7.
lista = ["Joao", 18, "Python", "Maria", 20, "C", -10, 2, 8, 5, 7]
impares = []
n = 0
s = ''
n = ''
t = ''
#Retorna uma lista n com os numeros de uma lista mista
for element in lista:
	n = [x for x in lista if (isinstance(x, int))]
#Itera sobre a lista retornada, verificando se ha multiplo de 7
#for a in n:
#	if (a % 7 == 0):
#		s = "Sim"
		
#	elif (a % 7 != 0) :
#		n = "Nao"

#	elif (a % 7 == 0 and a % 7 != 0):
#		t = s + "/" +  n

#print("Existem multiplos de 7: " + s + " " + n + " " + t)