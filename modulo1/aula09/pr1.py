#dado o diagrama abaixo, crie as classes indicadas

class Funcionario:
	def __init__(self, nome: str, data_nasc: str, salario: float = 0):
		self.nome = nome
		self.data_nasc = data_nasc
		self.__salario = salario

	def informar_salario(self):
		print(self.__salario)

	def reajuste_salario(self, salario, valor: float):
		self.__salario += valor

class Programador(Funcionario):
	def __init__(self, nome: str, data_nasc: str, linguagem: str):
		super().__init__(nome, data_nasc)

	def informar_linguagens(self):
		return self.linguagem

p = Programador('Ze', '01/12/2145', 'Python')
#p.reajuste_salario

