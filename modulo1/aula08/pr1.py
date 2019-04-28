#Desenvolva a classe Calculadora, que pode fazer operacoes de 
#soma, multiplicacao, subtracao e divisao entre n numeros

class Calculadora:
	def __init__(self, *numeros):
		self.numeros = numeros
		
	def soma(self):
		return sum(self.numeros)

calculadora = Calculadora(5, 3, 10, 565, 655)
print(calculadora.soma())