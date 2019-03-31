#6. Dada uma palavra remova todas as consoantes se o tamanho da palavra 
#for par e todas as vogais se o tamanho da palavra for impar.
s = 'Pythoon'
lista_temp = [a for a in s]
palavra_par = ''
palavra_impar = ''
#lista = ['par' if (len(s) % 2 == 0) else 'impar' for x in range(len(s))]
for n in range(len(lista_temp)):
	if (n % 2 != 0):
		lista_impar = [b for b in lista_temp if b in("A", "a", "E", "e", "I", "i", "O", "o", "U", "u")]
		palavra_impar = lista_impar
	else:
		lista_par = [b for b in lista_temp if b not in("A", "a", "E", "e", "I", "i", "O", "o", "U", "u")]
		palavra_par = lista_par

print(palavra_impar)
print(palavra_par)

#par = False
#impar = False
#count = 0
#for letra in s:
#	count += 1
#if (count % 2 == 0):
#	par = True
#else:
#	impar = True
