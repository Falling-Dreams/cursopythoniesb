# -*- coding: UTF-8 -*-
"""Projeto Final - Curso Python IESB - Modulo 01 - Item x

Executar apenas uma vez!

"""
def valor_numerico():
	'''Transforma as colunas do dataset googleplaystore.csv em valores numericos.

	Somando o valor ascii dos caracteres de cada item da coluna.

	Parameters
	----------
	void

	Returns
	-------
	void

	Raises
	------

	'''
	import csv
		
	linhas_csv = []
	try:
		with open('googleplaystore.csv') as csvDataFile:	
			csvReader = csv.reader(csvDataFile)		
			for coluna_csv in csvReader:
				
				category = (sum([ord(c) for c in coluna_csv.pop(1)]))
				coluna_csv.insert(1, category)
				tipo = (sum([ord(c) for c in coluna_csv.pop(6)]))
				coluna_csv.insert(6, tipo)
				content_rating = (sum([ord(c) for c in coluna_csv.pop(8)]))
				coluna_csv.insert(8, content_rating)
				genres = (sum([ord(c) for c in coluna_csv.pop(9)]))
				coluna_csv.insert(9, genres)
				last_updated = (sum([ord(c) for c in coluna_csv.pop(10)]))
				coluna_csv.insert(10, last_updated)
				current_version = (sum([ord(c) for c in coluna_csv.pop(11)]))
				coluna_csv.insert(11, current_version)
				#android_version = (sum([ord(c) for c in coluna_csv.pop(-1)]))
				#coluna_csv.insert(-1, android_version)			
				linhas_csv.append(coluna_csv)
			
			with open('googleplaystore.csv', mode='w') as csvDataFileWrite:		
				writer = csv.writer(csvDataFileWrite)
				writer.writerows(linhas_csv)
			
	except IOError:
		print("Erro: Arquivo nao encontrado ou nao e possivel ler o arquivo")
	else:
		print("\t\t\tColunas do dataset foram modificadas para valores numericos")
