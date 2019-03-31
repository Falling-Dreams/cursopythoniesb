#crie uma funcao que receba duas palavras e um separador, que por padrao
#e um espaco, e retorne as palavras separadas pelo separador em uma string
#retornar uma palavra

#def concat(palavra1,palavra2,separador=""):
#return separador.join([palavra1, palavra2])

def formatacao(str1, str2, sep=" "):
	return str1 + sep+ str2

str1 = "abacate"
str2 = "doce"
print(formatacao(str1,str2, sep = "5455"))