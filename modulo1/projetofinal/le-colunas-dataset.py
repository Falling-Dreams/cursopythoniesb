import csv
linhas = []
avaliacao = []
with open('googleplaystore.csv') as csvDataFile:	
	csvReader = csv.reader(csvDataFile)
	for coluna in csvReader:
		avaliacao.append(float(coluna[2]))
		#print((coluna[4]))

#print(sum(avaliacao)/len(avaliacao))
print(avaliacao)
