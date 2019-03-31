#2. Receba o nome e sobenomes de uma pessoa e retorne o nome dele em uma
#passagem de aviao. Exemplo: Rodrigo Guimaraes Araujo deve retornar 
#Araujo Rodrigo.
s = "Kevin de Santana Araujo"
nome_sobrenome_aviao = ''
nome_sobrenome = s.rsplit(" ")
nome_sobrenome.reverse()
for i in range(len(nome_sobrenome)):
	nome_sobrenome_aviao = nome_sobrenome[0], nome_sobrenome[len(nome_sobrenome) - 1]
print(nome_sobrenome_aviao)