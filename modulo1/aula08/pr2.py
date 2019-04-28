#crie a classe conta corrente e implemente os metodos necessarios
#para sacar, depositar e ver o saldo, de forma que o atributo 
#saldo seja privado

class ContaCorrente:
	def __init__(self, nome, saldo=0):
		self.nome = nome
		self.__saldo = saldo

	def sacar(self, valor):
		if 0 < valor <= self.__saldo:
			self.__saldo -= valor

	def depositar(conta, valor, saldo):
		self.conta = saldo - valor

	def saldo(self):
		print(self.__saldo)
