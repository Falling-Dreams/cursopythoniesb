def manipula_dataset():
	import csv
	linhas = []
	with open('googleplaystore.csv') as csvDataFile:	
		csvReader = csv.reader(csvDataFile)
		next(csvDataFile)
		for coluna in csvReader:
			app = (coluna.pop(0)).replace(',', '').replace('.', '').strip()		
			coluna.insert(0, app)
			rating = (coluna.pop(2)).replace('NaN', '0').strip()
			coluna.insert(2, rating)		
			size = (coluna.pop(4)).replace('.', '').replace('k', '000').replace('M', '000000').replace('Varies with device', '0').replace('+', '').replace(',','')\
			.strip()
			coluna.insert(4, size)		
			installs = (coluna.pop(5)).replace(',', '').replace('+', '').strip()
			coluna.insert(5, installs)
			last_updated = (coluna.pop(10)).replace(',', '').strip()		
			coluna.insert(10, last_updated)		
			linhas.append(coluna)
	#print(*linhas,sep='\n')

	with open('googleplaystore.csv', mode='w') as csvDataFileWrite:		
		writer = csv.writer(csvDataFileWrite)
		writer.writerows(linhas)
		



