#1. Crie uma funcao que calcule o numero primo seguinte ao numero informado.
#Parcialmente baseada na resposta abaixo:
	#https://stackoverflow.com/questions/27348983/trying-to-find-the-next-prime-number
	#resposta do usuario: Mohanlal

import sys
def eh_primo(a):
    return all(a % i for i in xrange(2, a))
    
def primo_proximo(num):
	prox = 0
	for q in xrange(num + 1, sys.maxsize):		
		if eh_primo(q):
			return q
			break
		prox +=1

print(primo_proximo(317))
