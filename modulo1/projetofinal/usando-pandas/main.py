# -*- coding: UTF-8 -*-
"""Projeto Final - Curso Python IESB - Modulo 01 - Main

Arquivo que exibe na tela as respostas aos itens do projeto final (utilizando a abordagem pandas e numpy).
"""

import pre_processamento_dataset

def main():
	opcao = -1
	while opcao != 0:
		try:
			opcao = int(input('''
			\tProjeto Final - Curso Python IESB - Modulo 01.\n\n\t\t\tDigite o número equivalente ao item que se deseja a resposta:\n			
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
			0 -  Para sair
			Escolha: '''))
			if opcao == 0:
				exit()
			elif opcao == 1:
				pre_processamento_dataset.item1()
			elif opcao == 2:
				pre_processamento_dataset.item2()
			elif opcao == 3:
				pre_processamento_dataset.item3()
			elif opcao == 4:
				pre_processamento_dataset.item4()
			elif opcao == 5:
				pre_processamento_dataset.item5()
			elif opcao == 6:
				pre_processamento_dataset.item6()
			elif opcao == 7:
				pre_processamento_dataset.item7()
			elif opcao == 8:
				pre_processamento_dataset.item8()
			elif opcao == 9:
				pre_processamento_dataset.item9()
			elif opcao == 10:
				pre_processamento_dataset.item10()					
			else:
				print("Este número não está nas alternativas, tente novamente.\n")	
		except ValueError:
			print("Isso não é um número, tente novamente.\n")
if __name__ == '__main__':
	main()