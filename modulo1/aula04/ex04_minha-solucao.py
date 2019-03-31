#4. Ao informar uma frase, seu programa deve mostrar, 
#quantas palavras tem a frase, - OK
#quantas letras tem a frase e a - OK
#media de letras por palavra - 
texto = 'Space: the final frontier.These are the voyages of the \
starship Enterprise.Its continuing mission: to explore strange \
new worlds. To seek out new life and new civilizations.To boldly \
go where no one has gone before! '
b = ''
lista_qtd_plv_frases = list()
qtd_ltr_frases = 0
md_ltr_plv = 0
lista_qtd_ltr_frases = list()
lista_md_ltr_plv = list()
frases = texto.split(".")

for a in range(len(frases)):
	b = frases[a]
	qtd_plv = (b.count(" ") + 1)
	lista_qtd_plv_frases.append(qtd_plv)
	qtd_ltr_frases = len(b) - qtd_plv
	lista_qtd_ltr_frases.append(qtd_ltr_frases)
	md_ltr_plv = qtd_ltr_frases/qtd_plv
	lista_md_ltr_plv.append(md_ltr_plv)

print("Quantidade de palavras nas frases: ", lista_qtd_plv_frases)
print("Quantidade de letras por fraase: ", lista_qtd_ltr_frases)
print("Media de letras por palavra: " ,lista_md_ltr_plv)
