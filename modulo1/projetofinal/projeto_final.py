# -*- coding: UTF-8 -*-
"""Projeto Final - Curso Python IESB - Modulo 01

Após avaliar os itens solicitados e o dataset, concluí que a melhor estrutura de dados, neste caso, seria uma lista dos aplicativos 
em que cada índice é um aplicativo, descrito por um dicionário no qual, as chaves são os atributos do aplicativo e o valor são os dados
de cada aplicativo.
"""

import math
import processar_dataset
import item_x

lista_aplicativos = []
chaves = ['App','Category','Rating','Reviews','Size','Installs','Type','Price','Content Rating','Genres','Last Updated','Current Ver',
'Android Ver']
# Retira os espacos em brancos e quebra de linhas separando os valores a cada virgula
with open('googleplaystore.csv', encoding='utf-8') as dataset:
	for linha_csv in dataset:
		valor_app = linha_csv.strip().split(',')	
		aplicativo = {k:v for (k,v) in zip(chaves, valor_app)}
		lista_aplicativos.append(aplicativo)

def pre_processamento():
	'''Executa a limpeza do dataset.
	
	Parameters
	----------
	void

	Returns
	-------
	void

	Raises
	------

	'''
	
	processar_dataset.limpar_dataset()

def item1():
	'''Printa a quantidade de aplicativos.
	
	Parameters
	----------
	void

	Returns
	-------
	void

	Raises
	------

	'''
	
	print("\n\t\t\tI): " + "Existem", (len(lista_aplicativos)), "aplicativos" + "\n")

def item2():
	'''Printa as categorias unicas.

	A partir de um set da coluna "Category".

	Parameters
	----------
	void

	Returns
	-------
	void

	Raises
	------

	'''
	
	categorias = [categoria["Category"] for categoria in lista_aplicativos]
	print("\n\t\t\tII): " + "As categorias são:")
	print("\t\t\t",*sorted(set(categorias)),sep='\n\t\t\t')

def item3():
	'''Printa a maior avaliacao para um aplicativo, e os aplicativos com essa avaliacao 

	Ignora-se o aplicativo "Life Made WI-Fi Touchscreen Photo Frame" com avaliacao (errada) de 19.

	Parameters
	----------
	void

	Returns
	-------
	void

	Raises
	------

	'''
	
	maior_avaliacao = max([float(avaliacao["Rating"]) for avaliacao in lista_aplicativos if ('19') not in avaliacao["Rating"]])
	app_avaliacao = {app["App"]: (float(app["Rating"])) for app in lista_aplicativos if float(app["Rating"]) >= maior_avaliacao}
	print("\n\t\t\tIII): " + "A maior avaliação é: ", maior_avaliacao,". " +  "E os aplicativos com essa avaliação são:",sep="")
	print("\t\t\t" ,*sorted(app_avaliacao.keys()),sep='\n\t\t\t')

def item4():
	'''Printa o maior tamanho de aplicativo, e os aplicativos com esse tamanho.

	Recupera-se aqueles aplicativos com maior tamanho em bytes (100000000) e converte-se no print de volta para Mb.

	Parameters
	----------
	void

	Returns
	-------
	void

	Raises
	------

	'''

	maior_tamanho_app = max([int(tamanho["Size"]) for tamanho in lista_aplicativos])
	app_maior_tamanho = {app_tamanho["App"]: (int(app_tamanho["Size"])) for app_tamanho in lista_aplicativos if int(app_tamanho["Size"])
	 >= maior_tamanho_app}
	print("\n\t\t\tIV): " + "O maior tamanho de aplicativo é: ", (maior_tamanho_app//1000000), "Mb" ,". " 
	+  "E os aplicativos com esse tamanho são:",sep="")
	print("\t\t\t" ,*sorted(app_maior_tamanho),sep='\n\t\t\t')

def item5():
	'''Printa a categoria com mais aplicativos e a quantidade de aplicativos em cada categoria.

	Com o get conta-se quantas vezes cada categoria aparece na coluna "Category".

	Parameters
	----------
	void

	Returns
	-------
	void

	Raises
	------

	'''

	categorias = [categoria["Category"] for categoria in lista_aplicativos]
	qtd_app_categoria = dict()
	for categoria in categorias:
		qtd_app_categoria[categoria] = qtd_app_categoria.get(categoria, 0) + 1
	print("\n\t\t\tV): " + "A categoria com mais aplicativos é:", max(qtd_app_categoria, key=qtd_app_categoria.get))
	print("\n\t\t\tA quantidade de aplicativo por categoria é:")
	print("\t\t\t",*sorted(qtd_app_categoria.items()),sep='\n\t\t\t')

def item6():
	'''Printa a media de avaliacao em cada categoria. 

	Os valores 'NaN' foram trocados por zero (0.0), assim, para obter a media soma-se toda a coluna "Rating" e entao a soma total de 
	cada categoria e dividida pela quantidade total de avaliacoes diferentes de 0 de cada categoria.

	Parameters
	----------
	void

	Returns
	-------
	void

	Raises
	------

	'''

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
	'''Printa o conteudo indicativo com mais aplicativos, e a quantidade de aplicativos por conteudo indicativo. 

	Conta-se com get quantas vezes cada conteudo indicativo aparece na coluna "Content Rating" com avaliacao maior do que 4.

	Parameters
	----------
	void

	Returns
	-------
	void

	Raises
	------

	'''
	app_audiencia = [audiencia["Content Rating"] for audiencia in lista_aplicativos if float(audiencia["Rating"]) >= 4]
	qtd_app_audiencia = dict()
	for audiencia in app_audiencia:
		qtd_app_audiencia[audiencia] = (qtd_app_audiencia.get(audiencia, 0) + 1)
	print("\n\t\t\tVII): " + "O conteudo indicativo com mais aplicativos é:", max(qtd_app_audiencia, key=qtd_app_audiencia.get))
	print("\t\t\tA quantidade de aplicativo por conteúdo indicativo é:" ,*sorted(qtd_app_audiencia.items()),sep='\n\t\t\t')

def item8():
	'''Printa o desvio padrao da coluna "Rating". 

	Aplica-se a formula do desvio padrao em uma populacao:
		dp = sqrt((somatorio de 1 a tamanho da populacao(amostra - media)^2)/tamanho populacao).

	Parameters
	----------
	void

	Returns
	-------
	void

	Raises
	------

	'''

	avaliacao = [float(avaliacao["Rating"]) for avaliacao in lista_aplicativos if float(avaliacao["Rating"]) > 0]
	media = (sum(avaliacao))/len(avaliacao)
	quadrado_distancia = [(n - media)**2 for n in avaliacao]
	desvio_padrao = math.sqrt((sum(quadrado_distancia))/len(avaliacao))
	print("\n\t\t\tVIII): O desvio padrão é:", desvio_padrao)

def item9():
	'''Printa a quantidade de aplicativos atualizados em janeiro de 2018. 

	Conta-se a quantidade de aplicativos na coluna "Last Updated" que contem a substring "January" e "2018"

	Parameters
	----------
	void

	Returns
	-------
	void

	Raises
	------

	'''
	
	app_atualizacao = [(atualizacao["App"], str(atualizacao["Last Updated"])) for atualizacao in lista_aplicativos]
	atualizacao = [(x,y) for (x,y) in app_atualizacao if ("January") in y and ("2018") in y]
	print("\n\t\t\tIX): " + "Foram atualizados", len(set(atualizacao)), "aplicativos")

def item10():
	'''Resposta ao item ix do projeto final. 

	Como foi feito.

	Parameters
	----------
	void

	Returns
	-------
	void

	Raises
	------

	'''
	item_x.valor_numerico()