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
			#last_updated = (coluna.pop(10)).replace(',', '/').replace('January','01/').replace('February','02/').replace('March','03/').replace('April','04/')\
			#.replace('May','05/').replace('June','06/').replace('July','07/').replace('August','08/').replace('September','09/').replace('October','10/')\
			#.replace('November','11/').replace('December','12/').replace(' ','').strip()
			last_updated = (coluna.pop(10)).replace(',', '').strip()		
			coluna.insert(10, last_updated)		
			linhas.append(coluna)
	#print(*linhas,sep='\n')

	with open('googleplaystore.csv', mode='w') as csvDataFileWrite:		
		writer = csv.writer(csvDataFileWrite)
		writer.writerows(linhas)
		



