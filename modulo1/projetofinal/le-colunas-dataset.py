import csv
linhas = []
avaliacao = []
with open('googleplaystore_original.csv') as csvDataFile:	
	csvReader = csv.reader(csvDataFile)
	for coluna in csvReader:
		avaliacao.append(coluna[2])
		#print((coluna[4]))

print(*sorted(avaliacao),sep='\n')

