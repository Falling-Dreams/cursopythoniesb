# -*- coding: UTF-8 -*-
# TODO menu para escolha das opcoes
# TODO ao selecionar uma opcao, volar ao menu de opcoes (escolher mais de um item sem precisar executar o programa mais de uma vez)
# TODO constuir menu

import projeto_final
import manipula_dataset

def main():
	opcao = -2
	while opcao != 0:
		try:
			opcao = int(input('''
			\tProjeto Final - Curso Python IESB - Modulo 01.\n\n\t\t\tDigite o número equivalente ao item que se deseja a resposta:\n
			0  -  Preparar o dataset (executar apenas uma vez)
			1  -  Quantidade de aplicativos
			2  -  Categorias
			3  -  Maior avaliação
			4  -  Aplicativo com maior tamanho
			5  -  Categoria com mais aplicativos
			6  -  Media de avaliação por categoria
			7  -  Conteúdo indicativo com mais aplicativos maiores do que 4
			8  -  Desvio padrão das avaliações
			9  -  Quantidade de aplicativos atualizados em janeiro de 2018
			10 -  Colunas do dataset em valores númericos
			-1 -  Para sair
			Escolha: '''))
			if opcao == 0:
				manipula_dataset.limpar_dataset()
			elif opcao == 1:
				projeto_final.item1()
			elif opcao == 2:
				projeto_final.item2()
			elif opcao == 3:
				projeto_final.item3()
			elif opcao == 4:
				projeto_final.item4()
			elif opcao == 5:
				projeto_final.item5()
			elif opcao == 6:
				projeto_final.item6()
			elif opcao == 7:
				projeto_final.item7()
			elif opcao == 8:
				projeto_final.item8()
			elif opcao == 9:
				projeto_final.item9()
			elif opcao == 10:
				projeto_final.item10()
			elif opcao == -1:
				exit()		
			else:
				print("Este número não está nas alternativas, tente novamente." + "\n")	
		except ValueError:
			print("Isso não é um número, tente novamente.\n")
if __name__ == '__main__':
	main()