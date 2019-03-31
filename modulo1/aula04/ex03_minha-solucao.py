#3. Receba varios nomes em sequencia e informa as primeiras letras 
#em uma unica string. Exemplo: IESB nota cinco no MEC deve retornar 
#IncnM
s = "Abacate doce batido no liquidificador"
t = ''
lista = s.split(" ")
iniciais = [item[0] for item in lista]
for n in range(len(iniciais)):
	t += iniciais[n]
print(t)

