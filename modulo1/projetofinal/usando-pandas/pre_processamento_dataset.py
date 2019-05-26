# -*- coding: utf-8 -*-

'''Projeto Final - Curso Python IESB - Modulo 01 - Módulo Para Processar Dataset
Abordagem utilizando pandas e numpy

'''

import pandas as pd
import numpy as np
from sklearn.preprocessing import Imputer

df = pd.read_csv('/media/veracrypt64/1Python/@Curso_Python_IESB/cursopythoniesb/modulo1/projetofinal/usando-pandas/googleplaystore.csv')

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
	
	print("A quantidade total de aplicativos é:",df['App'].count(),"\n")

def item2():

	'''	O aplicativo com a categoria '1.9' foi substituido por aquela de maior
	frequência: 'FAMILY'
	
	Parameters
	----------
	void

	Returns
	-------
	void

	Raises
	------

	'''
	
	df['Category'].value_counts().idxmax()
	df.loc[df.Category == '1.9', 'Category'] = 'FAMILY'
	print("As categorias são:")
	print(*sorted(set(df.Category)),sep=', ')

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
	
	df['Rating'].value_counts().idxmax()
	df.loc[df.Rating == 19.0, 'Rating'] = 4.4
	app_max_avaliacao = df['Rating'].max()
	print(*sorted(list(df.loc[df.Rating == app_max_avaliacao, str('App')])),sep='\n')

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

	max_size = (df['Size'][df.Size != 'Varies with device']).max()
	print(*sorted(set(list(df.loc[df.Size == max_size, 'App']))),sep='\n')

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
	
	print(df['Category'].value_counts().idxmax())

def item6():
	'''Printa a media de avaliacao em cada categoria. 

	Substituo os valores 'NaN' com o valor da media dos valores não nulos
	da coluna Rating

	Parameters
	----------
	void

	Returns
	-------
	void

	Raises
	------

	'''
	
	media_categoria = df['Rating'].mean() #Tratamento dos valores 'NaN'
	df['Rating'] = df['Rating'].fillna(media_categoria)
	print(df.groupby(['Category']).mean())

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

	df_ct_rt = df.groupby([df.Rating > 4.0, 'Content Rating'])['App'].count()
	print("Para aqueles aplicativos com nota maior do que 4, O conteúdo \
	 	indicativo com mais aplicativos é:", dict(df_ct_rt[True]),sep='\n')

def item8():
	'''Printa o desvio padrao da coluna "Rating". 
	
	Parameters
	----------
	void

	Returns
	-------
	void

	Raises
	------

	'''

	print("O desvio padrão é: ",df.loc[:, 'Rating'].std())

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
	
	df1 = df[df['Last Updated'].str.contains("January") & df['Last Updated'].str.contains("2018")] 
	print("Os seguintes aplicativos foram atualizados em janeiro de 2018:"
		, *sorted(set(df1['App'])),sep='\n')

#X) Suponha que você irá utilizar essa planilha em uma solução de IA.
#Transforme todas as colunas, com exceção do nome do aplicativo, em valores numéricos.