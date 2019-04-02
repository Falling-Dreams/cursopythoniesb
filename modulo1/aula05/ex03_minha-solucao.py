#3. Cria uma funcao que receba um numero e um parametro booleano
#que e verdadeiro por default, se for verdadeiro retorne o 
#quadrado do numero se falso retorne a raiz do numero.
import math
def ex03_aula04(numero, condicao = True):
	if condicao:
		return numero * numero
	else:
		return math.sqrt(numero)

print(ex03_aula04(25, condicao = False))
