#1. Crie uma funcao que calcule o numero primo seguinte ao numero informado.
#all(numero % i for i in range(2, numero)) true se for primo
#def proximo_primo(numero):	
	#checa_proximo_primo = False
	#for p in range(numero):
		#for i in range(2, p):
			#if p % i == 0:
				#break
			#else:
				#return p
	#return None
#print(proximo_primo(13))

#Fonte:
	#https://stackoverflow.com/questions/27348983/trying-to-find-the-next-prime-number
	#resposta do usuario: Mohanlal
def proximo_primo(numero):
    for i in range(2, numero):
        if numero % i == 0:
            return False
        sqr = i * i
        if sqr > numero:
           break
    return True

numero = int(input("Infome o numero: ")) + 1
while(True):
    res = proximo_primo(numero)
    if res:
        print("O proximo primo eh: ",numero)
        break
    numero += 1

