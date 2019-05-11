# -*- coding: UTF-8 -*-
"""Projeto Final - Curso Python IESB - Modulo 01

Após avaliar os itens solicitados e o dataset, concluí que a melhor estrutura de dados, neste caso, seria uma lista dos aplicativos 
em que cada índice é um aplicativo, descrito por um dicionário no qual, as chaves são os atributos do aplicativo e o valor são os dados
de cada aplicativo.
"""
# TODO aplicar PEP 8 ao codigo
# TODO criar uma funcao para responder ao item x
# D.R.Y. The acronym stands for the programming maxim “Don’t Repeat Yourself.”
# TODO utilizar format para apresentar um numero mais limpo para aqueles itens que envolvem operacoes matematicas

import manipula_dataset
import math

lista_aplicativos = []
chaves = ['App','Category','Rating','Reviews','Size','Installs','Type','Price','Content Rating','Genres','Last Updated','Current Ver',
'Android Ver']
# Retira os espacos em brancos e quebra de linhas separando os valores a cada virgula
with open('googleplaystore.csv', encoding='utf-8') as dataset:
	for linha_csv in dataset:
		valor_app = linha_csv.strip().split(',')	
		aplicativo = {k:v for (k,v) in zip(chaves, valor_app)}
		lista_aplicativos.append(aplicativo)

#'print(*lista_aplicativos,sep='\n')
def item1():
	#I) Quantos aplicativos existem? - OK
	print("\n\t\t\tI): " + "Existem", (len(lista_aplicativos)), "aplicativos" + "\n")

def item2():
	#II) Quais são as categorias? - OK
	categorias = [categoria["Category"] for categoria in lista_aplicativos]
	print("\n\t\t\tII): " + "As categorias são:")
	print("\t\t\t",*sorted(set(categorias)),sep='\n\t\t\t')

def item3():
	#III) Qual a maior avaliação? - OK*
	maior_avaliacao = max([float(avaliacao["Rating"]) for avaliacao in lista_aplicativos if ('19') not in avaliacao["Rating"]])
	app_avaliacao = {app["App"]: (float(app["Rating"])) for app in lista_aplicativos if float(app["Rating"]) >= maior_avaliacao}
	print("\n\t\t\tIII): " + "A maior avaliação é: ", maior_avaliacao,". " +  "E os aplicativos com essa avaliação são:",sep="")
	print("\t\t\t" ,*sorted(app_avaliacao.keys()),sep='\n\t\t\t')

def item4():
	#IV) Qual o aplicativo com maior tamanho? - OK
	maior_tamanho_app = max([int(tamanho["Size"]) for tamanho in lista_aplicativos])
	app_maior_tamanho = {app_tamanho["App"]: (int(app_tamanho["Size"])) for app_tamanho in lista_aplicativos if int(app_tamanho["Size"])
	 >= maior_tamanho_app}
	print("\n\t\t\tIV): " + "O maior tamanho de aplicativo é: ", (maior_tamanho_app//1000000), "M" ,". " 
	+  "E os aplicativos com esse tamanho são:",sep="")
	print("\t\t\t" ,*sorted(app_maior_tamanho),sep='\n\t\t\t')

def item5():
	#V) Qual é a categoria com mais aplicativos? - OK
	categorias = [categoria["Category"] for categoria in lista_aplicativos]
	qtd_app_categoria = dict()
	for categoria in categorias:
		qtd_app_categoria[categoria] = qtd_app_categoria.get(categoria, 0) + 1
	print("\n\t\t\tV): " + "A categoria com mais aplicativos é:", max(qtd_app_categoria, key=qtd_app_categoria.get))
	print("\n\t\t\tA quantidade de aplicativo por categoria é:")
	print("\t\t\t",*sorted(qtd_app_categoria.items()),sep='\n\t\t\t')

def item6():
	#VI) Qual é a média de avaliação em cada categoria? - OK
	categoria_avaliacao = [[categoria["Category"], (float(categoria["Rating"]))] for categoria in lista_aplicativos]
	avaliacao_soma = dict()
	qtd_avaliacao = dict()
	for categoria,avaliacao in categoria_avaliacao:
		if avaliacao != 0:
			qtd_avaliacao[categoria] = (qtd_avaliacao.get(categoria, 0) + 1)
		avaliacao_soma[categoria] = (avaliacao_soma.get(categoria, 0) + avaliacao)
	media_avaliacao = [i/j for (i,j) in zip(avaliacao_soma.values(), qtd_avaliacao.values())]
	media_avaliacao_categoria = list(zip(qtd_avaliacao.keys(),media_avaliacao))
	print("\n\t\t\tVI): A média de avaliação em cada categoria é:")
	print("\t\t\t",*media_avaliacao_categoria,sep='\n\t\t\t')

def item7():
	#VII) Daqueles com avaliação maior que 4, qual o conteudo indicativo com mais aplicativos? - OK
	app_audiencia = [audiencia["Content Rating"] for audiencia in lista_aplicativos if float(audiencia["Rating"]) >= 4]
	qtd_app_audiencia = dict()
	for audiencia in app_audiencia:
		qtd_app_audiencia[audiencia] = (qtd_app_audiencia.get(audiencia, 0) + 1)
	print("\n\t\t\tVII): " + "O conteudo indicativo com mais aplicativos é:", max(qtd_app_audiencia, key=qtd_app_audiencia.get))
	print("\t\t\tA quantidade de aplicativo por conteúdo indicativo é:" ,*sorted(qtd_app_audiencia.items()),sep='\n\t\t\t')

def item8():
	#VIII) Qual o desvio padrão da coluna de avaliações? - valor do dp esta correto
	avaliacao = [float(avaliacao["Rating"]) for avaliacao in lista_aplicativos if float(avaliacao["Rating"]) > 0]
	media = (sum(avaliacao))/len(avaliacao)
	quadrado_distancia = [(n - media)**2 for n in avaliacao]
	desvio_padrao = math.sqrt((sum(quadrado_distancia))/len(avaliacao))
	print("\n\t\t\tVIII): O desvio padrão é:", desvio_padrao)

def item9():	
	#IX) Quantos aplicativos foram atualizados em janeiro de 2018? - OK
	app_atualizacao = [(atualizacao["App"], str(atualizacao["Last Updated"])) for atualizacao in lista_aplicativos]
	atualizacao = [(x,y) for (x,y) in app_atualizacao if ("January") in y and ("2018") in y]
	print("\n\t\t\tIX): " + "Foram atualizados", len(set(atualizacao)), "aplicativos")

def item10():
	#X) Suponha que você irá utilizar essa planilha em uma solução de IA. Transforme todas as colunas, com exceção do nome
	#do aplicativo, em valores numéricos.
	print("\t\t\tX): Em construção...")