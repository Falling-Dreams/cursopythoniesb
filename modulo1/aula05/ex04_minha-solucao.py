"""Calcula as raizes de uma equacao do segundo grau no formato ax2+bx+c = 0"""
#TODO: tratar casos em que aconteca divisao por zero
import math

def equacao_segundo_grau(a, b, c):
	det = b*b - (4 * (a) * (c))
	raiz_det = math.sqrt(det)
	
	if det < 0 : 
		print("Nao existem raizes reais")
		
	elif det == 0 :
		raiz = (-b + raiz_det / (2*a))
		print("A equacao possui uma raiz real: " + raiz);
		
	else :
			raiz1 = (-b + raiz_det / (2*a))
			raiz2 = (-b - raiz_det / (2*a))
			raizes = raiz1, raiz2
			return raizes;



print(equacao_segundo_grau(1,7,8))