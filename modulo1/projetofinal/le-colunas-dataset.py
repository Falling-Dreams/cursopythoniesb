import csv

tamanho = []
with open('googleplaystore.csv') as csvDataFile:	
	csvReader = csv.reader(csvDataFile)
	for coluna in csvReader:
		tamanho.append(int(coluna[4]))

print(max(tamanho))


