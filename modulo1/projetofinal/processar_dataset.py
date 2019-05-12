def limpar_dataset():
	'''Funcao auxiliar para o projeto final.

	Limpa as colunas App,Rating,Size,Installs e Last Updated do dataset googleplaystore.csv.

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
			next(csvDataFile)
			for coluna_csv in csvReader:
				app = (coluna_csv.pop(0)).replace(',', '').replace('.', '').strip()		
				coluna_csv.insert(0, app)
				rating = (coluna_csv.pop(2)).replace('NaN', '0').strip()
				coluna_csv.insert(2, rating)		
				size = (coluna_csv.pop(4)).replace('.', '').replace('k', '000').replace('M', '000000').replace('Varies with device', '0')\
				.replace('+', '').replace(',','')\
				.strip()
				coluna_csv.insert(4, size)		
				installs = (coluna_csv.pop(5)).replace(',', '').replace('+', '').strip()
				coluna_csv.insert(5, installs)
				last_updated = (coluna_csv.pop(10)).replace(',', '').strip()		
				coluna_csv.insert(10, last_updated)		
				linhas_csv.append(coluna_csv)
		
		with open('googleplaystore.csv', mode='w') as csvDataFileWrite:		
			writer = csv.writer(csvDataFileWrite)
			writer.writerows(linhas_csv)
		
	except IOError:
		print("Erro: Arquivo nao encontrado ou nao e possivel ler o arquivo")
	else:
		print("Dataset limpo e gravado com sucesso")